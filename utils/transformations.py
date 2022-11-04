import copy
import sys

import augmentation.index
import cv2
import logging

transformation_dictionary = {
    "Brightness": "brightness",
    "Contrast": "contrast",
    "GaussianBlur": "gaussian_blur",
    "Rotation": "rotation",
    "Scaling": "scaling",
    "Translation": "translation",
    "Flip": "flip"
}


def apply_augmentation(images, processes, new_directory):
    count = 1
    for process in processes:
        for image in images:
            image_name, image_data = image
            transformations_name = ''
            temporary_image_data = copy.copy(image_data)
            for transformation in process:
                decode_transformation = transformation.split(' ')
                transformations_name = transformations_name + decode_transformation[0]+'_'
                function_name = transformation_dictionary[decode_transformation[0]]
                augmentation_function = getattr(augmentation.index, function_name)
                if len(decode_transformation) == 3:
                    parameter = [decode_transformation[1]]+[decode_transformation[2]]
                else:
                    parameter = [decode_transformation[1]]
                temporary_image_data = augmentation_function(temporary_image_data, parameter)
            status = cv2.imwrite(new_directory+'/'+image_name+'_'+transformations_name+str(count)+'.jpg', temporary_image_data)
            if not status:
                logging.error(f'ERROR: Writing {new_directory}/{image_name}_{transformations_name}{count}.jpg has failed')
                sys.exit()
            count = count + 1
            logging.info(f'I have processed the image {image_name}')
        logging.info(f'I have applied {transformations_name} to all images')
    logging.info('I have applied all the processes')
