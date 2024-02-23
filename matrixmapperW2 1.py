#!/usr/bin/python3
import sys
for line in sys.stdin:
	line = line.strip()
	key,words = line.split(',',1)
	print("%s\t%s"%(key,words))
