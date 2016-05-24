from pymongo import *
import json
from caricaDati import *
from query import *

client = MongoClient("localhost", 27017)
db = client.test

with open('dataset.json') as data_file:
    data = json.load(data_file)

popolaTutto(data,db)

print "\nfine programma"



