from caricaDati import *
from query import *

def primaQuery(db):
    #SELECT * FROM patients
    queryPrendiPazienti(db)

def secondaQuery(db):
    #SELECT * FROM patients WHERE nome = ''
    data = db.Paziente.find({ 'nome' : 'SIVV33W0'})
    '''for ele in data:
        print ele'''

def terzaQuery(db):
    #SELECT patients,healthstate FROM patients JOIN healthstate ON (healstate.id_patient = patient_id) Where timestamp > ''
    data = db.Relativo.find({})
    for ele in data:
        id_salute = ele['id_salute']
        data2 = db.Salute.find({'id': id_salute, 'timestamp': { '$gt': 5000}})
        '''for ele2 in data2:
                print ele2'''

def quartaQuery(db):
    #4)seleziona le terapie dei pazienti che hanno installato un device nel (when)
    data = db.Install.find({'quando': {'$gt': 5000}})
    for ele in data:
        id_paziente = ele['id_paziente']
        data2 = db.Relativo.find({'id_paziente' : id_paziente})
        for ele2 in data2:
            id_salute = ele2['id_salute']
            data3 = db.Salute.find({'id' : id_salute})
            for ele3 in data3:
                id_salute = ele3['id']
                data4 = db.Settare.find({'id_salute': id_salute})
                for ele4 in data4:
                    id_terapia = ele4['id_terapia']
                    data5 = db.Terapia.find({'id': id_terapia})






        '''data2 = db.Install.find({'quando' : {'$gt' : 5000}})
        for ele2 in data2:
            id_paziente = ele2['id_paziente']
            data3 = db.Paziente.find({'id' : id_paziente})
            for ele3 in data3:
                id_paziente = ele3['id']
                data4 = db.Relativo.find({'id_paziente' : id_paziente})
                for ele4 in data4:
                    id_salute = ele4['id_salute']
                    data5 = db.Salute.find({'id' : id_salute})
                    for ele5 in data5:
                        id_salute = ele5['id']
                        data6 = db.Settare.find({'id_salute' : id_salute})
                        for ele6 in data6:
                            id_terapia = ele6['id_terapia']
                            data7 = db.Terapia.find({'id' : id_terapia})
                            for ele7 in data7:
                                print ele7'''

def settaDataset(client,db,dataset):
    eliminaDatabase(client)
    creaCollezioni(db)
    data10 = caricaDatiDaJson(dataset)
    popolaTutto(data10,db)

    '''
    data = db.Terapia.find({})
    for ele in data:
        id_terapia = ele['id']
        data2 = db.Settare.find({'id_terapia' : id_terapia})
        #prendo id_terapia

        for ele2 in data2:
            id_terapia2 = ele2['id_terapia']
            data3 = db.Salute.find({'id' : id_terapia2})
            #prendo id_salute

            for ele3 in data3:
                id_salute = ele3['id']
                data4 = db.Relativo.find({ 'id' : id_salute })
                #prendo id_paziente da paziente

                for ele4 in data4:
                    id_paziente = ele4['id_paziente']
                    data5 = db.Install.find({ 'id_paziente' : id_paziente, 'quando' : { '$gt': 990000} })

                    for ele5 in data5:
                        id_device = ele5['id_device']
                        data6 = db.Device.find({'id' : id_device})

                        for ele6 in data6:
                            print ele'''