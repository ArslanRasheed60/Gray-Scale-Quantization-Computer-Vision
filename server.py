from fastapi import FastAPI, File, Query, UploadFile, Form
from fastapi.responses import FileResponse
from PIL import Image
from io import BytesIO
import numpy as np 
from fastapi.middleware.cors import CORSMiddleware

# internal imports
from Utils import high_level_mapping_gray_scale, \
                low_level_mapping_gray_scale, \
                    mid_level_mapping_gray_scale, \
                        mapping_rgb
app = FastAPI()

origins = ["*"]  

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
ALLOWED_SCALES = {2, 4, 8, 16, 32, 64, 128}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(file, colorFactor, scale):

    # processing of the grey level image
    if colorFactor == 0 or colorFactor == 1 or colorFactor == 2:
        with Image.open(file.file).convert('L') as img:
            img_array = np.array(img)
            # Perform image processing
            if colorFactor == 0:
                processed_array = low_level_mapping_gray_scale(img_array, scale)
            if colorFactor == 1:
                processed_array = mid_level_mapping_gray_scale(img_array, scale)
            if colorFactor == 2:
                processed_array = high_level_mapping_gray_scale(img_array, scale)

            processed_array = np.array(processed_array, dtype=np.uint8)
            # Convert the NumPy array back to an image
            processed_image = Image.fromarray(processed_array)
            # Save the processed image to a BytesIO object
            output = BytesIO()
            processed_image.save(output, format="PNG")
            output.seek(0)
            return output
    else:
        with Image.open(file.file).convert('RGB') as img:
            img_array = np.array(img)
            # Perform image processing 
            if colorFactor == 3:
                processed_array = mapping_rgb(img_array, scale, 1) #low level RGB mapping
            if colorFactor == 4:
                processed_array = mapping_rgb(img_array, scale, 2) #mid level RGB mapping
            if colorFactor == 5:
                processed_array = mapping_rgb(img_array, scale, 0) #high level RGB mapping

            processed_array = np.array(processed_array, dtype=np.uint8)
            # Convert the NumPy array back to an image
            processed_image = Image.fromarray(processed_array)
            # Save the processed image to a BytesIO object
            output = BytesIO()
            processed_image.save(output, format="PNG")
            output.seek(0)
            return output

@app.post("/processing/{colorFactor}/{scale}")
async def upload_image(file: UploadFile, colorFactor:int= 0 ,scale: int= 2):
    if allowed_file(file.filename) and scale in ALLOWED_SCALES:
        processed_image = process_image(file, colorFactor ,scale)
        # Save the processed image to a temporary file
        temp_filename = "./images/tempfile.png"
        with open(temp_filename, "wb") as temp_file:
            temp_file.write(processed_image.getvalue())
        
        # returning of processed image
        return FileResponse(temp_filename, media_type="image/png")
    else:
        return {"error": "Invalid file format or scale factor. Allowed formats: jpg, jpeg, png. Allowed scales: 2, 4, 8, 16, 32, 64, 128"}
