import numpy as np
import cv2
import logging

from utils.files import convert_to_float64, convert_to_uint8


def gaussian_blur(image, parameter):
    sigma = parameter[0]
    kernel_size = int(parameter[1])
    sigma = np.float64(sigma)
    image = convert_to_float64(image)
    kernel = np.zeros((kernel_size, kernel_size))
    for i in range(kernel_size):
        for j in range(kernel_size):
            kernel[i, j] = np.exp(-((i - kernel_size // 2) ** 2 + (j - kernel_size // 2) ** 2) / (2 * sigma ** 2))
    kernel = kernel / np.sum(kernel)
    image = cv2.filter2D(image, -1, kernel)
    logging.info(f'I have used Gaussian Blur algorithm with sigma {sigma} and kernel size {kernel_size}')
    return convert_to_uint8(image)
