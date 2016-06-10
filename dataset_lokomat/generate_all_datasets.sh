#!/bin/bash

# Syntax:
# python3 ./generate.py <records per table> <record count per nn relation> <relation probability> 

echo "Creating output folder"
mkdir -p output

echo "Generating 10"
python3 -O ./generate.py 10 > ./output/ds10.json

echo "Generating 100"
python3 -O ./generate.py 100 > ./output/ds100.json

echo "Generating 1000"
python3 -O ./generate.py 1000 > ./output/ds1000.json

echo "Generating 10000"
python3 -O ./generate.py 10000 > ./output/ds10000.json

echo "Generating 100000"
python3 -O ./generate.py 100000 > ./output/ds100000.json