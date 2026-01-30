import random 

def saving_throw(dc, mode = 'normal', trials=100000): 
	successes = 0 
	
	for  i in range(trials): 
		roll1= random.randint(1, 20)
		
		if mode == 'normal': 
			roll = roll1
		elif mode == 'advantage': 
			roll2 = random.randint(1, 20)
			roll = max(roll1, roll2)
		elif mode == 'disadvantage':
			roll2 = random.randint(1, 20)
			roll = min(roll1, roll2) 
		
		if roll >= dc: 
			successes += 1 
		
	return successes / trials
	
dcs = [5, 10, 15]
modes = ['normal', 'advantage', 'disadvantage']

for dc in dcs: 
	print(f'\nDC {dc}')
	for mode in modes: 
		rate = saving_throw(dc, mode)
		print(f"  {mode.capitalize():12}: {rate:.3f}")