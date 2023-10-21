import numpy as np
import cv2

TOTAL_COLOR_VALUE = 256


def high_level_mapping_gray_scale(matrix, quantization_size):
    
    #calculate the key
    key = int(TOTAL_COLOR_VALUE / quantization_size)

    # generate range of values according to the key
    quantized_key_array = [i-1 for i in range(key, TOTAL_COLOR_VALUE + key, key)]

    #dimensions of the original matrix
    height = len(matrix)
    width = len(matrix[0])

    new_matrix = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(0, height):
        for j in range(0, width):
            matrix_value = int(matrix[i][j])
            for index, value in enumerate(quantized_key_array):
                if quantized_key_array[0] > matrix_value:
                    matrix_value = quantized_key_array[0]
                    break
                elif index > 0 and quantized_key_array[index - 1] < matrix_value \
                                    and quantized_key_array[index] > matrix_value:
                    matrix_value = quantized_key_array[index]
                    break

            new_matrix[i][j] = matrix_value
            

    return new_matrix

# print(high_level_mapping_gray_scale([[11,27],[128,255]], 4))


def low_level_mapping_gray_scale(matrix, quantization_size):
    
    #calculate the key
    key = int(TOTAL_COLOR_VALUE / quantization_size)

    # generate range of values according to the key
    quantized_key_array = [i for i in range(0, TOTAL_COLOR_VALUE, key)]

    #dimensions of the original matrix
    height = len(matrix)
    width = len(matrix[0])

    new_matrix = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(0, height):
        for j in range(0, width):
            matrix_value = int(matrix[i][j])
            for index, value in enumerate(quantized_key_array):
                if index + 1 < len(quantized_key_array) and quantized_key_array[index] <= matrix_value \
                                                            and quantized_key_array[index + 1] > matrix_value:
                    matrix_value = quantized_key_array[index]
                    break
                elif index == len(quantized_key_array) - 1 and quantized_key_array[index] < matrix_value:
                    matrix_value = quantized_key_array[index]
                    break

            new_matrix[i][j] = matrix_value
            

    return new_matrix
