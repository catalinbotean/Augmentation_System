import numpy as np
import logging

from utils.files import convert_to_float64, convert_to_uint8


def contrast(image, parameter):
    param = parameter[0]
    image = convert_to_float64(image)
    # print(image)
    # print(image.shape)
    image = image * np.float64(param)
    image = image.clip(0.0, 255.0)
    image = np.array(image, dtype=np.uint8)
    logging.info(f'I have used Contrast algorithm with parameter {param}')
    return convert_to_uint8(image)
