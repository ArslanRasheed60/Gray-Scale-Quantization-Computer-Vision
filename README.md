"# Gray-Scale-Quantization-Computer-Vision" 

## Applying Gray level Quantization 
> 
> Quantization size (2, 4, 8, 16, 32, 64, 128)

## Quantization Level
> 
> High Level -> Move all quantized bits to maximum value
> 
> Low Level -> Move all quantized bits to minimum value
> 
> Middle Level -> Move all quantized bits to center value

### You need to close all windows for testing other mapping level
>
> Note: Greater the resolution of image greater will be the prcoessing time
>

# File Structure and setup
>
> First you need to install the important libraries
>
> For installation run this command: [pip install -r requirements.txt]
>

## Utils.py
> All functions like high level quantization, low level quantization and mid level quantization are there.  
>
## console.py
>
> To run the project on console. 
>
> Just run this command: [python console.py]
>
## Index.html and server.py
>
> To run the project on Web. Just run index.html file. But you need to start the server first. 
>
> For server, run this command: [uvicorn server:app --reload]
>

