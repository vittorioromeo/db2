#!/bin/bash
python3 -m cProfile -o out.prof "$@" && snakeviz ./out.prof