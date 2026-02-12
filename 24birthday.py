"""
Same problem as 23birthday.py, make a list from the calendar. In the 
previous program, appended birthdays to the list. In this one, all
possible days are already in a list, so assigning birthdays is 
calendar[birthday] += 1. 
"""

import random
import sys

trials = int(sys.argv[1])

days = int(sys.argv[2])

people = int(sys.argv[3])

samebday = 0

for t in range(trials): 
	calendar = [0] * days
	shared = False
	
	for p in range(people): 
		bday = random.randint(0, days - 1)
		calendar[bday] += 1 
		
		if calendar[bday] > 1: 
			shared = True
			
	if shared: 
		samebday += 1
		
probability = samebday / trials

print('Probability of Shared Birthdays:', probability)








