from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
import sys
import json

def make_connection(username, password):
    return GraphDatabase("http://localhost:7474", username=username, password=password)

class master: 
    def define_label(self, l):
        self.labels[l] = self.db.labels.create(l)

    def __init__(self, db):
        self.db = db
        self.labels = {}

        self.define_label("patient")
        self.define_label("device")
        self.define_label("parameter")
        self.define_label("observation")
        self.define_label("doctor")
        self.define_label("therapy")
        self.define_label("health_state")

    def delete_everything(self):
        q = '''
        MATCH (n) DETACH
        DELETE n
        '''

        self.db.query(q)

    def mk_node_from_dict(self, label, property_dict):
        n = self.db.nodes.create(**property_dict)
        self.labels[label].add(n)
        return n

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

    def relate(self, l0, l1, id0, id1, name, args={}):
        n0 = self.labels[l0].get(id=id0)[0]
        n1 = self.labels[l1].get(id=id1)[0]
        n0.relationships.create(name, n1, **args)
        return 0

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

m = master(make_connection("neo4j", "admin"))
m.delete_everything()

dataset_path = sys.argv[1]
print('Reading dataset from "{0}"'.format(dataset_path))

dataset_file = open(dataset_path, "r")
dataset_contents = dataset_file.read()
dataset_json = json.loads(dataset_contents)

ds_patients = dataset_json["patients"]
ds_devices = dataset_json["devices"]
ds_observations = dataset_json["observations"]
ds_parameters = dataset_json["parameters"]
ds_doctors = dataset_json["doctors"]
ds_health_states = dataset_json["health_states"]
ds_therapies = dataset_json["therapies"]

for x in ds_patients:
    m.mk_patient(x["id"], x["name"], x["surname"], x["date_of_birth"], x["address"], x["telephone"], x["email"])

for x in ds_devices:
    m.mk_device(x["id"], x["manufacturer"], x["model"])

for x in ds_observations:
    m.mk_observation(x["id"], x["timestamp"], x["value"], x["uom"])

for x in ds_parameters:
    m.mk_parameter(x["id"], x["description"], x["frequency"])

for x in ds_doctors:
    m.mk_doctor(x["id"], x["name"], x["surname"])

for x in ds_health_states:
    m.mk_health_state(x["id"], x["timestamp"], x["disease_type"], x["disease_degree"])

for x in ds_therapies:
    m.mk_therapy(x["id"], x["starting_time"], x["duration"], x["medicine"], x["posology"])

dataset_r_install = dataset_json["install"]
dataset_r_measurement = dataset_json["measurement"]
dataset_r_affect = dataset_json["affect"]
dataset_r_evaluate  = dataset_json["evaluate"]
dataset_r_set  = dataset_json["set"]
dataset_r_monitoring  = dataset_json["monitoring"]
dataset_r_related = dataset_json["related"]

for x in dataset_r_install: 
    m.mk_r_install(x["id_patients"], x["id_devices"], x["when"], x["where"]);

for x in dataset_r_measurement: 
    m.mk_r_measurement(x["id_devices"], x["id_parameters"]);

for x in dataset_r_monitoring: 
    m.mk_r_monitoring(x["id_parameters"], x["id_observations"]);

for x in dataset_r_affect: 
    m.mk_r_affect(x["id_observations"], x["id_health_states"]);

for x in dataset_r_related: 
    m.mk_r_related(x["id_patients"], x["id_health_states"]);

for x in dataset_r_evaluate: 
    m.mk_r_evaluate(x["id_health_states"], x["id_doctors"]);

for x in dataset_r_set: 
    m.mk_r_set(x["id_therapies"], x["id_health_states"]);


# m.mk_r_measurement(2, 2)

# m.mk_patient("x_name", "x_surname", "x_dob", "x_addr", "x_tel", "x_email")
# m.mk_device("x_man", "x_mod")

##class entity_model:
##    def __init__(self, label, property_map):
##        self.label = label
##        self.property_map = property_map
##
##    def print(self):
##        print('model::print()\n\tlabel: "{0}"\n\tproperty_map: "{1}"'.format(self.label, self.property_map))
##
##    def mk_create_query(self):
##        property_map_cql = '{';
##
##        for k, v in self.property_map.items():
##            property_map_cql += '{0}: "{1}", '.format(k, v)
##
##        # Remove last comma
##        property_map_cql = property_map_cql[:-2]
##
##        property_map_cql += '}'
##
##        return 'CREATE ({0}:{1} {2})'.format("n", self.label, property_map_cql)
##
##def make_patient_model(name, surname, date_of_birth, address, telephone, email):
##    return entity_model("Patient", {
##        "name": name,
##        "surname": surname,
##        "date_of_birth": date_of_birth,
##        "address": address,
##        "telephone": telephone,
##        "email": email
##    })
