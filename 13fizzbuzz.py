"""
Make a program that writes out the numbers 1 to 100. If the number is divisible, 
write Fizz instead. If the number is divisible by 5, write Buzz. If the number is 
divisible by both 3 and 5, write FizzBuzz
"""

for i in range(101): 
	if i % 15 == 0: print('FizzBuzz')
	elif i % 3 == 0: print('Fizz')
	elif i % 5 == 0: print('Buzz')
	else: print(i)
	
