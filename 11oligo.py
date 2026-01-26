"""
Write a function that returns the oligo melting temp 
given the number of As, Cs, Gs, and Ts in the 
oligo . Use these two methods: 

For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4

For longer oligos, Tm = 64.9 + 41*(G+C - 16.4)/(A + T + G + C)

Demonstrate that your program works by computing the 
Tm of several oligos of different sizes. 

For example: 
			print(tm(5, 7, 3, 4))
"""

import math

def oligo_meltingtemp(a, c, t, g):
	length = a + c + t + g 
	
	if length <= 13: 
		tm = ((a + t)**2 + (g + c)*4)	
	else: 
		tm = 64.9 + 41 * (g + c - 16.4) / length
		
	return tm
	
print(oligo_meltingtemp(3, 2, 4, 8))

print(oligo_meltingtemp(10, 10, 10, 10))
	
print(oligo_meltingtemp(1, 1, 1, 1))

