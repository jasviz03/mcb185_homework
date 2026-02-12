"""
Scoring system for aligning nucleotide sequences is often described 
with 2 values: match and mismatch. For example, +1 for a match
and a -1 for a mismatch. Printed out in the matrix, that would look like this: 

   A  C  G  T
A +1 -1 -1 -1
C -1 +1 -1 -1
G -1 -1 +1 -1
T -1 -1 -1 -1

Write a program that can print out a mismatch-match scoring matrix. 
The alphabet, match, and mismatch are all command line parameters. 
For example, the command line for generating a new matrix above would
look like this: 

python3 25scoringmatrix.py ACGT +1 -1
"""

import sys

alphabet = sys.argv[1]
match = int(sys.argv[2])
mismatch = int(sys.argv[3])

print(' ', end ='')
for letter in alphabet : 
	print(f'{letter:>3}', end = '')
print()

for row in alphabet: 
	print(row, end = '')
	for col in alphabet: 
		if row == col: 
			print(f'{match:>3}', end = '')
		else: 
			print(f'{mismatch:>3}', end = '')
	print()








