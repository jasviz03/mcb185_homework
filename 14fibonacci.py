"""
Write a program that reports the first ten numbers from the fibonacci sequence. This is a
tricky problem. You need to initialize and keep track of the previous two values. 
"""

a = 0
b = 1 

for i in range(10): 
	print(a)
	a, b = b, a + b