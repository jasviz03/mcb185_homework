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

"""
Let's talk about block structure
Blocks show hierarchy
all of the code is "owned by the function" is intended by one level
very much like an outline or journal article

If there is only one statement in the block, indentation can be omitted

ex: 
def pytha(a, b): return math.sqrt(a**2 + b**2)
"""
#Let's write some functions

#function that calculates the area of a circle 
def circle_area(r): 
	return math.pi * r**2

print (circle_area(3))

#function that calculates the area of a rectangle
def rectangle_area(l, w): 
		return (l* w)

print(rectangle_area(3,4))

#function that converts fahrenheit to celsius 
def ftoc(f): 
	return((f-32)* 5/9 )

print(ftoc(32))
#function that converts celsius to fahrenheit
def ctof(c): 
	return (c * 9/5 + 32 )
	
print(ctof(-40))

#function that converts feet to centimeters
def fttocm(x): 
	return(x * 12 * 0.0254 / 10**(-2))

print(fttocm(1))

#fucntion that converts ounces to milliliters
def ounce_to_ml(ounce): 
	return (ounce / 33.814 / 10**(-2))

print(ounce_to_ml(33.814))

#find the arithmetic mean of 3 numbers

def mean(a, b, c): 
	return ((a+ b + c)/3)
	
print(mean(1, 2 ,3))

# find the geometric mean of 3 numbers (i didn't know the difference)
def geomean(q, w, e): 
	return math.sqrt(q * w * e)
	
print(geomean(1, 2, 3))



