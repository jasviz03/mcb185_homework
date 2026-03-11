# Files

'''
Most data is stored in files. General rules: open file, stream data from it and close 
when done. 


fp = open(path)
for line in fp: 
	do_something_with(line)
fp.close()

open(): function that creates a new variable which is commonly called a "file pointer"
(or an fp)
	takes a path argument, which can be relative or absolute

type(open()): _io.TetxIOWrapper

for loop iterates through the file until there are no more lines left to read

do_something_with: stand in for whatever you plan to do 

fp.close(): closes the file, DO NOT FORGET THIS STEP
	other ways of closing a file include using the 'with' Python keyword
	
		with open(path) as fp: 
			for line in fp: 
				do_something_with(line)

#reading a compressed file
	import gzip
	gzip.open(path, 'rt')

	import gzip
	with gzip.open(path, 'rt')
		for line in fp: 
			print(line, end = '')
'''

#continue

'''
continue is used to immediately end the current iteration of the loop and restart it 
with the next iteration. can be called next. 

code below is somewhat different than the one above: 
	gets rid of the problem cases and operates on what is left
	
with gzip.open(sys.argv[1], 'rt') as fp: 
	for line in fp: 
		if line[0] == '#': continue
		words = line.split()
		if words[2] != 'CDS': continue
		beg = int(words[3])
		end = int(words[4])
		print(end - beg + 1)
		
'''

#Reading FASTA files

'''
Sequences are often stored in FASTA files. A single sequence record has a definition line 
followed by multiple lines of sequence. 

defile begins with a > and is immediately followed by an identifier that is usually
a unique identifier for the sequence. rest of the defile can have any descriptive info. 

Multi-FASTA files have more than one sequence record. Heres an example with two. 
There is no way of knowing if a FASTA has more than one record in it until you 
read it. 
'''

'''
Most software engineers create unit tests and integration tests that call lib 
functions with various arguments. Tests ensure that code works properly, 
unexpected input is handled correctly and that new changes to the code 
still provide the same output as the old code. Automated testing is a standard 
in the professional setting. 
'''

#sliding window algorithms

'''
w = 10   			sets size of the window, is three for translation bc of codons
s = 1 				sets step size, for trans this is three
for i in range(0, len(seq), -w +1, s): moves window along sequence
	subseq = seq[i:i+w]		creates a subsequence as a slice using offset i and w
'''

#sets

'''
A set is a mutable container, but all of the elements are unique and the 
elements are not ordered. 
'''

s = { 'A', 'G', 'C'}
print(s)				#mutable, changes when you run the program every time

s.add('T')
print(s)

s.add('A')				#adding same element does nothing
print(s)


#print(s[2]) will do nothing since there is no order

#dictionaries

'''
like a list, but the indices are strings instead of numbers. 
	list[0] - 0 is a numeric index
	dict['hey'] - 'hey' is a string index
	
no append() for dictionaries, each item exists as a key:value pair 
	key is the string in the square brackets
	value is anything you can put in a variable
	
An empty dictionary is created with either empty curly brackets or the dict() function
	d = {}
	d = dict()

To make a predefined dictionary, we can use curly brackets and key:value pairs
	d = {'dog' : 'woof', 'cat': 'meow'}
	print(d)

Both dictionaries and sets are displayed as curly brackets. DICTIONARIES USE THE 
KEY:VALUES PAIRS. SETS ARE JUST VALUES. 

dictionaries are efficient for lookups.
'''

d = {'dog' : 'woof', 'cat': 'meow'}
print(d)

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

#print(d['rat'])		#should result in an error

if 'dog' in d: print(d['dog'])


#iteration

'''
standard for loop iterates over the keys in the order in which they were created. to
get a specific element, use the key as an index to the dictionary. 

'''

for key in d: print (f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)

print(d.keys(), d.values(), list(d.values()))

#lookup tables

''''
dictionaries are tidy and efficient for looking values from a table. 

most labor intensive way is to make a stack of conditionals, DON'T DO THIS

another way is index parallel lists, it is the same linear search. 

best way is to make a dictionary. 
'''

kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)
    
#Categorical Data

'''
dictionaries can be used to categorize new info. 
'''

#Sorting 

'''
can sort through linux sort, the first line below sorts the output by the 
feature name. 

	for k in sorted(count): print(k, count[k])

	for k, v in sorted(count.items(), key = lambda item[1]): 
		print(k, v)

lambdas are tiny anonymous functions, reads the tuple item and returns the 
second element item[1] as the return value. 
'''

#does the same thing as lambda function 

'''
def by_tuple(tuple): 
	return tuple[1]

for k,v in sorted(count.items(), key = by_value): 
	print(k,v)
'''

#K-mers

'''
Simple a sequence of length k, where k is a small integer. The subsequences of 
sliding window algorithms are k-mers. Individual nts are k-mers of length 1. 
'''

import itertools
for nts in itertools.product('ACGT', repeat = 2):
	print(nts)

#argparse: finding help in python

#positional arguments 

#named arguments

#multiple dimensions

'''
sys.argv is a list with a single element: the name of your program, and of 
course you can access that by indexing. 

a list of strings is a 2d data structure. strings are 1d, letters are 2d
	putting a container inside other containers = multidimensional
	containers do not have to be the same size or shape
'''

import sys

print(sys.argv)
print(sys.argv[0])

print(sys.argv[0][3])

d = [
	'hello', 
	(3.14, 'pi'), 
	[-1, 0, 1], 
	{'year': 2000, 'month': 7}
]

print(d[0][4], d[1][0], d[2][2], d[3]['month'])


#arrays and matrices

'''
array and list are sometimes used interchangeably. In some languages, they mean the same 
thing. 

python defines arrays and lists seperately. 
	arrrays are constructed with array() function. 
	matricies are rectangular, and like arrays are of the same type. 
	computationally, arrays and matricies are much more efficent than lists
	
'''

#records 

'''
one of the most important data types is the list of dictionaries, can be a list of anything. 

record is a data type with various named fields.

catalog is a list of records. 

lists of records can be very large, so we don't type them in. we typically read them 
from files. here is how we would be able to read a CSV file. 
'''

def read_catalog(filepath): 
	catalog = []
	with open(filepath) as fp:
		for line in fp: 
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split()
			record = {
				'Name': name, 
				'Length': length, 
				'Sequence': seq, 
				'Description': desc
			}
			catalog.append(record)
	return catalog

catalog = read_catalog('primers.csv')
for primer in catalog: 
	print(primer['Name'], primer['Description'])


#Dicts of Lists

'''
What if we wanted to know the location of each kmer in the sequence? 

In order to record locations of kmers, we need to turn to initializion of 0 into an 
intialiation of an empty list. And then instead of counting kmers, we need to append
their locations.  
'''

kcount = {}
for i in range(len(seq) -k +1): 
	kmer = seq[i:i+k]
	if kmer not in kcount: kcount[kmer] = 0
	kcount[kmer] += 1
	
seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
k = 2 
kloc = {}
for i in range(len(seq) -k+1): 
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)

#complex data

'''
" " are used to write JSON code. This is very compatible to python, with a few exceptions.
	Double quotes only
	boolean values are true and false 
	trailing commas are not allowed on the last element of the block
	there are no comments
	
python does provide the the json library for reading and writing json. 
json.dumps() can be a useful way of examining the structure.
'''

truc = {
		'animals': {'dog':'woof', 'cat': 'meow', 'pig': 'oink'}, 
		'numbers': [1.09, 2.72, 3.14], 
		'is_complete': False, 
}
print(json.dumps(truc, indent = 4))

#Regular expressions

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









			
			
			
			
			
			
