import cv2
import numpy as np
from Utils import high_level_mapping_gray_scale, low_level_mapping_gray_scale


IMAGE_URL = './images/blue_dice.png'


print("""
        Welcome to Computer Vision: A Gray Scale Quantization.

        Enter the Quantization Size. Choose From (2, 4, 8, 16, 32, 64, 128)
    """)
user_input = input("Enter Input: ")
try:

    if type(int(user_input)) != int:
        raise ValueError
    elif int(user_input) != 2 \
            and int(user_input) != 4 \
            and int(user_input) != 8 \
            and int(user_input) != 16 \
            and int(user_input) != 32 \
            and int(user_input) != 64 \
            and int(user_input) != 128:
        raise ValueError
    else:
        mappingLevel = input("""What kind of mapping do you want? 
            0: High Level
            1: Low Level
            2: Middle Level
            : """)
        try:
            
            if int(mappingLevel) != 0 and int(mappingLevel) != 1 and int(mappingLevel) != 2:
                raise ValueError
            
            # Read the image in grayscale
            input_image_grayscale = cv2.imread(IMAGE_URL, 0) 
            # Read the image in RGB
            input_image_RGB = cv2.imread(IMAGE_URL)
            
            if int(mappingLevel) == 0:
                # Perform zero-order interpolation for image enlargement
                mappedImage = high_level_mapping_gray_scale(input_image_grayscale, int(user_input))

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)

                # Display the original and mappedImage images
                cv2.imshow('Original Image GrayScale', input_image_grayscale)
                cv2.imshow('High Level Mapped Image GrayScale2', mappedImage)
                

                mappedImage = high_level_mapping_gray_scale(input_image_grayscale, 4)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('High Level Mapped Image GrayScale4', mappedImage)


                mappedImage = high_level_mapping_gray_scale(input_image_grayscale, 8)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('High Level Mapped Image GrayScale8', mappedImage)


                mappedImage = high_level_mapping_gray_scale(input_image_grayscale, 16)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('High Level Mapped Image GrayScale16', mappedImage)


                mappedImage = high_level_mapping_gray_scale(input_image_grayscale, 32)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('High Level Mapped Image GrayScale32', mappedImage)


                mappedImage = high_level_mapping_gray_scale(input_image_grayscale, 64)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('High Level Mapped Image GrayScale64', mappedImage)


                mappedImage = high_level_mapping_gray_scale(input_image_grayscale, 128)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('High Level Mapped Image GrayScale128', mappedImage)

            if int(mappingLevel) == 1:
                # Perform zero-order interpolation for image enlargement
                mappedImage = low_level_mapping_gray_scale(input_image_grayscale, int(user_input))

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)

                # Display the original and mappedImage images
                cv2.imshow('Original Image GrayScale', input_image_grayscale)
                cv2.imshow('Low Level Mapped Image GrayScale2', mappedImage)
                

                mappedImage = low_level_mapping_gray_scale(input_image_grayscale, 4)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('Low Level Mapped Image GrayScale4', mappedImage)


                mappedImage = low_level_mapping_gray_scale(input_image_grayscale, 8)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('Low Level Mapped Image GrayScale8', mappedImage)


                mappedImage = low_level_mapping_gray_scale(input_image_grayscale, 16)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('Low Level Mapped Image GrayScale16', mappedImage)


                mappedImage = low_level_mapping_gray_scale(input_image_grayscale, 32)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('Low Level Mapped Image GrayScale32', mappedImage)


                mappedImage = low_level_mapping_gray_scale(input_image_grayscale, 64)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('Low Level Mapped Image GrayScale64', mappedImage)


                mappedImage = low_level_mapping_gray_scale(input_image_grayscale, 128)

                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)
                cv2.imshow('Low Level Mapped Image GrayScale128', mappedImage)
            
            # if int(isRGBoutput) == 1:
            #     enlarged_image_RGB = zero_order_enlargement_rgb(input_image_RGB, ZERO_ORDER_KERNEL)
            #     enlarged_image_RGB = np.array(enlarged_image_RGB)  # Your image data here
            #     enlarged_image_RGB = np.uint8(enlarged_image_RGB)

            #     # Display the original and enlarged images
            #     cv2.imshow('Original Image RGB', input_image_RGB)
            #     cv2.imshow('Enlarged zer order Image RGB', enlarged_image_RGB)
            # else:
            #     print("Invalid Input")

            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except ValueError as ev:
            print("Invalid input value: ")
            print(ev)

    
except ValueError as e:
    print("Invalid input: ")
    print(e)


# gray scale enlargment (single channel)



# # first order hold

# # Perform zero-order interpolation for image enlargement
# enlarged_image = first_order_enlargement_gray_scale(input_image_grayscale, FIRST_ORDER_KERNEL)

# enlarged_image = np.array(enlarged_image)  # Your image data here
# enlarged_image = np.uint8(enlarged_image)

# # Display the original and enlarged images
# cv2.imshow('Enlarged first order Image GrayScale', enlarged_image)



# cv2.waitKey(0)
# cv2.destroyAllWindows()