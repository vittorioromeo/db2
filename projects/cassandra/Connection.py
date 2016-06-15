from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('db2')


def update(query):
    session.execute(query)


def query(query):
    return session.execute(query)