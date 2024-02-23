#!/usr/bin/python3
"""reducer2.py"""
import sys
a={}
b={}
for line in sys.stdin:
	line=line.strip()
	key,value=line.split('\t')
	v=value.split(',')
	if key=='a':
		a[(int(v[0]),int(v[1]))]=int(v[2])
	elif key=='b':
		b[(int(v[0]),int(v[1]))]=int(v[2])
	  
result=0
print("On Addition:\n")

for i in range(0,3):
	for j in range(0,3):
		result=a[(i,j)]+b[(i,j)]
		print("%s,%s,%s"%(i,j,result))
print("On Subtraction:\n")
result=0
for i in range(0,3):
	for j in range(0,3):
		result=a[(i,j)]-b[(i,j)]
		print("%s,%s,%s"%(i,j,result))
result=0
print("On Multiplication:\n")
for i in range(0,3):
	for j in range(0,3):
		for k in range(0,3):
			result+=a[i,k]*b[k,j]
		print("%s,%s,%s"%(i,j,result))
		result=0
