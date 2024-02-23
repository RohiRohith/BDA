#!/usr/bin/python
import sys
 
for line in sys.stdin:
	line = line.strip()
	registration, name, marks = line.split(',')
	print(f'{name},{registration},{marks}')
