## this class produces rank abundance distributions

import numpy as np
import matplotlib.pyplot as plt   ## comment out for use on BC3
import matplotlib as mpl
import operator
import math

class Rad_calculator:

	def __init__(self, save_flag=True, save_name='./rad'):
		self.save_flag = save_flag
		self.save_name = save_name

		self.distribution = None
		#print(self.save_flag)	

	def from_output_species(self, directory, fname = 'output_species.csv'):

		## creates from output_species file
		try:
			f = np.genfromtxt(directory + fname, delimiter=',', skip_header=1)
		except:
			print('Cannot open output_species file')
			return

		sp = f[:,0]
		tl = f[:,1]
		ab = f[:,8]

		abundance_dict = dict(zip(sp, ab))
		#print(abundance_dict)
	
		sorted_ab = sorted(abundance_dict.items(), key=operator.itemgetter(1))
		#print(sorted_ab[0])

		ind = 0
		rank = len(sorted_ab)
		distribution = np.zeros((3, len(sorted_ab)))    ## 3rd row to contain trophic level for colouring points on plot
		for a in sorted_ab:
			distribution[0,ind] = rank
			if a[1]>0.0:
				distribution[1,ind] = math.log10(a[1])		
			else:
				distribution[1,ind] = a[1]
			distribution[2,ind] = int(tl[a[0]-1])
			ind += 1
			rank -= 1

		self.distribution = distribution	

		if self.save_flag:
			np.savetxt(self.save_name + '.csv', distribution, delimiter=',')
			#print('saving')
	


if __name__=='__main__':

	r = Rad_calculator(True)
	r.from_output_species('/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/200sp_rewired/mut_0/sp_60/3120931_26/')
