import logging


def flip(image, parameters):
    x = int(parameters[0])
    y = int(parameters[1])
    if x == 1:
        image_x = image[:, ::-1, :]
    else:
        image_x = image
    if y == 1:
        image_y = image_x[::-1, :, :]
    else:
        image_y = image_x
    logging.info(f'I have used Flip algorithm with x {x} and y {y}')
    return image_y
