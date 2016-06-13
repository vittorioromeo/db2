import os
from pymongo import *
import matplotlib.pyplot as plt
import time
import utility
from query import *

client = MongoClient("localhost", 27017)
db = client.test

listaDataSet = ['ds10.json','ds100.json','ds1000.json','ds10000.json','ds100000.json']
#listaDataSet = ['ds10.json']

directory = "result"
if not os.path.exists(directory):
    os.makedirs(directory)

listaQuery = [primaQuery, secondaQuery, terzaQuery]
tempototaleIniziale = time.time()
#Eseguo il tutto per ogni dataset
for dataset in listaDataSet:
    queryEliminaCollection(db)
    data = utility.caricaDatiDaJson("../../../dataset_lokomat/" + dataset)
    #Inserisco dataSet
    for i in data:
        queryInserisciDati(db,i['id'],i['name'],i['width'],i['height'],i['l_shank'],i['l_thigh'],i['lokomat_shank'],i['lokomat_thigh']
                           ,i['lokomat_recorded'],i['version'],i['legtype'],i['lwalk_training_duration'],i['lwalk_distance']
                           ,i['step_datas'])
    #Eseguo query
    i=0
    for query in listaQuery:
        i = i + 1
        tempi = []
        #Stessa query 31 volte
        for _ in range(0, 31):
            tempo = time.time()
            query(db)
            tempoFinale = time.time() - tempo
            tempi.append(tempoFinale)
        plt.plot(tempi)
        plt.ylabel("Query n " + str(i))
        plt.xlabel(dataset)
        plt.savefig('result/' + dataset + 'Query' + str(i) + '.png')
        plt.clf()

tempototaleFinale = time.time()
print str("Il tempo totale e : ") + str(tempototaleFinale-tempototaleIniziale)