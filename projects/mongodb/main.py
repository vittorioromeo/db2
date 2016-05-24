from pymongo import *
import json
from caricaDati import *
import time
from query import *

tempoIniziale = time.time()

client = MongoClient("localhost", 27017)
db = client.test

data = caricaDatiDaJson()
pprint(data)

tempoFinale = time.time()

print str("\n Tempo iniziale ") + str(tempoIniziale) + str("\n Tempo finale ") + str(tempoFinale) + str("\n Tempo totale ") + str(tempoFinale-tempoIniziale)



