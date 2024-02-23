#!/usr/bin/python
import sys

current_unit = None
total_salary = 0
count = 0

# Iterate over input lines from the mapper
for line in sys.stdin:
    line = line.strip()

    # Split the input line into unit and salary
    unit, salary = line.split('\t')
    salary = int(salary)

    # Check if the unit is the same as the current unit
    if current_unit == unit:
        total_salary += salary
        count += 1
    else:
        # Output result for the previous unit (if any)
        if current_unit:
            average_salary = total_salary / count
            print(f'{current_unit}\t{average_salary}')
        
        current_unit = unit
        total_salary = salary
        count = 1

# Output result for the last unit
if current_unit:
    average_salary = total_salary / count
    print(f'{current_unit}\t{average_salary}')

