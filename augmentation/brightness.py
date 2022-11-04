import logging
import numpy as np

from utils.files import convert_to_uint8, convert_to_float64


def truncate_pixel(pixel_value, parameter):
    new_value = pixel_value + np.float64(parameter)
    return np.maximum(0., np.minimum(255., new_value))


def brightness(image, parameter):
    param = parameter[0]
    image = convert_to_float64(image)
    # print(image)
    # print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    for i in range(height):
        for j in range(width):
            for k in range(channel):
                image[i, j, k] = truncate_pixel(image[i, j, k], param)
    logging.info(f'I have used Brightness algorithm with parameter {param}')
    return convert_to_uint8(image)
