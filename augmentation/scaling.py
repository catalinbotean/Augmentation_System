import cv2
import numpy as np
import logging

from utils.files import convert_to_float64, convert_to_uint8


def scaling(image, parameter):
    scale_x = float(parameter[0])
    scale_y = float(parameter[1])
    image = convert_to_float64(image)
    scaling_matrix = np.float64([[scale_x, 0, 0], [0, scale_y, 0]])
    image = cv2.warpAffine(image, scaling_matrix, (image.shape[1], image.shape[0]))
    image = np.array(image, dtype=np.uint8)
    logging.info(f'I have used Scaling algorithm with scale_x {scale_x} and scale_y {scale_y}')
    return convert_to_uint8(image)
