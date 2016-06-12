#!/bin/python3

# Import neo4j libraries
import neo4jrestclient
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

# Import timer utilities
import time

# Import `sys` for command line argument parsing
import sys
import io

# Import `json` to read the generated dataset
import json

class StringBuilder(object):
    def __init__(self):
        self._stringio = io.StringIO()

    def __str__(self):
        return self._stringio.getvalue()

    def append(self, *objects, sep=' ', end=''):
        print(*objects, sep=sep, end=end, file=self._stringio)

# Given `username` and `password`, returns a connection to the neo4j db
def make_connection(username, password):
    return GraphDatabase("http://localhost:7474", username=username, password=password)

# TODO: hardcode for speed
def make_patient_dict(p):
    x = {
        "id": p["id"],
        "name": p["name"],
        "weight": p["width"],
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

def md(x):
    if x == None:
        return "null"
    else:
        return x

# TODO: hardcode for speed
def make_measurement_dict(m):
    r = StringBuilder()

    r.append('bw_support:')
    r.append(md(m[0]))
    r.append(', ')
    
    r.append('p_coeff:')
    r.append(md(m[1]))
    r.append(', ')

    r.append('rom_hl:')
    r.append(md(m[2]))
    r.append(', ')

    r.append('rom_kl:')
    r.append(md(m[3]))
    r.append(', ')

    r.append('rom_hr:')
    r.append(md(m[4]))
    r.append(', ')

    r.append('rom_kr:')
    r.append(md(m[5]))
    r.append(', ')

    r.append('offset_rom_hl:')
    r.append(md(m[6]))
    r.append(', ')

    r.append('offset_rom_kl:')
    r.append(md(m[7]))
    r.append(', ')

    r.append('offset_rom_hr:')
    r.append(md(m[8]))
    r.append(', ')

    r.append('offset_rom_kr:')
    r.append(md(m[9]))
    r.append(', ')

    r.append('guidance_l:')
    r.append(md(m[10]))
    r.append(', ')

    r.append('guidance_r:')
    r.append(md(m[11]))
    r.append(', ')

    r.append('speed:')
    r.append(md(m[12]))
    r.append(', ')

    r.append('energy_hip_l:')
    r.append(md(m[13]))
    r.append(', ')

    r.append('energy_knee_l:')
    r.append(md(m[14]))
    r.append(', ')

    r.append('energy_hip_r:')
    r.append(md(m[15]))
    r.append(', ')

    r.append('energy_knee_r:')
    r.append(md(m[16]))
    r.append(', ')

    r.append('step:')
    r.append(md(m[17]))
    r.append(', ')

    r.append('bio_hl_st:')
    r.append(md(m[18]))
    r.append(', ')

    r.append('bio_hl_sw:')
    r.append(md(m[19]))
    r.append(', ')

    r.append('bio_kl_st:')
    r.append(md(m[20]))
    r.append(', ')

    r.append('bio_kl_sw:')
    r.append(md(m[21]))
    r.append(', ')

    r.append('bio_hr_st:')
    r.append(md(m[22]))
    r.append(', ')

    r.append('bio_hr_sw:')
    r.append(md(m[23]))
    r.append(', ')

    r.append('bio_kr_st:')
    r.append(md(m[24]))
    r.append(', ')

    r.append('bio_kr_sw:')
    r.append(md(m[25]))
    r.append(', ')

    r.append('pos_dev_hl:')
    r.append(md(m[26]))
    r.append(', ')

    r.append('pos_dev_hr:')
    r.append(md(m[27]))
    r.append(', ')

    r.append('light_c_l:')
    r.append(md(m[28]))
    r.append(', ')

    r.append('light_c_r:')
    r.append(md(m[29]))
    r.append(', ')

    r.append('unloading_l:')
    r.append(md(m[30]))
    r.append(', ')

    r.append('unloading_r:')
    r.append(md(m[31]))

    return str(r)

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

    def do_query(self, x):
        tx = self.db.transaction(for_query=True)
        tx.append(x)
        tx.execute()
        tx.commit()

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
    chunk_size = int(sys.argv[2])
    print('Reading dataset from "{0}"'.format(dataset_path))

    # Read the dataset file as json
    print('Reading json dataset file')
    dataset_file = open(dataset_path, "r")
    dataset_contents = dataset_file.read()
    ds_patients = json.loads(dataset_contents)
    print('Dataset file loaded')

    idx = 0

    print('Executing queries...')
    for i in range(0, len(ds_patients), chunk_size):
        q = StringBuilder()

        for p in ds_patients[i:i + chunk_size]:
            q.append("CREATE (n"+str(idx)+":patient {")
            q.append(make_patient_dict(p))
            q.append("})\n")

            for s in p["step_datas"]:
                q.append("CREATE (n"+str(idx)+")-[:measure]->(:measurement {")
                q.append(make_measurement_dict(s))
                q.append("})\n")

            idx += 1

        m.do_query(str(q))
        sys.stdout.write('\r{0}/{1}'.format(i, len(ds_patients)))
        sys.stdout.flush()

    print("")
    end_timer()