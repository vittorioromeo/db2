#!/bin/bash

# Create `results` folder if required
mkdir -p results

# Dataset N array
# VALUES=(10 100 1000 10000 100000)
VALUES=(1000 10000)

# Load dataset chunk N array
CHUNKS=(1 1 1 5 10)

# Next chunk value index
ICHUNK=0

for i in "${VALUES[@]}"
do
    echo "Loading and benchmarking ${i}"

    # Dataset path
    DS="../../dataset_lokomat/output/ds${i}.json"

    # Output graph path
    OF="./results/r${i}.txt"

    # Load dataset
    python3 -O ./load_dataset.py "${DS}" "${CHUNKS[$ICHUNK]}"

    # Increment index for next chunk
    ((ICHUNK++))

    # Run queries and create plot data
    python3 -O ./queries.py > "${OF}"
done

# Create plots
python3 -O ./make_plots.py

echo "Done"