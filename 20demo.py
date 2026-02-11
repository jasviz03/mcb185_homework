s = 'hello world '

print(s)


s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

"""
String operators

= assignment

+ concatenation 

* repitition 

>, < comparison

== comparison
"""

""" 
String Functions

len(): returns the length of the string 
chr(): get the character whose ASCII Value is inside parentheses
ord(): get the ASCII value of the character inside parentheses
"""

"""
Method Synthax

Variable comes first, then a dot, then the name of the operation, 
finally the parentheses. 

function(string) #function syntax

string.method(): #method syntax

s.count(s1): number of occurrences of s1 in s

s.endswith(s1): true if s ends with s1

s.upper(): Uppercase version of s 

s.lower(): lowercase version of s

s.rstrip(): strip characters from the right (spaces by default)

s.replace(a, b): convert substring a to b 
"""

print(s.upper())
print(s)


print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))


"""
String formatting

Three different syntaxes for string formatting

f.strings : modern and best way 

str.format(): an older method

printf-style: something that look a bit like printf() from C

To make an f-string, proceed with a lowercase f. Anything inside curly 
brackets is interpolated. Code inside curly brackets is live, 
variables can be expanded and functions are called. 

A left justify is text along the left margin, while a right justify 
aligns texts along the right margin.

f for fixed point
e for exponent notation 
<^> for left, center, or right justify
"""
import math

print(f'{math.pi}')   					#does nothing special
print(f'{math.pi:.3f}')					#3 fixed digits after decimal
print(f'{1e6 * math.pi: e}')			#exponent notation
print(f'{"hello world":>20}')			#right justify with space filler
print(f'{"hello world":.>20}')			#right justify with dot filler
print(f'{20:<10} {10}')					#left justify


#String Format 

print('{} {:.3f}'.format('str.format', math.pi))


#printf Style

print('%s %.3f' % ('printf', math.pi))

"""
Indexes
 
Each character in a string has an index. seq[0] refers to the first 
letter of the sequence and seq[1] is the second character. 

Indexes can be negative, in which they can count backwards from the 
right.

You can reiterate through the characters using a for loop. 
"""

seq = 'GAATTC'
print(seq[0], seq[1])

print(seq[-1])						#prints last character of string

for nt in seq: 
	print(nt, end='')				#reiterate through the character using a for loop
print()						

for i in range(len(seq)): 			#iterate through the letters by their indices using range()
	print(i, seq[i])				#len is used to set the limit

"""
Slices 

Subset of a container. Slice operator is a pair of square brackets with a colon inside. 
Work like the range() function in that they take an initial position and end-before limit. 
The following code prints the first five letters of the string. 
"""

s = ' ABCDEFGHIJ'
print(s[0:5])						#0 represents the initial position while 5 is the end-before limit

#This prints out ABCD

print(s[0:8:2])						#prints out BDF, step size is set to 2 and goes up to 7th letter

print(s[0:5], s[:5])

print(s[5: len(s)], s[5:])

print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3): 
	codon = dna[i:i+3]
	print(i, codon)

"""
Tuples 

Container that holds multiple values. Generally constructed with comma-
separated values (usually in parentheses
"""

tax = ('Homo', 'sapiens', '9606')
print(tax)

#Tuples and strings are immutable, cannot change their contents by poking at
#indicies, next two lines will generate errors

"""
s[0] = 'C'
tax[0] = 'human'
"""

#linear containers of values, just like strings, can be indexes and sliced using same syntax

print(tax[0])						#index
print(tax[::-1])					#slice

# enumerate

nts = 'ACGT'
for i in range(len(nts)): 
	print(i, nts[i])
	
for i, n in enumerate(nts): 
	print(i, nt)
	
# zip 
# range simultaneously indexes separate containers

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)): 
	print(nts[i], names[i])

for nt, name in zip(nts, names): 
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)): 
	print(i, nt, name)

"""
Lists

Similar to tuples except they are constructed with square brackets and their
contents are mutable. 
"""

