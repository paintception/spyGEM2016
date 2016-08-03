import numpy as np 
import random
from matplotlib import pyplot as plt


class DNA_Analysis(object):
	
	message = ['G','A','C','C','A','A','G','C','C','T','G','C','A','A','A','A','A','C','A','A','A','G','T','G','C','A','A','A','G','A','T',
	'A','T','C','A','G','T','A','A','G','G','T','C','T','T','A','A','A','G','G','C','C','G','A','A','G','C','G','G','T','G','G','C','C','T',
	'A','A','G','A','T','A','A','A','A','C','T','G','G','G','C','G','C','C','C','T','G','G','C','G','T','T','A','G','T','T','C','C','G','C',
	'A','G','A','A','G','A','T','A','A','A','A','C','T','G','G','G','C','T','A','A','G','G','C','A','T','C','A','A','A','G','A','A','G','G',
	'T','A','T','C','T','A','A','A','T','C','C','G','A','A','G','T','A','G','T','T','A','G','C','T','A','A','G','T','G','A','T','T','G','G',
	'C','G','G','G','C','G','A','A','G','G','A','A','T','T','T','G','C','T','A','A','G','C','T','A','T','G','A','A','G','G','A','T','T','G',
	'G','A','C','T','A','A','G','C','C','A','T','T','C','C','C','G','A','A','G','C','T','A','T','C','A','C','A','T','A','A','G','C','G','A',
	'T','G','A','C','A','T','G','C','A','C','C','G','C','A','G','C','A','G','A','C','A','G','G','T','A','C','A','A','A','T','A','A','G','A',
	'A','A','A','C','T','T','T','G','A','A','G','T','C','T','T','T','A','A','G','A','A','T','T','A','G','T','A','T','T','A','A','G','A','A',
	'G','T','G','A','T','G','A','A','G','G','G','C','T','A','T','G','C','C','A','C','C','C','T','C','C','T','A','G','A','G','A','C','A','G','C',
	'T','A','T','A','A','G','C','T','C','T','T','A','A','G','G','A','G','T','G','A','A','G','C','T','G','T','T','G','A','A','T','A','A','G',
	'G','C','G','T','A','G','T','A','G','A','A','G','C','A','A','T','T','A','A','G','T','C','C','T','G','A','A','G','T', 'T','C','T','G','A',
	'A','G','C','T','G','T','T','G','A','C','G','A','A','G','A','T','A','A','A','A','C','T','C','T','G','A','A','T','A','A','T','A','A','G','A',
	'C','C','T','A','C','T','A','T','A','A','G','T','G','C','T','G','A','A','G','C','G','T','T','G','A', 'A','G','A','G','A','T','A','A','G','A',
	'C','A','G','A','G','A','A','G','T','C','T','T','G','A','A','G','T','G','C','T','T','A','A','A','G','A','A','G','C','C','T','T','C','A','A',
	'C','T','A','A','G','T','G','A','T','T','A','C','A','C','T','G','C','T','A','A','G','A','G','A','T','G','A','A','G','C','A','T','T','G','C',
	'A','C','C','C','A','C','C','G','A','C']
	
	def random_mutation():
		pass


	def read_sequence():

	    genome = []

	    with open('BacillusSubtilis.txt') as f:
		    g = map(str.rstrip, f)
		
	    g = ''.join(g)
	    
	    for i in g:
	    	genome.append(i)

	    return genome

	def insert_message(genome, message):
		
		starting_index = random.randint(0, len(genome)-1)
		
		while True:
			ending_index = random.randint(0, len(genome)-1)
			if ending_index > starting_index and ending_index - starting_index == len(message):
				break
		
		genome[starting_index:ending_index] = message
		
		return genome

	if __name__ == '__main__':

		genome = read_sequence()

		inserted_genome = insert_message(genome, message)