from pymongo import *
from query import *

client = MongoClient("localhost", 27017)
db = client.test

queryInserisciSalute(db)
queryPrendiSalute(db)

print "\nfine programma"



