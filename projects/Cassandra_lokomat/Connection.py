from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('db2_project')


def update(query):
    session.execute(query)

def query(query):
    return session.execute(query)


def query1():
    risultato = query("select * from patient;")
    return risultato

def query2():
    risultato = query("SELECT * FROM patient WHERE name = 'KRVYRSKX7' allow filtering;")
    return risultato

def query3():
    x = []
    risultato = query("select * from patient where lwalk_training_duration < 2400 allow filtering;")
    for a in risultato:
        if (a[11] != None):
            if ((a[13] != 0.80) and (len(a[11]) > 4)):
                x.append(a)
    return risultato