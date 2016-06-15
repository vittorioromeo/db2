import Connection
import getJson
import datetime
import matplotlib.pyplot as plt
import numpy
import math

def eliminaTuttiDati():
    tab = ["patient"]
    i = 0
    while (i < len(tab)):
        query = "truncate " + tab[i] + ";"
        Connection.update(query)
        i = i + 1

def inserisciAllData(scelta):
    people = getJson.getAllData(scelta)
    step = ''
    for x in people:
        step = ''
        query = "insert into patient (id, name, width, height, l_shank, l_thigh, lokomat_shank, lokomat_thigh, " \
                "lokomat_recorded, version, legtype, lwalk_training_duration, lwalk_distance, step_datas) " \
                "values ("+ str(x['id'])+", '" + str(x['name']) + "', " + str(x['width']) + ", "+ str(x['height']) +", "+ str(x['l_shank'])+", "+ str(x['l_thigh'])+", " \
                + str(x['lokomat_shank'])+", "+ str(x['lokomat_thigh'])+", "+ str(x['lokomat_recorded'])+", '"+ str(x['version'])+"', '"+ str(x['legtype'])+"', " \
                + str(x['lwalk_training_duration'])+", "+ str(x['lwalk_distance'])+", "
        step += "["
        for s in x['step_datas']:
            step += "{step_value: "
            step += "["
            for a in s:
                if (a == None):
                    step += "'None', "
                else:
                    step += "'"+str(a)+"', "
            step = step[:-2]
            step += "]}, "
        if(len(x['step_datas']) > 0):
            step = step[:-2]
        step += "]"
        query += step
        query += ");"

        Connection.update(query)

def printMedia(all_first, all_media, scelta):
    all_mean = []
    all_stddev = []
    all_conf = []
    eConf = {'ecolor': '0.3'}

    # Media delle query
    for a in all_media:
        mean = numpy.mean(a)
        stddev = numpy.std(a)
        conf = 0.95 * (stddev / math.sqrt(len(a)))
        all_mean.append(mean)
        all_stddev.append(stddev)
        all_conf.append(conf)

    count = 0
    for firstTime in all_first:
        plt.bar(count, firstTime, width=0.5, color='g')
        count += 2

    count = 0
    i=0
    while(i<len(all_mean)):
        plt.bar(count + 0.5, all_mean[i], width=0.5, yerr=all_conf[i], error_kw=eConf, color='r')
        count += 2
        i += 1

    plt.xticks([0.5, 2.5, 4.5, 6.5], ['10', '100', '1000', '10000'])
    plt.savefig('doc/query' + str(scelta+1) + '.png')
    plt.clf()

def iterazioneQuery():

    for i in range(0,2):
        if(i==0):

            tempi = []
            all_media = []
            all_first = []

            for a in range(0,4):
                print "situazione: query " + str(i+1) + " dataset " + str(a+1)
                #elimino dati su db e carico dataset
                eliminaTuttiDati()
                inserisciAllData(a)
                for _ in range(0, 31):
                    #eseguo la prima query sul dataset 30 volte
                    tPrima = datetime.datetime.now()
                    risultato = Connection.query1()
                    tTotale = datetime.datetime.now() - tPrima
                    tTotale = tTotale.total_seconds()
                    tempi.append(tTotale)
                # dentro first metto il tempo di esecuzione della prima query
                # dentro tempi i rimanenti 30 tempi calcolati
                first = tempi[0]
                tempi = tempi[1:]

                all_media.append(tempi)
                all_first.append(first)

            printMedia(all_first, all_media, i)

        elif(i==1):

            tempi = []
            all_media = []
            all_first = []

            for a in range(0, 4):
                print "situazione: query " + str(i + 1) + " dataset " + str(a + 1)
                # elimino dati su db e carico dataset
                eliminaTuttiDati()
                inserisciAllData(a)
                for _ in range(0, 31):
                    # eseguo la prima query sul dataset 30 volte
                    tPrima = datetime.datetime.now()
                    risultato = Connection.query2()
                    tTotale = datetime.datetime.now() - tPrima
                    tTotale = tTotale.total_seconds()
                    tempi.append(tTotale)
                # dentro first metto il tempo di esecuzione della prima query
                # dentro tempi i rimanenti 30 tempi calcolati
                first = tempi[0]
                tempi = tempi[1:]

                all_media.append(tempi)
                all_first.append(first)

            printMedia(all_first, all_media, i)

        elif(i==2):

            tempi = []
            all_media = []
            all_first = []

            for a in range(0, 4):
                print "situazione: query " + str(i + 1) + " dataset " + str(a + 1)
                # elimino dati su db e carico dataset
                eliminaTuttiDati()
                inserisciAllData(a)
                for _ in range(0, 31):
                    # eseguo la prima query sul dataset 30 volte
                    tPrima = datetime.datetime.now()
                    risultato = Connection.query3()
                    tTotale = datetime.datetime.now() - tPrima
                    tTotale = tTotale.total_seconds()
                    tempi.append(tTotale)
                # dentro first metto il tempo di esecuzione della prima query
                # dentro tempi i rimanenti 30 tempi calcolati
                first = tempi[0]
                tempi = tempi[1:]

                all_media.append(tempi)
                all_first.append(first)

            printMedia(all_first, all_media, i)

        i+=1

plt.clf()
print("inizio processo")
tPrima = datetime.datetime.now()
iterazioneQuery()
tTotale = datetime.datetime.now() - tPrima
tTotale = tTotale.total_seconds()
print("processo terminato in: " +str(tTotale)+ " secondi")
