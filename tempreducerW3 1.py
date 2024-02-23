#!/usr/bin/python

import sys

current_year = None
total_temperature = 0
count = 0
min_temperature = float('inf')  # Initialize to positive infinity
max_temperature = float('-inf')  # Initialize to negative infinity

print("Year	Avg	Min	Max")
for line in sys.stdin:

    year, temperature = line.strip().split('\t')
    temperature = int(temperature)


    if current_year == year:

        total_temperature += temperature
        count += 1
        min_temperature = min(min_temperature, temperature)
        max_temperature = max(max_temperature, temperature)
    else:

        if current_year:

            average_temperature = total_temperature / count

            print(f'{current_year}\t{average_temperature}\t{min_temperature}\t{max_temperature}')


        current_year = year
        total_temperature = temperature
        count = 1
        min_temperature = temperature
        max_temperature = temperature


if current_year:
    average_temperature = total_temperature / count
    print(f'{current_year}\t{average_temperature}\t{min_temperature}\t{max_temperature}')

