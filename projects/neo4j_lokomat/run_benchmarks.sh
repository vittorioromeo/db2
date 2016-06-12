#!/bin/bash

mkdir -p results

VALUES=(10 100 1000 10000 100000)
CHUNKS=(10 10 10 10 10)
ICHUNK=0

for i in "${VALUES[@]}"
do
    echo "Loading and benchmarking ${i}"
    DS="../../dataset_lokomat/output/ds${i}.json"
    OF="./results/r${i}.txt"
    python3 -O ./load_dataset.py "${DS}" "${CHUNKS[$ICHUNK]}"
    ((ICHUNK++))
    echo "OUTPUT (${DS}):" > "${OF}"
    python3 -O ./queries.py >> "${OF}"
    printf "\n\n\n" >> "${OF}"
done

echo "Done"