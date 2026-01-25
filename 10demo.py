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

# find the area of a sphere 
def sphere_area(r): 
	return (4 * math.pi * (r**2))

print(sphere_area(2))

#strings are a sequence of characters written inside quotes; can include letters, numbers, symbols and spaces
s = 'hello world'
print(s, type(s))

#conditional statements

"""
makes choices about what we do next 
 = is used for an assignment
== is an equal sign
"""
a = 3
b = 2

print(a,b)

if a == b: 
	print('a equals b')  #block structure

def is_even(x):
	if x % 2 == 0: return True
	return False
	
print(is_even(2))
print(is_even(3))
	
#boolean; can have a value of true or false
c = a == b
print(c)
print(type(c))

#can be formatted like this if there is not multiple statements

if 	 a < b: print('a < b')
elif a > b: print('a > b')	
else: 		print('a == b') 

#if-elif-else construct, only the first condition is executed

if    a < b: print( 'a < b ')
elif a <= b: print( ' a <= b ') 
elif a == b: print( 'a ==b ') # this will never print!!!

#boolean chains; can be chained with 'and', 'or' and inverted with 'not'
if a < b or a > b: print( 'all things equal, a and b are are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

#floating point warning 
a = 0.3 
b = 0.1 * 3 

print (a, b)

if     a < b: print('a < b ')
elif   a > b: print('a > b ')
else:         print('a == b')

"""
running this code will report that 
a < b
NEVER test for an inequality with floating point numbers
"""

print(abs(a-b))									#examine their difference
if abs(a-b) < 1e-9: print(' close enough ')		#if there is a less than acceptable
												#precision, consider them the same
												
#we can use math.isclose instead of doing it manually
if math.isclose (a, b): print( ' close enough ')

#string comparison

"""
compared alphabetically, kinda 
compared to their ASCII values
"""

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print( ' A < B ')
if s2 < s3: print ( ' B < a')

""""
#mismatched type error
a = 1 
s = 'G'
if a < s: print( ' a < s ') 		#will result in a type error
"""

#none type
def silly(m , x , b): 
	y = m * x + b
	
print(silly(2, 3, 4))  #output is none

#write a function that determines if a number is an integer
def is_integer(a): 
	r = a % 1 
	if math.isclose (0,r): return True
	else: 				   return False
	
print(is_integer(3.0))


#write a function that determines if a number is a valid probability (number between 0 - 1)
def is_prob(b): 
	if b<= 1 and b>= 0: print('is a valid probability')
	else: 				print('not a probability')

(is_prob(0.89))										#do not need a print here
													#sends value back to the function
"""
write a function that returns the molecular weight of a DNA letter. 
if the letter does not match any nucleotide, return None
"""

def nucleotide_weight(base): 
	if base == 'A': 
		return 331
	elif base == 'T': 
		return 322			
	elif base == 'G': 
		return 347 		
	elif base == 'C':
		return 307		
	else: 
		return None
		
print(nucleotide_weight('A'), 'Da', sep = ' ')

"""
write a function that returns the complement 
of a DNA letter, returning None if the letter isn't DNA
"""

def DNA_complement(base): 
	if base == 'A'  :  
		return 'T' 
	elif base == 'T': 
		return 'A'
	elif base == 'G': 
		return 'C'
	elif base == 'C': 
		return 'G'
	else: 
		return None
		
print(DNA_complement('U'))

"""
style is important for coding 
another coder being able to understand your code is important
code with poor style is confusing 
and difficult to maintain/extend



naming conventions 
x : can represent anything, but often a float
i, j, k are loop variables
n, m are integers
a, b, and c are numbers
x, y, and z are floats/cartesian coordinates 
p, q are probabilities
s, including s1, and s2 are a list of strings
X is a list of numbers
P, Q are probability distributions 
nt represent nucleotides
dna is a string of nucleotide symbols
aa represents amino acids
seq is a string of aa or nucleotides 
seqs is a list of sequences 
file is a named file path 
fp is a file pointer
"""

#write a function that returns the maximum of 3 numbers; returns the single largest one
def maxofthree(n, m, o): 
	if n > m: 
		return n 
	elif m > o: 
		return m 
	else: 
		return o 
		
print(maxofthree(1,2,3))

"""
given values for true positives, true negatives, and false negatives
write functions that return specificity, sensitivity, and F1 score 
"""

TN = 6
TP = 8
FN = 2
FP = 1

def specificity(TN, FP): 
	return TN / (TN + FP)
	
def sensitivity(TP, FN): 
	return TP / (TP + FN)

def f1score(TP, FP, FN): 
	return (2 * TP) / (2 * TP + FP + FN)

print('sensitivity:',  sensitivity(TP, FN))
print('specificity:',  specificity(TN, FP))
print('F1 Score:', 	   f1score(TP, FP, FN))


"""
write the function that returns the Shannon entropy 
for nucleotide counts A, C, G, T. It should work 
in the case where there are zero counts for one 
or more letters. 
"""

#i don't know what shannon entropy is. time to find out. 
#shannon entropy is a standard measure of order state of symbol sequences

def shannon_entropy(A, C, G, T): 
	counts = [A, C, G, T]
	total= sum(counts)         #total number of nucleotides

	if total == 0: 
		return 0  #no nucleotides, so entropy is 0 
		
	entropy = 0
	for count in counts: 
		if count > 0: 		# skips zero counts to avoid log2(0)
			p = count / total
			entropy -= p * math.log2(p) #Shannon formula
		return entropy
		
print(shannon_entropy(30,0,0,0))

