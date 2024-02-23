#!/usr/bin/python
import sys

# Initialize lists to store employee information
emp_numbers = []
emp_names = []
units = []
designations = []
salaries = []

# Read input lines and extract employee information
for line in sys.stdin:
    line = line.strip()
    if line.startswith("EmpNo"):
        emp_numbers = [int(x) for x in next(sys.stdin).strip().split()]
    elif line.startswith("EmpName"):
        emp_names = next(sys.stdin).strip().split()
    elif line.startswith("Unit"):
        units = next(sys.stdin).strip().split()
    elif line.startswith("Designation"):
        designations = next(sys.stdin).strip().split()
    elif line.startswith("Salary"):
        salaries = [int(x) for x in next(sys.stdin).strip().split()]

# Emit unit-wise salary key-value pairs
for i in range(len(emp_numbers)):
    print(f'{units[i]}\t{salaries[i]}')

