from pprint import pprint
from query import *

def popolaPazienti(data,db):
    for i in data['patients']:
        pprint(i)
        queryInserisciPaziente(db, i['id'], i['surname'], i['name'], i['date_of_birth'], i['address'], i['telephone'], i['email'])

def popolaDevices(data,db):
    for i in data['devices']:
        pprint(i)
        queryInserisciDevice(db, i['id'], i['manufacturer'], i['model'])

def popolaParametri(data,db):
    for i in data['parameters']:
        pprint(i)
        queryInserisciParametri(db, i['id'], i['description'], i['frequency'])

def popolaOsservazione(data,db):
    for i in data['observations']:
        pprint(i)
        queryInserisciOsservazioni(db, i['id'], i['timestamp'], i['value'],i['uom'])

def popolaTerapia(data,db):
    for i in data['therapies']:
        pprint(i)
        queryInserisciTerapia(db, i['id'], i['starting_time'], i['duration'],i['medicine'], i['posology'])

def popolaSalute(data,db):
    for i in data['health_states']:
        pprint(i)
        queryInserisciSalute(db, i['id'], i['timestamp'], i['disease_type'], i['disease_degree'])

def popolaDottore(data,db):
    for i in data['doctors']:
        pprint(i)
        queryInserisciDottore(db, i['id'], i['name'], i['surname'])

def popolaInstall(data,db):
    for i in data['install']:
        pprint(i)
        queryInserisciInstallazione(db, i['id'], i['where'], i['when'], i['id_patients'], i['id_devices'])

def popolaMisurazioni(data,db):
    for i in data['measurement']:
        pprint(i)
        queryInserisciMisurazioni(db, i['id'], i['id_devices'], i['id_parameters'])

def popolaEffetto(data,db):
    for i in data['affect']:
        pprint(i)
        queryInserisciEffetto(db, i['id'], i['id_observations'], i['id_health_states'])

def popolaValutare(data,db):
    for i in data['evaluate']:
        pprint(i)
        queryInserisciValutare(db, i['id'], i['id_doctors'], i['id_health_states'])

def popolaSettare(data,db):
    for i in data['set']:
        pprint(i)
        queryInserisciSettare(db, i['id'], i['id_therapies'], i['id_health_states'])

def popolaMonitoraggio(data,db):
    for i in data['monitoring']:
        pprint(i)
        queryInserisciMonitoraggio(db, i['id'], i['id_observations'], i['id_parameters'])

def popolaRelativo(data,db):
    for i in data['related']:
        pprint(i)
        queryInserisciRelativo(db, i['id'], i['id_health_states'], i['id_patients'])

def popolaTutto(data,db):
    popolaPazienti(data,db)
    popolaDevices(data,db)
    popolaDottore(data,db)
    popolaEffetto(data,db)
    popolaInstall(data,db)
    popolaMisurazioni(data,db)
    popolaMonitoraggio(data,db)
    popolaOsservazione(data,db)
    popolaParametri(data,db)
    popolaRelativo(data,db)
    popolaSalute(data,db)
    popolaSettare(data,db)
    popolaTerapia(data,db)
    popolaValutare(data,db)