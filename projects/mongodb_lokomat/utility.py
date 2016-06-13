import json

def caricaDatiDaJson(jsonFile):
    with open(jsonFile) as data_file:
        data = json.load(data_file)
        return data
