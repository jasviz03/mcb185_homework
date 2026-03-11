'''
One of the oldest but still more useful ways to analyze a protein sequence are PROSITE
patterns. 

R-G-D means proteins with the peptide 'RGD' in them
X means any amino acid
[ST] - X - [RK] means S or T followed by any amino acid, followed by R or K
[ILV](3,5) any mixture of 3-5 of these hydrophobic amino acids
{P} means not proline 
<M means begins with met 
>W means ends with trp
'''
import sys
import mcb185

#
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if 'DKTGT' in seq: print(defline)

#regular expression, takes two arguments (pattern and a string)
for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	if re.search('DKGT', seq): print defline

for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq): print(defline)

#you can also...

pat = '(C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H)'
for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	m = re.search(pat, seq)
	if m: print(m.group(1))











































