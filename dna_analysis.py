import numpy as np 
import random
import copy
from matplotlib import pyplot as plt


class DNA_Analysis():
	
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
	'G','C','G','T','A','G','T','A','G','A','A','G','C','A','A','T','T','A','A','G','T','C','C','T','G','A','A','G','T','T','C','T','G','A',
	'A','G','C','T','G','T','T','G','A','C','G','A','A','G','A','T','A','A','A','A','C','T','C','T','G','A','A','T','A','A','T','A','A','G','A',
	'C','C','T','A','C','T','A','T','A','A','G','T','G','C','T','G','A','A','G','C','G','T','T','G','A', 'A','G','A','G','A','T','A','A','G','A',
	'C','A','G','A','G','A','A','G','T','C','T','T','G','A','A','G','T','G','C','T','T','A','A','A','G','A','A','G','C','C','T','T','C','A','A',
	'C','T','A','A','G','T','G','A','T','T','A','C','A','C','T','G','C','T','A','A','G','A','G','A','T','G','A','A','G','C','A','T','T','G','C',
	'A','C','C','C','A','C','C','G','A','C']
	
	def random_mutation(g):		#Random Mutation works TODO implement the causes of the mutation rate
		
		mutation_rate = 2
		indexes_to_mutate = []

		for i in xrange(0,mutation_rate):
			index = random.randint(0,len(g)-1)
			indexes_to_mutate.append(index)

		for i in xrange(0,len(g)):
			for j in indexes_to_mutate:
				
				print "=== Generating the Random Mutations ==="		

				if i == j:
					if g[i] == 'A':
						mutation = random.randint(0,2)
						if mutation == 0:
							g[i] = 'T'
						elif mutation == 1:
							g[i] = 'C'
						elif mutation == 2:
							g[i] = 'G'

					elif g[i] == 'T':
						mutation = random.randint(0,2)
						if mutation == 0:
							g[i] = 'A'
						elif mutation == 1:
							g[i] = 'C'
						elif mutation == 2:
							g[i] = 'G'
		
					elif g[i] == 'C':
						mutation = random.randint(0,2)
						if mutation == 0:
							g[i] = 'A'
						elif mutation == 1:
							g[i] = 'T'
						elif mutation == 2:
							g[i] = 'G'
	
					elif g[i] == 'G':
						mutation = random.randint(0,2)
						if mutation == 0:
							g[i] = 'A'
						elif mutation == 1:
							g[i] = 'C'
						elif mutation == 2:
							g[i] = 'T'
		
				return g

	def check_genomes(original_g, mutated_g):
		
		random_mutation_indexes = []
		random_mutation_values = []

		for i, (or_g, mut_g) in enumerate(zip(original_g, mutated_g)):
			if or_g != mut_g:
				random_mutation_values.append(mut_g)
				random_mutation_indexes.append(i) 

		print "Mutated components", random_mutation_values
		print "Position", random_mutation_indexes

		return random_mutation_values, random_mutation_indexes	#important for checking if the indexes are the same ones of where the message is placed

	def read_sequence():	#Original Bacteria DNA sequence

	    genome = []

	    with open('BacillusSubtilis.txt') as f:
		    g = map(str.rstrip, f)
		
	    g = ''.join(g)
	    
	    for i in g:
	    	genome.append(i)

	    print "=== Importing Bacillus Subtilis DNA ==="

	    return genome

	def insert_message(genome, message):	#Message is there!
		
		starting_index = random.randint(0, len(genome)-1)
		
		while True:
			ending_index = random.randint(0, len(genome)-1)
			if ending_index > starting_index and ending_index - starting_index == len(message):
				break
		
		genome[starting_index:ending_index] = message
		
		print "=== Inserting the Message into the DNA ==="

		return genome

	if __name__ == '__main__':
		
		"""
		orig_g = ['A','T','T','C','G','T']
		intact_genome = copy.copy(orig_g)
		mutat_g = random_mutation(orig_g)
		print "Original Genome After", intact_genome
		print "Mutated Genome", mutat_g		
		check_genomes(intact_genome, mutat_g)
		"""
		genome = read_sequence()
		
		inserted_genome = insert_message(genome, message)
		intact_inserted_genome = copy.copy(inserted_genome)
		mutated_genome = random_mutation(inserted_genome)
		check_genomes(intact_inserted_genome, mutated_genome)



