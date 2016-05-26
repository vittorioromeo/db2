from pymongo import *
import json
from caricaDati import *
import time
from query import *
from queryTest import *

client = MongoClient("localhost", 27017)
db = client.test

listaDataSet = ['ds10.json','ds100.json','ds1000.json','ds10000.json','ds100000.json']
for d in listaDataSet:
    settaDataset(client,db,d)
    listaQuery = [primaQuery,secondaQuery,terzaQuery,quartaQuery]
    i = 0
    print str("Benchmark per il dataset : ") + str(d)
    for q in listaQuery:
        tempoIniziale = time.time()
        for _ in range(0, 100):
            q(db)
        tempoFinale = time.time()
        i = i + 1
        print str("Iterazione n ") + str(i) + str(" tempo impiegato : ") + str(tempoFinale-tempoIniziale)
    print ""