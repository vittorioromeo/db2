import Connection
import getJson
import time



def eliminaTuttiDati():
    tab = ["affect", "device", "doctor", "evaluate", "health_state", "install", "measurement", "monitoring", "observation", "parameter", "patient", "related", "set_", "therapy"]
    i = 0
    while (i < len(tab)):
        query = "truncate " + tab[i] + ";"
        Connection.update(query)
        i = i + 1

def inserisciAffect(scelta):
    affect = getJson.getAffect(scelta)
    for x in affect:
        query = "insert into affect (id_health_state, id_observation) " \
                "values ( " + str(x['id_observations']) + ", " + str(
            x['id_health_states']) + " );"
        Connection.update(query)

def inserisciDevices(scelta):
    devices = getJson.getDevice(scelta)
    for x in devices:
        query = "insert into device (id, manufacturer, model) " \
                "values (" + str(x['id']) + ", '"+ x['manufacturer'] +"' , '"+ x['model'] +"') ; "
        Connection.update(query)

def inserisciDoctors(scelta):
    doctors = getJson.getDoctor(scelta)
    for x in doctors:
        query = "insert into doctor (id, name, surname)" \
                " values (" + str(x['id']) + ", '" + x['name'] + "', '" + x['surname'] + "' );"
        Connection.update(query)

def inserisciEvaluate(scelta):
    evaluate = getJson.getEvaluate(scelta)
    for x in evaluate:
        query = "insert into evaluate (id_doctor, id_health_state) " \
                "values (" + str(x['id_doctors']) + ", " + str(x['id_health_states']) + ");"
        Connection.update(query)

def inserisciHealth_states(scelta):
    health_states = getJson.getHealthState(scelta)
    for x in health_states:
        query = "insert into health_state (id, disease_degree, disease_type, timestamp) " \
                "values (" + str(x['id']) + ", " + str(x['disease_degree']) + ", '" + x['disease_type'] + "', " + str(x['timestamp']) + ");"
        Connection.update(query)

def inserisciInstall(scelta):
    install = getJson.getInstall(scelta)
    for x in install:
        query = "insert into install (id_patient, id_device, when, where_) " \
                "values (" + str(x['id_patients']) + ", " + str(x['id_devices']) + ", " + str(x['when']) + ", '" + x['where'] + "');"
        Connection.update(query)

def inserisciMeasurement(scelta):
    measurement = getJson.getMeasurement(scelta)
    for x in measurement:
        query = "insert into measurement (id_parameter, id_device) " \
                "values (" + str(x['id_parameters']) + ", " + str(x['id_devices']) + ");"
        Connection.update(query)

def inserisciMonitoring(scelta):
    monitoring = getJson.getMonitoring(scelta)
    for x in monitoring:
        query = "insert into monitoring (id_parameter, id_observation) " \
                "values (" + str(x['id_parameters']) + ", " + str(x['id_observations']) + ");"
        Connection.update(query)

def inserisciObservations(scelta):
    observations = getJson.getObservations(scelta)
    for x in observations:
        query = "insert into observation (id, timestamp, uom, value) " \
                "values (" + str(x['id']) + ", " + str(x['timestamp']) + ", '" + x['uom'] + "', " + str(x['value']) + " );"
        Connection.update(query)

def inserisciParameter(scelta):
    parameter = getJson.getParameters(scelta)
    for x in parameter:
        query = "insert into parameter (id, description, frequency) " \
                "values (" + str(x['id']) + ", '" + x['description'] + "', " + str(x['frequency']) + ");"
        Connection.update(query)

def inserisciPatient(scelta):
    patient = getJson.getPatients(scelta)
    for x in patient:
        query = "insert into patient (id, address, dateofbirth, email, name, surname, telepthon) " \
                "values (" + str(x['id']) + ", '" + x['address'] + "', '" + x['date_of_birth'] + "', '" + x['email'] + "', '" + x['name'] + "', '" + x['surname'] + "', '" + x['telephone'] + "' );"
        Connection.update(query)

