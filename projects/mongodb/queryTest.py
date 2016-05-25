from query import *

def primaQuery(db):
    queryPrendiPazienti(db)

def secondaQuery(db):
    data = db.Paziente.find({ 'nome' : '8M6NKRHS'})
    for ele in data:
        print ele

def terzaQuery(db):
    data = db.Relativo.find({})
    for ele in data:
        id_salute = ele['id_salute']
        data2 = db.Salute.find({'id': id_salute, 'timestamp': { '$gt': 900000}})
        for ele2 in data2:
            print ele2

def quartaQuery(db):
    #4)seleziona le terapie dei pazienti che hanno installato un device nel (when)
    data = db.Settare.find({})
    #prendo id_terapia
    for ele in data:
        id_terapia = ele['id_terapia']
        #print id_terapia
        data2 = db.Salute.find({'id' : id_terapia})
        #prendo id_salute
        for ele2 in data2:
            id_salute = ele2['id']
            #print id_salute
            data3 = db.Relativo.find({ 'id' : id_salute })
            #prendo id_paziente da paziente
            for ele3 in data3:
                id_paziente = ele3['id_paziente']
                #print id_paziente
                data4 = db.Install.find({ 'id_paziente' : id_paziente, 'quando' : { '$gt': 990000} })
                for ele4 in data4:
                    print ele4