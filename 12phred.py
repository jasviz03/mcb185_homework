"""
Write the functions that convert quality symbol values into error rates 
and vice versa. The ord() function returns the ASCII value of a letter. 
The chr() function turns an ASCII value into a letter. 

Demonstrate the functions work by calling them several times. Edge cases
should return None. 

When DNA is sequenced, each base gets a quality value score that tells you
how confident the machine is that the base is correct.

These are stored as ASCII symbols to save space. 

A high Q is a low error rate, while a low Q is a high error rate.
"""
import math

def prob_to_char(n):
	Q = -10 * math.log10(n)  		 #error rate to quality score
	return chr(int(round(Q)) + 33)	 # convert Q to ASCII symbol  

def char_to_prob(sym):
	Q = ord(sym) - 33 
	return 10**(-Q / 10)

print(char_to_prob('I'))
print(char_to_prob('!'))

print(prob_to_char(0.001))
print(prob_to_char(0.5))












