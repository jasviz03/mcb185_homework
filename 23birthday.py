"""
Write a program that stimulates the problem of filling up classrooms of 
students with randomly assigned birthdays. Make the number of days in the 
calendar and the number of people in the classroom in the classroom command
line arguments. You will have to run this thousands of times to get a real
estimate, so have a parameter for the number of trials. 

Must use a list for the birthdays. For example, if there are 23 people in the
classroom, you will list.append() 23 times. 
"""

import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

samebday = 0 		#how many trials had at least one shared birthday

for t in range(trials): 
	birthdays = []

	for p in range(people): 
		bday = random.randint(0, days - 1)
		birthdays.append(bday)

	if len(birthdays) != len(set(birthdays)): 
		samebday += 1
		
probability = samebday / trials
	
print('Probability of shared birthday:', probability)







