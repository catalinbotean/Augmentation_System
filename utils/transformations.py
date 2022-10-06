import sys

import augmentation.dummy
import cv2
import logging

transformation_dictionary = {
    "TRANSFORMATION_1": "dummy1",
    "TRANSFORMATION_2": "dummy2",
    "TRANSFORMATION_3": "dummy3",
    "TRANSFORMATION_4": "dummy4",
    "TRANSFORMATION_5": "dummy5"
}


def apply_augmentation(images, processes, new_directory):
    count = 1
    for process in processes:
        for image in images:
            image_name, image_data = image
            transformations_name = ''
            for transformation in process:
                decode_transformation = transformation.split(' ')
                transformations_name = transformations_name + decode_transformation[0]+'_'
                function_name = transformation_dictionary[decode_transformation[0]]
                augmentation_function = getattr(augmentation.dummy, function_name)
                image_data = augmentation_function(image_data, decode_transformation[1])
            status = cv2.imwrite(new_directory+'/'+image_name+'_'+transformations_name+str(count)+'.jpg', image_data)
            if not status:
                logging.error(f'ERROR: Writing {new_directory}/{image_name}_{transformations_name}{count}.jpg has failed')
                sys.exit()
            count = count + 1
            logging.info(f'I have processed the image {image_name}')
        logging.info(f'I have applied {transformations_name} to all images')
    logging.info('I have applied all the processes')
