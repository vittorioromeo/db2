# neo4j tests

## Usage

### `load_dataset.py` script

This `python3` script clears any existing data in the `neo4j` instance and loads a new dataset.

It takes one command line argument: the path of the dataset to load.

Example:

```
python3 -O ./load_dataset.py "../../dataset/output/ds1000.json"
```

### `queries.py` script

This `python3` script executes the queries specified in `query.md` in the current `neo4j` instance and measures the time spent on them.

It takes no command line parameters and assumes a valid dataset is loaded in the current `neo4j` instance.

Example:

```
python3 -O ./queries.py 
```

### `run_benchmarks.sh` script

This `bash` script does the following, for `i = [10, 100, 1000, 10000, 100000]`:

1. Call `load_dataset.py` with the dataset of size `i`.

2. Call `queries.py` and pipes its output in `./results/r{i}.txt`.


Code for `i`:

```bash
echo "Loading and benchmarking ${i}"
DS="../../dataset/output/ds{i}.json"
OF="./results/r{i}.txt"
python3 -O ./load_dataset.py "${DS}"
echo "OUTPUT (${DS}):" > "${OF}"
python3 -O ./queries.py >> "${OF}"
printf "\n\n\n" >> "${OF}"
```
