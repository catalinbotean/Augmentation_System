import logging

from constants import CONFIG_FILE_PATH, DATE_FORMAT, LOGGING_FILE, LOGGING_FORMAT
from utils.parser import load_config_file

if __name__ == '__main__':
    logging.basicConfig(format=LOGGING_FORMAT, datefmt=DATE_FORMAT, level=logging.INFO, filename=LOGGING_FILE, filemode='w')
    logging.info('The config file is being loaded ...')
    data = load_config_file(CONFIG_FILE_PATH)
    logging.info('The config file has been loaded.')
    print(data)
