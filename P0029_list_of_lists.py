#!/usr/bin/env python3

inputfile = open('P0029_input.txt')
data = []
for line in inputfile:
	data.append(line.strip().split())
for person in data:
	print(person)

inputfile.close()