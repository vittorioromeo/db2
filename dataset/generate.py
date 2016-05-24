import json
import random
import string

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

def rndi_x(min, max):
    return random.randint(min, max - 1)

def rnds_x(min, max):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(rndi_x(min, max)))

def rnds():
    return rnds_x(4, 10)

def xid(f):
    res = f.next_id
    f.next_id += 1
    return res

def rnd_timestamp():
    return rndi_x(0, 1000000)

@static_vars(next_id=0)
def rnd_patient():
    return {
        "id": xid(rnd_patient),
        "name": rnds(),
        "surname": rnds(),
        "address": rnds(),
        "date_of_birth": rnds(),
        "telephone": rnds(),
        "email": rnds()
    }

@static_vars(next_id=0)
def rnd_device():
    return {
        "id": xid(rnd_device),
        "manufacturer": rnds(),
        "model": rnds()
    }

@static_vars(next_id=0)
def rnd_parameter():
    return {
        "id": xid(rnd_parameter),
        "description": rnds(),
        "frequency": rnds()
    }

@static_vars(next_id=0)
def rnd_observation():
    return {
        "id": xid(rnd_observation),
        "timestamp": rnd_timestamp(),
        "value": rnds(),
        "uom": rnds()
    }

@static_vars(next_id=0)
def rnd_therapy():
    return {
        "id": xid(rnd_therapy),
        "starting_time": rnds(),
        "duration": rndi_x(60, 240),
        "medicine": rnds(),
        "posology": rnds()
    }

@static_vars(next_id=0)
def rnd_health_state():
    return {
        "id": xid(rnd_health_state),
        "timestamp": rnd_timestamp(),
        "duration": rndi_x(60, 240),
        "disease_type": rnds(),
        "disease_degree": rnds()
    }

@static_vars(next_id=0)
def rnd_doctor():
    return {
        "id": xid(rnd_doctor),
        "name": rnds(),
        "surname": rnds()
    }

@static_vars(next_id=0)
def rnd_rel_install():
    return {
        "id": xid(rnd_rel_install),
        "when": rnds(),
        "where": rnds()
    }

@static_vars(next_id=0)
def rnd_rel_measurement():
    return {
        "id": xid(rnd_rel_measurement)
    }

@static_vars(next_id=0)
def rnd_rel_monitoring():
    return {
        "id": xid(rnd_rel_monitoring)
    }

@static_vars(next_id=0)
def rnd_rel_affect():
    return {
        "id": xid(rnd_rel_affect)
    }

@static_vars(next_id=0)
def rnd_rel_related():
    return {
        "id": xid(rnd_rel_related)
    }

@static_vars(next_id=0)
def rnd_rel_set():
    return {
        "id": xid(rnd_rel_set)
    }

@static_vars(next_id=0)
def rnd_rel_evaluate():
    return {
        "id": xid(rnd_rel_evaluate)
    }


def pretty_print(x):
    print(json.dumps(x, sort_keys=True, indent=4))

def mk_rnd_collection(f, n):
    result = []
    
    for _ in range(0, n):
        result.append(f())

    return result

def mk_entity_table(f, name):
    return {name: mk_rnd_collection(f, 10)}

def key_of_tbl(t):
    for k, _ in t.items():
        return k

def mk_nn_relation(f, t0, t1, prob, name):
    result = []

    t0_key = key_of_tbl(t0)
    t1_key = key_of_tbl(t1)
    
    for v_t0 in t0[t0_key]:
        for v_t1 in t1[t1_key]:
            if(random.random() <= prob):
                rel_data = f()
                rel_data["id_" + t0_key] = v_t0["id"]
                rel_data["id_" + t1_key] = v_t1["id"]

                result.append(rel_data)

    return {name: result}

def mk_1n_relation(f, t1, tn, prob, name):
    result = []

    t1_key = key_of_tbl(t1)
    tn_key = key_of_tbl(tn)
    
    # Iterate over (1,1) table
    for v_t1 in t1[t1_key]:
        
        # Select random entity from (1,N) table
        v_tn = random.choice(tn[tn_key])

        if(random.random() <= prob):
            rel_data = f()
            rel_data["id_" + t1_key] = v_t1["id"]
            rel_data["id_" + tn_key] = v_tn["id"]

            result.append(rel_data)

    return {name: result}

# Generate entity tables
patients = mk_entity_table(rnd_patient, "patients")
devices = mk_entity_table(rnd_device, "devices")
parameters = mk_entity_table(rnd_parameter, "parameters")
observations = mk_entity_table(rnd_observation, "observations")
therapies = mk_entity_table(rnd_therapy, "therapies")
health_states = mk_entity_table(rnd_health_state, "health_states")
doctors = mk_entity_table(rnd_doctor, "doctors")

# Generate relations
r_nn_install = mk_nn_relation(rnd_rel_install, patients, devices, 0.75, "install")
r_nn_measurement = mk_nn_relation(rnd_rel_measurement, devices, parameters, 0.50, "measurement")
r_nn_affect = mk_nn_relation(rnd_rel_affect, observations, health_states, 0.50, "affect")
r_nn_evaluate  = mk_nn_relation(rnd_rel_evaluate, health_states, doctors, 0.50, "evaluate")
r_nn_set  = mk_nn_relation(rnd_rel_evaluate, therapies, health_states, 0.50, "set")
r_1n_monitoring  = mk_1n_relation(rnd_rel_monitoring, observations, parameters, 0.50, "monitoring")
r_1n_related = mk_1n_relation(rnd_rel_related, health_states, patients, 1.00, "related")

def merge_dicts(*args):
    result = dict()
    for a in args:
        result = {**result, **a}

    return result

result = merge_dicts(patients, devices, parameters, observations, therapies, health_states, doctors, r_nn_install, r_nn_measurement, r_nn_affect, r_nn_evaluate, r_nn_set, r_1n_monitoring, r_1n_related)
pretty_print(result)