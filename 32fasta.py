'''
Reading FASTA files is a little awkward because there is no end-of-record 
delimiter. Records start with a > but the end is either signaled by a new record or 
end of file. 
'''

import sys
import mcb185

for defile, seq in mcb185.read_fasta(sys.argv[1]):
	print(defile[:30], seq[:40], len(seq))











