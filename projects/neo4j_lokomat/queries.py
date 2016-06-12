#!/bin/python3

# Import neo4j libraries
import neo4jrestclient
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
import matplotlib.pyplot as plt

# Import timer utilities
import time

# Import `sys` for command line argument parsing
import sys

# Given `username` and `password`, returns a connection to the neo4j db
def make_connection(username, password):
    return GraphDatabase("http://localhost:7474", username=username, password=password)

t0 = []
def start_timer():
    global t0
    t0.append(time.perf_counter())

def end_timer():
    global t0
    print("Time: {:.2f}s\n".format(time.perf_counter() - t0.pop()))


# Class containing an open neo4j connection and functions to manage the data
class master:
    # Constructor
    # Given an open connection, stores the connection in `master`
    # Defines labels for every entity
    def __init__(self, db):
        self.db = db

    def exec_query(self, q):
        self.db.query(q)

def bench_query(q):
    start_timer()
    for _ in range(0, 100):
        m.exec_query(q)
    end_timer()

# Main function
if __name__ == "__main__":

    # Create a `master` and clear the database
    print('Initializing `master`')
    m = master(make_connection("neo4j", "admin"))
    print('`master` initialized')

    print('Query 0: select all patients')
    bench_query('\
        MATCH (n:patient) \
        RETURN n')

    print('Query 1: select all patients by name')
    bench_query('\
        MATCH (n:patient) \
        WHERE n.name = "SIVV33W0" \
        RETURN n')

    print('Query 2: select all patients with at least 5 measurements filtering by `training_duration < x` and `width != y`')
    bench_query('\
        MATCH (p:patient)-[r:measure]->(m:measurement) \
        WITH p, m, count(m) as relcount \
        WHERE p.lwalk_training_duration < 5000 AND p.width <> 5000 AND relcount > 4 \
        RETURN p')
