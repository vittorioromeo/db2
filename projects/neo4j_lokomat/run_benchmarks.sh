#!/bin/bash

mkdir results

echo "Loading and benchmarking 10"
DS="../../dataset/output/ds10.json"
OF="./results/r10.txt"
python3 -O ./load_dataset.py "${DS}"
echo "OUTPUT (${DS}):" > "${OF}"
python3 -O ./queries.py >> "${OF}"
printf "\n\n\n" >> "${OF}"

echo "Loading and benchmarking 100"
DS="../../dataset/output/ds100.json"
OF="./results/r100.txt"
python3 -O ./load_dataset.py "${DS}"
echo "OUTPUT (${DS}):" > "${OF}"
python3 -O ./queries.py >> "${OF}"
printf "\n\n\n" >> "${OF}"

echo "Loading and benchmarking 1000"
DS="../../dataset/output/ds1000.json"
OF="./results/r1000.txt"
python3 -O ./load_dataset.py "${DS}"
echo "OUTPUT (${DS}):" > "${OF}"
python3 -O ./queries.py >> "${OF}"
printf "\n\n\n" >> "${OF}"

echo "Loading and benchmarking 10000"
DS="../../dataset/output/ds10000.json"
OF="./results/r10000.txt"
python3 -O ./load_dataset.py "${DS}"
echo "OUTPUT (${DS}):" > "${OF}"
python3 -O ./queries.py >> "${OF}"
printf "\n\n\n" >> "${OF}"

echo "Loading and benchmarking 100000"
DS="../../dataset/output/ds100000.json"
OF="./results/r100000.txt"
python3 -O ./load_dataset.py "${DS}"
echo "OUTPUT (${DS}):" > "${OF}"
python3 -O ./queries.py >> "${OF}"
printf "\n\n\n" >> "${OF}"

echo "Done"