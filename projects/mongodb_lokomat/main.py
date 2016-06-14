import os
import numpy as np
from matplotlib.font_manager import FontProperties
from pymongo import *
import matplotlib.pyplot as plt
import time
import utility
from query import *

client = MongoClient("localhost", 27017)
db = client.test

listaDataSet = ['ds10.json','ds100.json','ds1000.json','ds10000.json','ds100000.json']
listaDatiPrimaQuery = []
listaDatiOtherQuery = []
listTitoli = ['Benchmark prima query', 'Benchmark seconda query', 'Benchmark terza query']
#listaDataSet = ['ds10.json','ds100.json']

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
    contatoreQuery = 0
    for query in listaQuery:
        #Stessa query 31 volte
        sommaTempi = 0
        for _ in range(0, 31):
            tempo = time.time()
            query(db)
            tempoFinale = time.time() - tempo
            if (_ == 0):
                listaDatiPrimaQuery.append(tempoFinale)
            else:
                sommaTempi = sommaTempi + tempoFinale
        sommaTempi = sommaTempi / 30
        listaDatiOtherQuery.append(sommaTempi)

i = 0
for __ in range(0, 3):
    numDataset = 0
    for _ in range(0,5):
        print i
        istogrammaPrimaQuery = plt.bar(numDataset, listaDatiPrimaQuery[i], 0.5, color='b')

        numDataset = numDataset + 0.5
        istogrammaOtherQuery = plt.bar(numDataset, listaDatiOtherQuery[i], 0.5, color='r')
        numDataset = numDataset + 1.5
        i = i + 1
    plt.ylabel('Time', fontsize=12)
    plt.xlabel('Dataset', fontsize=12)
    plt.title(listTitoli[__])
    plt.xticks([0.5, 2.5, 4.5, 6.5, 8.5], ['10', '100', '1000', '10000', '100000'], rotation='horizontal')
    fontP = FontProperties()
    fontP.set_size('small')
    #legend([plot1], "title", prop=fontP)
    plt.legend([istogrammaPrimaQuery, istogrammaOtherQuery], ('Prima Query', 'Media altre query'), prop=fontP, loc='upper center', bbox_to_anchor=(0.5, -0.05),
              fancybox=True, shadow=True, ncol=2)
    plt.savefig('result/' + listTitoli[__] + '.png')
    plt.clf()

tempototaleFinale = time.time()
print str("Il tempo totale e : ") + str(tempototaleFinale-tempototaleIniziale)