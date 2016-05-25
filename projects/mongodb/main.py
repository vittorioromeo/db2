from pymongo import *
import json
from caricaDati import *
import time
from query import *
from queryTest import *

tempoIniziale = time.time()

client = MongoClient("localhost", 27017)
db = client.test

'''data = db.Relativo.find({ 'id' : 0})

for ele in data:
    id_paziente = ele['id_paziente']
    id_salute = ele['id_salute']
    print id_paziente
    print id_salute
    print ele

data = db.Salute.find({ 'id' : id_salute})

for ele in data:
    print ele

data = db.Paziente.find({ 'id' : id_paziente })

for ele in data:
    print ele'''

quartaQuery(db)


tempoFinale = time.time()

print str("\n Tempo iniziale ") + str(tempoIniziale) + str("\n Tempo finale ") + str(tempoFinale) + str("\n Tempo totale ") + str(tempoFinale-tempoIniziale)



