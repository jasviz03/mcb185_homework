# 10demo.py by jasmin ;P 
print('hello, again') #greeting 

"""
This is a
multi-line 
comment hahaha
"""

#use a lot of whitespace; makes code look neater and provides clarity

import math

print(1.5e-2)

print (1+2)

#be sure to import math

print(pow(2, 5))

print(2**3) 

print(pow (2, 3))

print(math.pow(2, 3))

print(math.log(2))


a = 3 						#side of triangle 
b = 4 						#side of triangle
c = math.sqrt(a**2 + b**2)	#hypotenuse
print (c)

print(type(a), type(b), type(c))

print(type (a), type (b), type (c), sep=', ', end= '!\n' )

#\n makes a new line (represents vertical space)

#functions are reusable code constructs that form the backbone of computer programs

#def is what defines a program 

def pythagoras(a, b):           #variables a and b are parameters
	c = math.sqrt(a**2 + b**2)	# calculation is stored here 
	return c
	
hyp = pythagoras(3, 4)
print(hyp)

#this could have been simplified a little

def pytha(c,d): 
	return math.sqrt(c**2 + d**2)
	
#no need to create the variable hyp

print(pytha(3,4))


