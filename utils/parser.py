import json
import logging


def load_config_file(file_name):
    file = open(file_name)
    file_data = json.load(file)
    data = parse_json_file(file_data)
    file.close()
    return data


def parse_json_file(file_data):
    data = []
    for process in file_data:
        logging.info(f'The data is processed for {process.capitalize()} ...')
        data.append(get_transformations_list(file_data[process]))
        logging.info('Processing is completed.')
    return data


def get_transformations_list(process):
    transformation_list = []
    for transformation in process:
        transformation_list.append(process[transformation])
    return transformation_list
