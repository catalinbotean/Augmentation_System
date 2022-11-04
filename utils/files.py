import logging
import os
import cv2
import sys
import numpy as np


def get_images(directory):
    if directory != "No directory selected":
        images_name = sorted(os.listdir(directory))
        for i, img in enumerate(images_name):
            images_name[i] = os.path.join(directory, img)
        logging.info('The name of every image was received')
        return images_name
    else:
        logging.error('ERROR: No directory has been selected')
        sys.exit()


def read_images(selected_images_path):
    images = []
    for path in selected_images_path:
        image = cv2.imread(path, cv2.IMREAD_COLOR)
        image_tuple = (os.path.basename(path).split('.')[0], image)
        images.append(image_tuple)
        logging.info('I have read one image')
    return images


def create_directory(directory_path):
    new_directory = directory_path + '_aug'
    if os.path.exists(new_directory):
        logging.error('ERROR:The directory already exists')
        sys.exit()
    os.mkdir(new_directory)
    logging.info('The new directory was created')
    return new_directory


def convert_to_float64(image):
    return np.array(image, dtype=np.float64)


def convert_to_uint8(image):
    return np.array(image, dtype=np.uint8)
