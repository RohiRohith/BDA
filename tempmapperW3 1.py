#!/usr/bin/python

import sys

for line in sys.stdin:
    year = line.strip()[:4]  # Extract the year from the temperature data
    temperature = int(line.strip()[4:])
    print(f'{year}\t{temperature}')

