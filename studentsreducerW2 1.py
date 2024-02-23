#!/usr/bin/python
import sys

current_name = None
current_records = []

for line in sys.stdin:
    line = line.strip()
    name, registration, marks = line.split(',')

    if current_name == name:
        current_records.append((registration, int(marks)))
    else:
        if current_name:
            sorted_records = sorted(current_records, key=lambda x: x[0])
            for reg, mark in sorted_records:
                print(f'{current_name},{reg},{mark}')
        current_name = name
        current_records = [(registration, int(marks))]

if current_name:
    sorted_records = sorted(current_records, key=lambda x: x[0])
    for reg, mark in sorted_records:
        print(f'{current_name},{reg},{mark}')



