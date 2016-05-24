from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

def make_connection(username, password):
    return GraphDatabase("http://localhost:7474", username=username, password=password)

class master: 
    def define_label(self, l):
        self.labels[l] = self.db.labels.create(l)

    def __init__(self, db):
        self.db = db
        self.labels = {}

        self.define_label("Patient")
        self.define_label("Device")
        self.define_label("Parameter")
        self.define_label("Observation")

    def mk_node_from_dict_pati ent(self, label, property_dict):
        n = self.db.nodes.create(**property_dict)
        self.labels[label].add(n)
        return n

    def mk_patient(self, name, surname, date_of_birth, address, telephone, email):
        return self.mk_node_from_dict_patient("Patient", {
            "name": name,
            "surname": surname,
            "date_of_birth": date_of_birth,
            "address": address,
            "telephone": telephone,
            "email": email
        })

    def mk_device(self, manufacturer, model):
        return self.mk_node_from_dict_patient("Device", {
            "manufacturer": manufacturer,
            "model": model
        })

    def mk_parameter(self, description, frequency):
        return self.mk_node_from_dict_patient("Parameter", {
            "description": description,
            "frequency": frequency
        })

    def mk_observation(self, timestamp, value, uom):
        return self.mk_node_from_dict_patient("Observation", {
            "timestamp": timestamp,
            "value": value,
            "uom": uom
        })

    def mk_doctor(self, name, surname):
        return self.mk_node_from_dict_patient("Doctor", {
            "name": name,
            "surname": surname
        })

m = master(make_connection("neo4j", "admin"))
m.mk_patient("x_name", "x_surname", "x_dob", "x_addr", "x_tel", "x_email")
m.mk_device("x_man", "x_mod")

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