nts = ['A', 'T', 'C']                          
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')   #elements can be added to the end of a list with list.append()
print(nts)			#most operations on lists use method syntax

last = nts.pop()	#remove elements from end of the list with list.pop()
print(last)

nts.sort()
print(nts)

nts.sort(reverse=True)	#lists are sorted with these and can have a mixture of ints and floats
print(nts)				#cannot mix them with strings

nucleotides = nts		#same list, different name
nucleotides.append('C')	#nucleotides is modified and SAME MODS occur in nts
nucleotides.sort()
print(nts, nucleotides)

"""
To make a copy, use list.copy. This is a shallow copy, meaning that multi-dimensional 
lists and other complex data structures are NOT FULLY COPIED.
"""

items = list()		#creates an empty list since there are no arguments
print(items)		#printed []

items.append('eggs')
print(items)		#now prints out ['eggs']

stuff = []			#still an empty list
stuff.append(3)		#adding the number three
print(stuff)		#printed [3]

alph = 'ABCDEFGHIKLMPQRVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day 			to you'
words = text.split()	#splits strings into lists of strings
print(words)			#delimiter is any number of spaces

#for CSV or TSV data, split on \t or comma

line = '1.41,2.72,3.14'
print(line.split(','))

#lists can be turned in strings by joining them with a delimiter
#which could be nothing

s = '-'.join(aas)
print(s)

s = ''.join(aas)
print(s)

"""
Searching for items in containers

You can use in, find(), and index()
"""

#in; works well in conditional statements

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

#index:returns the index of the first element it finds. if not found, returns error

print('index G?', alph.index('G'))

#print('index Z?', alph.index('Z')) RETURNS AN ERROR

'''
find, returns the index of the first elements it finds or a -1 if it can't be found
Works only for strings, NOT TUPLES OR LISTS 
'''

print('Find G?', alph.find('G'))
print('Find Z?', alph.find('Z'))

#If you are in a list or a tuple, and are unsure about the element being found, use in

#if thing in list: idx = list.index(thing)

#write a function that returns the minimum value of a list

def minimum(vals): 
	mini = vals[0]			#assumes the first value is smallest
	for val in vals [1:]:   #loops through everything after first element
		if val < mini: 
			mini = val 		#updates mini if we find something smaller 
	return mini


print(minimum([1, 2, 3]))

#Write a function that returns both the minimum and maximum values of a list

def min_and_max(valss):
	min = valss[0]				#assume first element is the smallest value
	max = valss[0]				#assume first element is largest value
	for val in valss: 			#loop thru all values in list
		if val < min: min = val #if current number is smaller than what we think is mini, then update mini
		if val > max: max = val	#if current number is bigger than what we think is the maxi, update maxi
	return min, max
	
print(min_and_max([1, 2, 3, 4, 5]))

#Write the function that returns the mean of the values in a list


def mean(vals): 
	total = 0 
	for val in vals: total += val 		
	return total / len(vals)

print(mean([1, 2, 3]))

import math

#write a function that computes the entropy of a probability distribution

def entropy(probability): 
	h = 0
	for prob in probability: 
		h -= prob * math.log2(prob)
	return h
	
print(entropy([0.9, 0.8, 0.7]))

#write a function that computes the kullback-leibler distance between two sets of prob dist

def k_ldistance(P,Q): 
	d = 0 
	for p, q in zip(P, Q): 
		d += p * math.log2(p/q)
	return d 
p1  = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)

print(k_ldistance(p1, p2))

"""
External Data 

all of the code examples so far have included the data in the program. 
programs can be given data from various sources, which might include user 
input, a file, or a network connection. 
"""

#input: allows python programs to get a line of input from the user

#line = input('type something and hit return: ')
#print('that line was', len(line), 'characters long')

#sys.argv: complete list of words on the command line

import sys
print(sys.argv)

i = int('42')
x = float('0.61803')
print (x * i)

# x = float('hello'): can't convert string to float






















