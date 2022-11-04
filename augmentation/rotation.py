import cv2
import numpy as np
import logging

from utils.files import convert_to_float64, convert_to_uint8


def rotation(image, parameter):
    param = parameter[0]
    image = convert_to_float64(image)
    center_width = image.shape[1] / 2
    center_height = image.shape[0] / 2
    rotation_matrix_2d = cv2.getRotationMatrix2D((center_width, center_height), int(param), 1)
    image = cv2.warpAffine(image, rotation_matrix_2d, (image.shape[1], image.shape[0]))
    image = np.array(image, dtype=np.uint8)
    logging.info(f'I have used Rotation algorithm with angle {param}')
    return convert_to_uint8(image)
