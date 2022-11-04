import numpy as np
import logging


def translation(image, parameters):
    x = int(parameters[0])
    y = int(parameters[1])
    image_x = np.zeros_like(image)
    image_y = np.zeros_like(image)
    if x > 0:
        image_x[:, x:, :] = image[:, :-x, :]
    elif x < 0:
        x = abs(x)
        image_x[:, :-x, :] = image[:, x:, :]
    else:
        image_x = image
    if y > 0:
        image_y[y:, :, :] = image_x[:-y, :, :]
    elif y < 0:
        y = abs(y)
        image_y[:-y, :, :] = image_x[y:, :, :]
    else:
        image_y = image_x
    logging.info(f'I have used Translation algorithm with x {x} and y {y}')
    return image_y
