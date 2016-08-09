from __future__ import division

import numpy as np
from matplotlib import pyplot as plt 

class ProbabilityLord(object):

	def choose_algo():

		correct_algo = 1
		total_algo = 3

		return correct_algo/total_algo

	def choose_wave_length():

		correct_wave_range = 30
		total_range = 100

		return correct_wave_range/total_range

	def chooose_antibiotic():
		
		correct_antibio = 1
		total_antibio = 100

		return correct_antibio/total_antibio


	if __name__ == '__main__':
		
		p1 = choose_algo()
		p2 = choose_wave_length()
		p3 = chooose_antibiotic()


		print p1,p2,p3

		FinalProbability = p1*p2*p3

		print "The Probabilty of success is:", float(FinalProbability)
