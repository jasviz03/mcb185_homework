"""
Report the lengths of protein-coding genes in the E.coli genome. The program will need 
to perform the following tasks as it reads each line of the file. 

1. Skip over comment lines. 
2. Find CDS features
3. Extract the beginning and end coordinates
4. Convert the coordinates to integers
5. Report the length of the CDS (end- begin +1)
"""
import gzip
import sys

filename = sys.argv[1]

with gzip.open(filename , 'rt') as fp: 
	for line in fp: 
		if line[0] != '#':
			words = line.split()
			if words[2] == 'CDS': 
				beg = int(words[3])
				end = int(words[4])
				print(end - beg + 1)
				
				
				
				


