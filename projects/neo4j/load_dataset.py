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
        self.define_label("device")
        self.define_label("parameter")
        self.define_label("observation")
        self.define_label("doctor")
        self.define_label("therapy")
        self.define_label("health_state")

        tx = self.db.transaction(for_query=True)
        tx.append("CREATE INDEX ON :patient(id)")
        tx.append("CREATE INDEX ON :device(id)")
        tx.append("CREATE INDEX ON :parameter(id)")
        tx.append("CREATE INDEX ON :observation(id)")
        tx.append("CREATE INDEX ON :doctor(id)")
        tx.append("CREATE INDEX ON :therapy(id)")
        tx.append("CREATE INDEX ON :health_state(id)")
        tx.execute()
        tx.commit()

    # Given a `label` and a dictionary `property_dict` creates a node
    # and returns the newly created node. The node is added to the `label`
    def mk_node_from_dict(self, label, property_dict):
        # Join parameters by commas, surround non-int values with double quotes
        ds = ', '.join("{0}: {1}".format(k, v if isinstance(v, int) else '"' + v + '"') \
            for (k, v) in property_dict.items())

        q = 'CREATE (:{0}{{{1}}})'.format(label, ds)
        self.queries.append(q)

    def mk_patient(self, id, name, surname, date_of_birth, address, telephone, email):
        return self.mk_node_from_dict("patient", {
            "id": id,
            "name": name,
            "surname": surname,
            "date_of_birth": date_of_birth,
            "address": address,
            "telephone": telephone,
            "email": email
        })

    def mk_device(self, id, manufacturer, model):
        return self.mk_node_from_dict("device", {
            "id": id,
            "manufacturer": manufacturer,
            "model": model
        })

    def mk_parameter(self, id, description, frequency):
        return self.mk_node_from_dict("parameter", {
            "id": id,
            "description": description,
            "frequency": frequency
        })

    def mk_observation(self, id, timestamp, value, uom):
        return self.mk_node_from_dict("observation", {
            "id": id,
            "timestamp": timestamp,
            "value": value,
            "uom": uom
        })

    def mk_doctor(self, id, name, surname):
        return self.mk_node_from_dict("doctor", {
            "id": id,
            "name": name,
            "surname": surname
        })

    def mk_therapy(self, id, starting_time, duration, medicine, posology):
        return self.mk_node_from_dict("therapy", {
            "id": id,
            "starting_time": starting_time,
            "duration": duration,
            "medicine": medicine,
            "posology": posology
        })

    def mk_health_state(self, id, timestamp, disease_type, disease_degree):
        return self.mk_node_from_dict("health_state", {
            "id": id,
            "timestamp": timestamp,
            "disease_type": disease_type,
            "disease_degree": disease_degree
        })

    # Creates a directed relationship from `id0:l0` to `id1:l1` with `name`
    # and an optional set of arguments `args`
    def relate(self, l0, l1, id0, id1, name, args={}):
        # TODO: parameters
        q = '''
        MATCH (n0:{0} {{ id:{1} }}), (n1:{2} {{ id:{3} }})
        CREATE (n0)-[:`{4}`]->(n1)
        '''.format(l0, id0, l1, id1, name)

        self.queries.append(q)

    def mk_r_install(self, id_patient, id_device, when, where):
        return self.relate("patient", "device", id_patient, id_device, "has installed", {"when":when, "where":where})

    def mk_r_measurement(self, id_device, id_parameter):
        return self.relate("device", "parameter", id_device, id_parameter, "measures")

    def mk_r_monitoring(self, id_parameter, id_observation):
        return self.relate("parameter", "observation", id_parameter, id_observation, "is observed by")

    def mk_r_affect(self, id_observation, id_health_state):
        return self.relate("observation", "health_state", id_observation, id_health_state, "affects")

    def mk_r_related(self, id_patient, id_health_state):
        return self.relate("patient", "health_state", id_patient, id_health_state, "has")

    def mk_r_evaluate(self, id_health_state, id_doctor):
        return self.relate("health_state", "doctor", id_health_state, id_doctor, "is checked by")

    def mk_r_set(self, id_therapy, id_health_state):
        return self.relate("therapy", "health_state", id_therapy, id_health_state, "manages")

    def execute_generated_queries(self):
        tx = self.db.transaction(for_query=True)

        start_timer()
        print('Appending...')
        for q in self.queries:
            tx.append(q)
        end_timer()

        start_timer()
        print('Executing...')
        tx.execute()
        end_timer()

        start_timer()
        print('Committing...')
        tx.commit()
        end_timer()

        self.queries.clear()

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
    print('Dataset file loaded')
    end_timer()

    # Get json arrays for entities
    start_timer()
    print('Getting json arrays: entities')
    ds_patients = dataset_json["patients"]
    ds_devices = dataset_json["devices"]
    ds_observations = dataset_json["observations"]
    ds_parameters = dataset_json["parameters"]
    ds_doctors = dataset_json["doctors"]
    ds_health_states = dataset_json["health_states"]
    ds_therapies = dataset_json["therapies"]
    print('Done getting json arrays: entities')
    end_timer()

    start_timer()
    print('Executing queries...')
    m.execute_generated_queries()
    end_timer()

    bench_execute_fill_ds("patients", ds_patients, \
        lambda: m.mk_patient(x["id"], x["name"], x["surname"], x["date_of_birth"], x["address"], x["telephone"], x["email"]))

    bench_execute_fill_ds("devices", ds_devices, \
        lambda: m.mk_device(x["id"], x["manufacturer"], x["model"]))

    bench_execute_fill_ds("observations", ds_observations, \
        lambda: m.mk_observation(x["id"], x["timestamp"], x["value"], x["uom"]))

    bench_execute_fill_ds("parameters", ds_parameters, \
        lambda: m.mk_parameter(x["id"], x["description"], x["frequency"]))

    bench_execute_fill_ds("doctors", ds_doctors, \
        lambda: m.mk_doctor(x["id"], x["name"], x["surname"]))

    bench_execute_fill_ds("health_states", ds_health_states, \
        lambda: m.mk_health_state(x["id"], x["timestamp"], x["disease_type"], x["disease_degree"]))
        
    bench_execute_fill_ds("therapies", ds_therapies, \
        lambda: m.mk_therapy(x["id"], x["starting_time"], x["duration"], x["medicine"], x["posology"]))

    # Get json arrays for relationships
    start_timer()
    print('Getting json arrays: entities')
    dataset_r_install = dataset_json["install"]
    dataset_r_measurement = dataset_json["measurement"]
    dataset_r_affect = dataset_json["affect"]
    dataset_r_evaluate  = dataset_json["evaluate"]
    dataset_r_set  = dataset_json["set"]
    dataset_r_monitoring  = dataset_json["monitoring"]
    dataset_r_related = dataset_json["related"]
    print('Done getting json arrays: relationships')
    end_timer()

    # Fill database with relationships
    bench_execute_fill_ds("install", dataset_r_install, \
        lambda: m.mk_r_install(x["id_patients"], x["id_devices"], x["when"], x["where"]))

    bench_execute_fill_ds("measurement", dataset_r_measurement, \
        lambda: m.mk_r_measurement(x["id_devices"], x["id_parameters"]))

    bench_execute_fill_ds("monitoring", dataset_r_monitoring, \
        lambda: m.mk_r_monitoring(x["id_parameters"], x["id_observations"]))

    bench_execute_fill_ds("affect", dataset_r_affect, \
        lambda: m.mk_r_affect(x["id_observations"], x["id_health_states"]))

    bench_execute_fill_ds("related", dataset_r_related, \
        lambda: m.mk_r_related(x["id_patients"], x["id_health_states"]))

    bench_execute_fill_ds("evaluate", dataset_r_evaluate, \
        lambda: m.mk_r_evaluate(x["id_health_states"], x["id_doctors"]))

    bench_execute_fill_ds("set", dataset_r_set, \
        lambda: m.mk_r_set(x["id_therapies"], x["id_health_states"]))

    end_timer()