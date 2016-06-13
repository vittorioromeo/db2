#!/bin/python3

# Import neo4j libraries
import neo4jrestclient
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

# Import utilities
import time
import sys
import io
import json

# Helper class for efficient string concatenation
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

# Given a json `p` patient data dictionary, returns a string that can be
# used in a Cypher query
def make_patient_dict(p):
    x = {
        "id": p["id"],
        "n": p["name"],
        "w": p["width"],
        "h": p["height"],
        "l_shank": p["l_shank"],
        "l_thigh": p["l_thigh"],
        "lk_shank": p["lokomat_shank"],
        "lk_thigh": p["lokomat_thigh"],
        "lk_rec": p["lokomat_recorded"],
        "v": p["version"],
        "leg_t": p["legtype"],
        "lw_td": p["lwalk_training_duration"],
        "lw_d": p["lwalk_distance"]
    }

    ds = ', '.join("{0}: {1}".format(\
        k, v if isinstance(v, int)  or isinstance(v, float) else '"' + v + '"') \
            for (k, v) in x.items())

    return ds

# Given `x`, returns "null" if the value is `None`
def null_if_none(x):
    if x == None:
        return "null"
    else:
        return x

# Appends `key` + ":" + `m[i]`
def make_measurement_dict_par_no_comma(sb, key, m, i):
    sb.append(key)
    sb.append(':')
    sb.append(null_if_none(m[i]))

# Appends `key` + ":" + `m[i]` and a comma
def make_measurement_dict_par(sb, key, m, i):
    make_measurement_dict_par_no_comma(sb, key, m, i)
    sb.append(', ')

# Given a measurement `m`, returns a Cypher-friendly string containing
# its values
def make_measurement_dict(m):
    sb = StringBuilder()

    make_measurement_dict_par(sb, "bw_sup", m, 0)
    make_measurement_dict_par(sb, "p_coeff", m, 1)
    make_measurement_dict_par(sb, "rom_hl", m, 2)
    make_measurement_dict_par(sb, "rom_kl", m, 3)
    make_measurement_dict_par(sb, "rom_hr", m, 4)
    make_measurement_dict_par(sb, "rom_kr", m, 5)
    make_measurement_dict_par(sb, "or_hl", m, 6)
    make_measurement_dict_par(sb, "or_kl", m, 7)
    make_measurement_dict_par(sb, "or_hr", m, 8)
    make_measurement_dict_par(sb, "or_kr", m, 9)
    make_measurement_dict_par(sb, "gd_l", m, 10)
    make_measurement_dict_par(sb, "gd_r", m, 11)
    make_measurement_dict_par(sb, "speed", m, 12)
    make_measurement_dict_par(sb, "ey_hip_l", m, 13)
    make_measurement_dict_par(sb, "ey_knee_l", m, 14)
    make_measurement_dict_par(sb, "ey_hip_r", m, 15)
    make_measurement_dict_par(sb, "ey_knee_r", m, 16)
    make_measurement_dict_par(sb, "step", m, 17)
    make_measurement_dict_par(sb, "bio_hl_st", m, 18)
    make_measurement_dict_par(sb, "bio_hl_sw", m, 19)
    make_measurement_dict_par(sb, "bio_kl_st", m, 20)
    make_measurement_dict_par(sb, "bio_kl_sw", m, 21)
    make_measurement_dict_par(sb, "bio_hr_st", m, 22)
    make_measurement_dict_par(sb, "bio_hr_sw", m, 23)
    make_measurement_dict_par(sb, "bio_kr_st", m, 24)
    make_measurement_dict_par(sb, "bio_kr_sw", m, 25)
    make_measurement_dict_par(sb, "pos_dev_hl", m, 26)
    make_measurement_dict_par(sb, "pos_dev_hr", m, 27)
    make_measurement_dict_par(sb, "light_c_l", m, 28)
    make_measurement_dict_par(sb, "light_c_r", m, 29)
    make_measurement_dict_par(sb, "ul_l", m, 30)
    make_measurement_dict_par_no_comma(sb, "ul_r", m, 31)

    return str(sb)

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

    # Completely clears the database
    def delete_everything(self):
        q = 'MATCH (n) DETACH DELETE n'

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

# Benchmark utilities
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

    # Read dataset path from command line arguments
    dataset_path = sys.argv[1]

    # Read how many queries to batch per transaction
    chunk_size = int(sys.argv[2])

    # Read the dataset file as json
    print('Reading dataset from "{0}"'.format(dataset_path))    
    dataset_file = open(dataset_path, "r")
    dataset_contents = dataset_file.read()
    ds_patients = json.loads(dataset_contents)
    print('Dataset file loaded')

    # Index used to generate unique node names
    idx = 0

    print('Executing queries...')
    for i in range(0, len(ds_patients), chunk_size):
        q = StringBuilder()

        # Iterate patients in chunks
        for p in ds_patients[i:i + chunk_size]:

            # Stringify `idx`
            sidx = str(idx)

            # Generate patient node creation query
            q.append("CREATE (n")
            q.append(sidx)
            q.append(":patient {")
            q.append(make_patient_dict(p))
            q.append("})\n")

            # Generate measurement queries, which build relationships
            for s in p["step_datas"]:
                q.append("CREATE (n")
                q.append(sidx)
                q.append(")-[:measure]->(:measurement {")
                q.append(make_measurement_dict(s))
                q.append("})\n")

            # Increment next unique node id
            idx += 1

        m.do_query(str(q))
        sys.stdout.write('\r{0}/{1}'.format(i, len(ds_patients) - 1))
        sys.stdout.flush()

    print("")
    end_timer()