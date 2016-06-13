import Connection
import getJson
import time
import matplotlib.pyplot as plt


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


def funzione(scelta):
    tempi = []
    for _ in range(0,31):
        tPrima = time.time()
        risultato = Connection.query("select * from patient;")
        tTotale = time.time() - tPrima
        tempi.append(tTotale)

    plt.plot(tempi)
    plt.ylabel("Query n " + str(1))
    plt.xlabel(scelta)
    plt.savefig('doc/' + str(scelta) + 'Query' + str(1) + '.png')
    plt.clf()

    print "Il tempo per fare la query 1 e': " + str(tTotale)

    tempi = []
    for _ in range(0,31):
        tPrima = time.time()
        risultato = Connection.query("SELECT * FROM patient WHERE name = 'SIVV33W0' allow filtering;")
        tTotale = time.time() - tPrima
        tempi.append(tTotale)

    plt.plot(tempi)
    plt.ylabel("Query n " + str(2))
    plt.xlabel(scelta)
    plt.savefig('doc/' + str(scelta) + 'Query' + str(2) + '.png')
    plt.clf()

    print "Il tempo per fare la query 2 e': " + str(tTotale)

    tempi = []
    x = []
    for _ in range(0,31):
        tPrima = time.time()
        risultato = Connection.query("select * from patient where lwalk_training_duration > 5000 allow filtering;")
        for a in risultato:
            if(a[11] != None):
                if((a[13]!=0.70338464) and (len(a[11])>4)):
                    x.append(a)
        tTotale = time.time() - tPrima
        tempi.append(tTotale)

    plt.plot(tempi)
    plt.ylabel("Query n " + str(3))
    plt.xlabel(scelta)
    plt.savefig('doc/' + str(scelta) + 'Query' + str(3) + '.png')
    plt.clf()

    print "Il tempo per fare la query 3 e': " + str(tTotale)

scelta = 0
while (scelta < 4):
    print scelta


    print "elimino elementi dal DB"
    eliminaTuttiDati()
    print "inserisco gli elementi dal DB"
    inserisciAllData(scelta)
    print "inizio le query"

    funzione(scelta)

    scelta = scelta + 1
