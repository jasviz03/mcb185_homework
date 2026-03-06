"""
Write a program that predicts which proteins in a proteome are transmembrane. 
Transmembrane proteins are characterized by having: 
	a hydrophobic signal near the N-terminus
	other hydrophobic regions to cross the plasma membrane
	
Use Kyte-Doolittle. 

Signal peptide: 8 aa long, average KD >= 2.5, first 30 aa 
transmembrane protein: 11 aa long, average KD >= 2.0, after 30 aa

Both signal peptide and transmembrane regions are alpha-helicies and do not contain 
proline. 
"""
import sys 
import mcb185 
import sequence

#kyte doolittle values

kd = {
'A': 1.8,  'C': 2.5,  'D': -3.5, 'E': -3.5, 'F': 2.8,
'G': -0.4, 'H': -3.2, 'I': 4.5,  'K': -3.9, 'L': 3.8,
'M': 1.9,  'N': -3.5, 'P': -1.6, 'Q': -3.5, 'R': -4.5,
'S': -0.8, 'T': -0.7, 'V': 4.2,  'W': -0.9, 'Y': -1.3
}

for name, seq in mcb185.read_fasta(sys.argv[1]): 
	
	if len(seq) < 30: 
		continue
	
	has_signal = False 
	has_tm = False 

	for i in range(30 - 8 + 1): 
		window = seq[i:i+8]
		
		if 'P' in window: 
			continue
		if any(aa not in kd for aa in window): 
			continue
		
		total = sum(kd[aa] for aa in window)
		if total / 8 >= 2.5: 
			has_signal = True
			break
		
			
	for i in range(30, len(seq) - 11 + 1): 
		window = seq[i:i+11]
		
		if 'P' in window: 
			continue
		if any(aa not in kd for aa in window): 
			continue
		
		total = sum(kd[aa] for aa in window)
		if total / 11 >= 2.0: 
			has_tm = True
			break
			
	if has_signal and has_tm: 
		print(name)





