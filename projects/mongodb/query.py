def queryInserisciPaziente(db):
    collection = db.Paziente
    collection.insert({
        "id" : 0,
		"cognome" : "gangemi",
		"nome" : "salvatore",
		"dataDiNascita": "05/06/1994",
		"indirizzo" : "via gangemi",
		"telefono" : "450445",
		"email" : "email@email.it"
   })

def queryPrendiPazienti(db):
    collection = db.Paziente
    print "\n INIZIO QUERY \n"
    pazienti = collection.find({'id': "0"})
    for paz in pazienti:
        print(paz)
    print "\n FINE QUERY \n"

def queryPrendiInstallazione(db):
    collection = db.Install
    print "\n INIZIO QUERY \n"
    installazioni = collection.find({'id': "0"})
    for ins in installazioni:
        print(ins)
    print "\n FINE QUERY \n"

def queryInserisciInstallazione(db):
    collection = db.Install
    collection.insert({
        "id" : 0,
		"dove" : "messina",
		"quando" : "24/05/2016",
		"id_paziente" : "0",
		"id_device" : "0",
   })

def queryInserisciDevice(db):
    collection = db.Device
    collection.insert({
        "id" : 0,
		"produttore" : "samsung",
		"modello" : "galaxy s2",
    })

def queryPrendiDevice(db):
    collection = db.Device
    print "\n INIZIO QUERY \n"
    devices = collection.find({'id': "0"})
    for dev in devices:
        print(dev)
    print "\n FINE QUERY \n"

def queryInserisciParametri(db):
    collection = db.Parametri
    collection.insert({
        "id" : 0,
		"descrizione" : "descrizione",
		"frequenza" : "frequenza",
    })

def queryPrendiParametri(db):
    collection = db.Parametri
    print "\n INIZIO QUERY \n"
    devices = collection.find({'id': "0"})
    for dev in devices:
        print(dev)
    print "\n FINE QUERY \n"







def queryInserisciOsservazioni(db):
    collection = db.Osservazioni
    collection.insert({
        "id" : "0",
		"timestamp" : "descrizione",
		"value" : "frequenza",
		"uom" : "uom",
		"id_parametro" : "0",
    })

def queryPrendiOsservazioni(db):
    collection = db.Osservazioni
    print "\n INIZIO QUERY \n"
    osservazioni = collection.find({'id': "0"})
    for oss in osservazioni:
        print(oss)
    print "\n FINE QUERY \n"







def queryInserisciEffetto(db):
    collection = db.Effetto
    collection.insert({
        "id" : "0",
		"id_osservazione" : "descrizione",
		"id_salute" : "frequenza",
    })

def queryPrendiEffetto(db):
    collection = db.Effetto
    print "\n INIZIO QUERY \n"
    salute = collection.find({'id': "0"})
    for sal in salute:
        print(sal)
    print "\n FINE QUERY \n"







def queryInserisciSalute(db):
    collection = db.Salute
    collection.insert({
        "id" : "0",
		"timestamp" : "descrizione",
		"malattia" : "frequenza",
		"grado_malattia" : "frequenza",
		"id_paziente" : "0"
    })

def queryPrendiSalute(db):
    collection = db.Salute
    print "\n INIZIO QUERY \n"
    salute = collection.find({'id': "0"})
    for sal in salute:
        print(sal)
    print "\n FINE QUERY \n"






