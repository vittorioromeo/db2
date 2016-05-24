#PAZIENTE
def queryInserisciPaziente(db,id,cognome,nome,data,indirizzo,telefono,email):
    collection = db.Paziente
    collection.insert({
        "id" : id,
		"cognome" : nome,
		"nome" : cognome,
		"dataDiNascita": data,
		"indirizzo" : indirizzo,
		"telefono" : telefono,
		"email" : email,
   })

def queryPrendiPazienti(db):
    collection = db.Paziente
    print "\n INIZIO QUERY \n"
    pazienti = collection.find({})
    for paz in pazienti:
        print(paz)
    print "\n FINE QUERY \n"


#INSTALLAZIONE

def queryInserisciInstallazione(db,id,dove,quando,id_paziente,id_device):
    collection = db.Install
    collection.insert({
        "id" : id,
		"dove" : dove,
		"quando" : quando,
		"id_paziente" : id_paziente,
		"id_device" : id_device,
   })

def queryPrendiInstallazione(db):
    collection = db.Install
    print "\n INIZIO QUERY \n"
    installazioni = collection.find({})
    for ins in installazioni:
        print(ins)
    print "\n FINE QUERY \n"


#DEVICE

def queryInserisciDevice(db,id,produttore,modello):
    collection = db.Device
    collection.insert({
        "id" : id,
		"produttore" : produttore,
		"modello" : modello,
    })

def queryPrendiDevice(db):
    collection = db.Device
    print "\n INIZIO QUERY \n"
    devices = collection.find({})
    for dev in devices:
        print(dev)
    print "\n FINE QUERY \n"


#PARAMETRI

def queryInserisciParametri(db,id,descrizione,frequenza):
    collection = db.Parametri
    collection.insert({
        "id" : id,
		"descrizione" : descrizione,
		"frequenza" : frequenza,
    })

def queryPrendiParametri(db):
    collection = db.Parametri
    print "\n INIZIO QUERY \n"
    devices = collection.find({})
    for dev in devices:
        print(dev)
    print "\n FINE QUERY \n"



#MISURAZIONI

def queryInserisciMisurazioni(db,id,id_device,id_parametro):
    collection = db.Misurazioni
    collection.insert({
        "id" : id,
		"id_device" : id_device,
		"id_parametro" : id_parametro,
    })

def queryPrendiMisurazioni(db):
    collection = db.Misurazioni
    print "\n INIZIO QUERY \n"
    devices = collection.find({})
    for dev in devices:
        print(dev)
    print "\n FINE QUERY \n"


#OSSERVAZIONI

def queryInserisciOsservazioni(db,id,timestamp,value,uom):
    collection = db.Osservazioni
    collection.insert({
        "id" : id,
		"timestamp" : timestamp,
		"value" : value,
		"uom" : uom,
    })

def queryPrendiOsservazioni(db):
    collection = db.Osservazioni
    print "\n INIZIO QUERY \n"
    osservazioni = collection.find({})
    for oss in osservazioni:
        print(oss)
    print "\n FINE QUERY \n"



#EFFETTO

def queryInserisciEffetto(db,id,id_osservazione,id_salute):
    collection = db.Effetto
    collection.insert({
        "id" : id,
		"id_osservazione" : id_osservazione,
		"id_salute" : id_salute,
    })

def queryPrendiEffetto(db):
    collection = db.Effetto
    print "\n INIZIO QUERY \n"
    salute = collection.find({})
    for sal in salute:
        print(sal)
    print "\n FINE QUERY \n"



#SALUTE

def queryInserisciSalute(db,id,timestamp,malattia,grado_malattia):
    collection = db.Salute
    collection.insert({
        "id" : id,
		"timestamp" : timestamp,
		"malattia" : malattia,
		"grado_malattia" : grado_malattia,
    })

def queryPrendiSalute(db):
    collection = db.Salute
    print "\n INIZIO QUERY \n"
    salute = collection.find({})
    for sal in salute:
        print(sal)
    print "\n FINE QUERY \n"



#SETTARE

def queryInserisciSettare(db,id,id_terapia,id_salute):
    collection = db.Settare
    collection.insert({
        "id" : id,
		"id_terapia" : id_terapia,
		"id_salute" : id_salute,
    })

def queryPrendiSettare(db):
    collection = db.Settare
    print "\n INIZIO QUERY \n"
    salute = collection.find({})
    for sal in salute:
        print(sal)
    print "\n FINE QUERY \n"



#TERAPIA

def queryInserisciTerapia(db,id,tempo_avvio,durata,medicina,posologia):
    collection = db.Terapia
    collection.insert({
        "id" : id,
		"tempo_avvio" : tempo_avvio,
		"durata" : durata,
		"medicina" : medicina,
		"posologia" : posologia,
    })

def queryPrendiTerapia(db):
    collection = db.Terapia
    print "\n INIZIO QUERY \n"
    salute = collection.find({})
    for sal in salute:
        print(sal)
    print "\n FINE QUERY \n"



#VALUTARE

def queryInserisciValutare(db,id,id_dottore,id_salute):
    collection = db.Valutare
    collection.insert({
        "id" : id,
		"id_dottore" : id_dottore,
		"id_salute" : id_salute,
    })

def queryPrendiValutare(db):
    collection = db.Valutare
    print "\n INIZIO QUERY \n"
    salute = collection.find({})
    for sal in salute:
        print(sal)
    print "\n FINE QUERY \n"



#DOTTORE

def queryInserisciDottore(db,id,nome,cognome):
    collection = db.Dottore
    collection.insert({
        "id" : id,
		"nome" : nome,
		"cognome" : cognome,
    })

def queryPrendiDottore(db):
    collection = db.Dottore
    print "\n INIZIO QUERY \n"
    salute = collection.find({})
    for sal in salute:
        print(sal)
    print "\n FINE QUERY \n"



#MONITORAGGIO

def queryInserisciMonitoraggio(db,id,id_osservazione,id_parametro):
    collection = db.Monitoraggio
    collection.insert({
        "id" : id,
		"id_osservazione" : id_osservazione,
		"id_parametro" : id_parametro,
    })

def queryPrendiMonitoraggio(db):
    collection = db.Monitoraggio
    print "\n INIZIO QUERY \n"
    salute = collection.find({})
    for sal in salute:
        print(sal)
    print "\n FINE QUERY \n"



#RELATIVO

def queryInserisciRelativo(db,id,id_salute,id_paziente):
    collection = db.Relativo
    collection.insert({
        "id" : id,
		"id_salute" : id_salute,
		"id_paziente" : id_paziente,
    })

def queryPrendiRelativo(db):
    collection = db.Relativo
    print "\n INIZIO QUERY \n"
    salute = collection.find({})
    for sal in salute:
        print(sal)
    print "\n FINE QUERY \n"