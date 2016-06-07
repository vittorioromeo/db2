#!/bin/python3

# Import neo4j libraries
import neo4jrestclient
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

# Import timer utilities
import time

# Import `sys` for command line argument parsing
import sys

# Import `json` to read the generated dataset
import json

# Given `username` and `password`, returns a connection to the neo4j db
def make_connection(username, password):
    return GraphDatabase("http://localhost:7474", username=username, password=password)

def make_patient_dict(p):
    x = {
        "id": p["id"],
        "name": p["name"],
        "width": p["width"],
        "height": p["height"],
        "l_shank": p["l_shank"],
        "l_thigh": p["l_thigh"],
        "lokomat_shank": p["lokomat_shank"],
        "lokomat_thigh": p["lokomat_thigh"],
        "lokomat_recorded": p["lokomat_recorded"],
        "version": p["version"],
        "legtype": p["legtype"],
        "lwalk_training_duration": p["lwalk_training_duration"],
        "lwalk_distance": p["lwalk_distance"]
    }

    ds = ', '.join("{0}: {1}".format(k, v if isinstance(v, int)  or isinstance(v, float) else '"' + v + '"') \
            for (k, v) in x.items())

    return ds

def make_measurement_dict(m):
    x = {
        "p00": m[0],
        "p01": m[1],
        "p02": m[2],
        "p03": m[3],
        "p04": m[4],
        "p05": m[5],
        "p06": m[6],
        "p07": m[7],
        "p08": m[8],
        "p09": m[9],
        "p10": m[10],
        "p11": m[11],
        "p12": m[12],
        "p13": m[13],
        "p14": m[14],
        "p15": m[15],
        "p16": m[16],
        "p17": m[17],
        "p18": m[18],
        "p19": m[19],
        "p20": m[20],
        "p21": m[21],
        "p22": m[22],
        "p23": m[23],
        "p24": m[24],
        "p25": m[25],
        "p26": m[26],
        "p27": m[27],
        "p28": m[28],
        "p29": m[29],
        "p30": m[30],
        "p31": m[31]
    }

    ds = ', '.join("{0}: {1}".format(k, v if isinstance(v, int) or isinstance(v, float) else "null") \
            for (k, v) in x.items())

    return ds

# Class containing an open neo4j connection and functions to manage the data
class master:
    # Defines a label `l` and stores it in the labels list
    def define_label(self, l):
        self.labels[l] = self.db.labels.create(l)

    # Constructor
    # Given an open connection, stores the connection in `master`
    # Defines labels for every entity
    def __init__(self, db):
        self.db = db
        self.labels = {}
        self.queries = []

    # Completely clears the database
    def delete_everything(self):
        q = '''MATCH (n) DETACH
        DELETE n'''

        self.db.query(q)

        self.define_label("patient")
        self.define_label("measurement")

        tx = self.db.transaction(for_query=True)
        tx.append("CREATE INDEX ON :patient(id)")
        tx.execute()
        tx.commit()

        self.currtx = self.db.transaction(for_query=True)

    def execute_generated_queries(self):

        start_timer()
        print('Executing...')
        self.currtx .execute()
        end_timer()

        start_timer()
        print('Committing...')
        self.currtx.commit()
        end_timer()

        self.currtx = self.db.transaction(for_query=True)

    def q(self, x):
        self.currtx.append(q)

t0 = []
def start_timer():
    global t0
    t0.append(time.perf_counter())

def end_timer():
    global t0
    print("Time: {:.2f}s\n".format(time.perf_counter() - t0.pop()), file=sys.stderr)

# Main function
if __name__ == "__main__":

    start_timer()

    # Create a `master` and clear the database
    print('Initializing `master`')
    m = master(make_connection("neo4j", "admin"))
    m.delete_everything()
    print('`master` initialized')

    def bench_execute_generated_queries():
        start_timer()
        print('Executing queries...')
        m.execute_generated_queries()
        end_timer()

    def bench_execute_fill_ds(msg, collection, f):
        start_timer()
        print("Filling: " + msg)
        for x in collection:
            f()
        end_timer()

        bench_execute_generated_queries()

    # Read dataset path from command line arguments
    dataset_path = sys.argv[1]
    print('Reading dataset from "{0}"'.format(dataset_path))

    # Read the dataset file as json
    start_timer()
    print('Reading json dataset file')
    dataset_file = open(dataset_path, "r")
    dataset_contents = dataset_file.read()
    dataset_json = json.loads(dataset_contents)
    ds_patients = dataset_json
    print('Dataset file loaded')
    end_timer()

    chunk_size = 100

    for i in range(0, len(ds_patients), chunk_size):
        for p in ds_patients[i:i + chunk_size]:
            q = "CREATE (n:patient {{{0}}})\n".format(make_patient_dict(p))

            for s in p["step_datas"]:
                q += "CREATE (n)-[:measure]->(:measurement {{{0}}})\n".format(make_measurement_dict(s))

            m.q(q)

        start_timer()
        print('Executing queries...')
        m.execute_generated_queries()
        end_timer()


    end_timer()