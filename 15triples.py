"""
Write a program that finds all Pythagorean triples with sides a and b less 
than 100. For example, 3, 4, 5 is a triple. 3'^2 + 4^2 = 5^2. Hint: all 
sides including the hypotenuse, must be integers. A good way to test for an
integer is like: if c % 1 == 0. 
"""

for a in range(100): 
	for b in range (1, 100): 
		c = (a**2 + b**2) ** 0.5
		if c % 1 == 0: 
			print (a, b, int(c))