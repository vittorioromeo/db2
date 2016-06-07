#!/bin/python3

import json
import random
import string
import sys
import time
import numpy

chars = [c for c in string.ascii_uppercase + string.digits]

t0 = []
def start_timer():
    global t0
    t0.append(time.perf_counter())

def end_timer():
    global t0
    print("Time: {:.2f}s\n".format(time.perf_counter() - t0.pop()), file=sys.stderr)

count = 0
nn_rel_count = 0

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

def rndi_x(min, max):
    return numpy.random.randint(min, max - 1)

def rnds_x(min, max):
    return ''.join(numpy.random.choice(chars, rndi_x(min, max)))

def rnds():
    return rnds_x(4, 10)

def xid(f):
    res = f.next_id
    f.next_id += 1
    return res

def rnd_timestamp():
    return rndi_x(0, 10000)

def rnd_float():
    return numpy.random.rand()

def rnd_float_or_null():
    if(rnd_float() < 0.75):
        return rnd_float()
    else:
        return None

@static_vars(next_id=0)
def rnd_stepdata():
    res = []
    for i in range(0, 32):
        res.append(rnd_float_or_null())

    return res

def rnd_stepdata_array():
    res = []
    for i in range(0, rndi_x(0, 64)):
        res.append(rnd_stepdata())

    return res

@static_vars(next_id=0)
def rnd_patient():
    return {
        "id": xid(rnd_patient),
        "name": rnds(),
        "width": rnd_float(),
        "height": rnd_float(),
        "l_shank": rnd_float(),
        "l_thigh": rnd_float(),
        "lokomat_shank": rnd_float(),
        "lokomat_thigh": rnd_float(),
        "lokomat_recorded": rnd_timestamp(),
        "version": rnds(),
        "legtype": rnds(),
        "lwalk_training_duration": rnd_timestamp(),
        "lwalk_distance": rnd_float(),
        "step_datas": rnd_stepdata_array()
    }

def pretty_print(x):
    print(json.dumps(x, indent=None))

def mk_rnd_collection(f, n):
    result = []
    
    for _ in range(0, n):
        result.append(f())

    return result

if __name__ == "__main__":

    count = int(sys.argv[1])

    start_timer()
    result = mk_rnd_collection(rnd_patient, count)
    end_timer()

    start_timer()
    pretty_print(result)
    end_timer()