def inserisciRelated(scelta):
    related = getJson.getRelated(scelta)
    for x in related:
        query = "insert into related (id_patient, id_health_state) " \
                "values (" + str(x['id_patients']) + ", " + str(x['id_health_states']) + ");"
        Connection.update(query)

def inserisciSet(scelta):
    set = getJson.getSet(scelta)
    for x in set:
        query = "insert into set_ (id_healt_state, id_therapy) " \
                "values (" +str(x['id_health_states']) + ", " + str(x['id_therapies']) + ");"
        Connection.update(query)

def inserisciTherapies(scelta):
    therapies = getJson.getTherapies(scelta)
    for x in therapies:
        query = "insert into therapy (id, duration, medicine, posology, starting_time) " \
                "values (" + str(x['id']) + ", " + str(x['duration']) + ", '" + x['medicine'] + "', '" + x['posology'] + "', '" + x['starting_time'] + "' );"
        Connection.update(query)

def inserisciTuttiDati(scelta):
    inserisciAffect(scelta)
    inserisciDevices(scelta)
    inserisciDoctors(scelta)
    inserisciEvaluate(scelta)
    inserisciHealth_states(scelta)
    inserisciInstall(scelta)
    inserisciMeasurement(scelta)
    inserisciMonitoring(scelta)
    inserisciObservations(scelta)
    inserisciParameter(scelta)
    inserisciPatient(scelta)
    inserisciRelated(scelta)
    inserisciSet(scelta)
    inserisciTherapies(scelta)

def funzione(scelta):

    tPrima = time.time()
    for _ in range(0,100):
        risultato = Connection.query("select * from patient;")
    print "prova"
    for x in risultato:
        print x
    tTotale = time.time() - tPrima
    print "Il tempo per fare la query 1 e': " + str(tTotale)

    tPrima = time.time()
    for _ in range(0,100):
        risultato = Connection.query("SELECT * FROM patient WHERE name = 'SIVV33W0' allow filtering;")
    tTotale = time.time() - tPrima
    print "Il tempo per fare la query 2 e': " + str(tTotale)

    tPrima = time.time()
    for _ in range(0,100):
        query3()
    tTotale = time.time() - tPrima
    print "Il tempo per fare la query 3 e': " + str(tTotale)
    """
    tPrima = time.time()
    for _ in range(0,100):
        query4()
    tTotale = time.time() - tPrima
    print "Il tempo per fare la query 4 e': " + str(tTotale)
    """
def query3():

    query = "select * from health_state where timestamp > 400073 allow filtering;"
    risultato = Connection.query(query)
    for x in risultato:
        query1 = "select id_patient from related where id_health_state = "+ str(x.id) +" allow filtering;"
        risultato2 = Connection.query(query1)
        for y in risultato2:
            query2 = "select * from patient where id = "+ y.id_patient +"allow filtering;"
            risultato3 = Connection.query(query2)


def query4():
    query = "select distinct id_patient from install where when > 5000 allow filtering;"
    risultato = Connection.query(query)
    for x in risultato:
        query1 = "select id_health_state from related where id_patient = " + str(x.id_patient) + " allow filtering;"
        risultato2 = Connection.query(query1)
        for y in risultato2:
            query2 = "select id_therapy from set_ where id_healt_state = "+ str(y.id_health_state) +" allow filtering;"
            risultato3 = Connection.query(query2)
            for z in risultato3:
                query3 = "select * from therapy where id = "+ str(z.id_therapy) + " allow filtering;"
                risultato4 = Connection.query(query3)



scelta = 0
while (scelta < 4):
    print scelta


    print "elimino elementi dal DB"
    eliminaTuttiDati()
    print "inserisco gli elementi dal DB"
    inserisciTuttiDati(scelta)
    print "inizio le query"

    funzione(scelta )

    scelta = scelta + 1