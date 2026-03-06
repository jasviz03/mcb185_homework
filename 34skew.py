import sequence
import mcb185
import sys


w = 1000

g = 0 
c = 0 

for name, seq in mcb185.read_fasta(sys.argv[1]):
	g = 0 
	c = 0 

	for nt in seq[0:w]: 
		if nt == 'G': g += 1 
		elif nt == 'C': c+= 1
	
	for i in range(len(seq) - w + 1): 

		gc_comp = (g + c)/ w
		if g + c == 0: 
			gc_skew = 0 
			
		else: 
			gc_skew = (g - c) / (g + c)
		
		print(i, gc_comp, gc_skew)
	
		if i + w >= len(seq): break
	
		left = seq[i]
		right = seq[i + w]
	
		if left == 'G': g -= 1
		elif left == 'C': c -= 1
	
		if right == 'G': g += 1
		elif right == 'C': c += 1

	
	