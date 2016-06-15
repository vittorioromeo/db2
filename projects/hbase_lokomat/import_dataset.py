import json

def import_data_set(path):

    with open(path) as data_file:
        data_set = json.load(data_file)
    return data_set
