import json

def settaData(scelta):

    if(scelta == 0):
        with open('dataset10.json') as data:
            record = json.load(data)
    elif (scelta == 1):
        with open('dataset100.json') as data:
            record = json.load(data)
    elif (scelta == 2):
        with open('dataset1000.json') as data:
            record = json.load(data)
    elif (scelta == 3):
        with open('dataset10000.json') as data:
            record = json.load(data)
    elif (scelta == 4):
        with open('dataset100000.json') as data:
            record = json.load(data)
    return record

def getAffect(scelta):
    record = settaData(scelta)
    affect = record['affect']
    return affect


def getDevice(scelta):
    record = settaData(scelta)
    devices = record['devices']
    return devices


def getDoctor(scelta):
    record = settaData(scelta)
    doctors = record['doctors']
    return doctors


def getEvaluate(scelta):
    record = settaData(scelta)
    evaluate = record['evaluate']
    return evaluate


def getHealthState(scelta):
    record = settaData(scelta)
    health_states = record['health_states']
    return health_states


def getInstall(scelta):
    record = settaData(scelta)
    install = record['install']
    return install


def getMeasurement(scelta):
    record = settaData(scelta)
    measurement = record['measurement']
    return measurement


def getMonitoring(scelta):
    record = settaData(scelta)
    monitoring = record['monitoring']
    return monitoring


def getObservations(scelta):
    record = settaData(scelta)
    observations = record['observations']
    return observations


def getParameters(scelta):
    record = settaData(scelta)
    parameters = record['parameters']
    return parameters


def getPatients(scelta):
    record = settaData(scelta)
    patients = record['patients']
    return patients


def getRelated(scelta):
    record = settaData(scelta)
    related = record['related']
    return related


def getSet(scelta):
    record = settaData(scelta)
    set = record['set']
    return set


def getTherapies(scelta):
    record = settaData(scelta)
    therapies = record['therapies']
    return therapies