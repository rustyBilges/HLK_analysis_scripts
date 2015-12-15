"""
This module is for Recurrence Quantification Analysis of N-dimensional time series data.
Univariate time series must be embedded in a phase space before they can be used with this module. 
The choice of how to do this is left to the user. (Time delay embedding is recommended but not implemented.)

Here the threshold 'epsilon' is considered to be constant.
"""

## TODO: edit 'infer' mode: how many standard deviations is good? (maybe make adaptive mode..)

import numpy as np
import random as rand
import matplotlib.pyplot as plt

def _norm(v1,v2):
	"""This method is used to calculate the distance between two points in phase space.
		Currently this method uses the l2-norm.

	Args: 
		v1,v2 (numpy array vector): length N, representing poistion of two points in phase space

	Returns:
		float: the distance between v1 and v2

	Raises:
		ValueError: if the position vectors are not the same length
	"""
	if len(v1)!=len(v2):
		raise ValueError("position vectors not the same length")
		
	return np.sqrt(np.sum((v2-v1)**2)) 

 
def _sample(data, period, original_times=None):
	"""Helper method to sample data, reducing number of data points. 

	Args:
		data: numpy array with full (embedded dynamics), dimension LxN
		period (int): sampling period P (takes one sample from every P data points)
		original_times: list of the original timestamps  

	Returns:
		tuple: (sampled_data, sampled_times)
	"""
	if original_times==None:
		original_times = np.arange(0,np.shape(data)[0])
	
	sampled_data = data[::period,:]
	sampled_times = original_times[::period]

	return (sampled_data,sampled_times)

def recurrence_matrix(data, epsilon=None, mode='infer', time=None):
	"""This method calculates and returns the symmetric recurrence matrix. 

	Args:
		data: LxN numpy array containing the dynamics, where N=embedding dimension, and L=length

		epsilon (float): threshold distance. (less than epsilon->matrix element = 1)
			If None behaviour is specified by 'mode'
	
		mode (string): What to do if epsilon is None
			'infer' -> calculate epsilon as fraction of variance in distance matrix
			'dist'  -> just return distance matrix without thresholding
			'vari'  -> variable thresholding NOT IMPLEMENTED (see Eckmann et al.)

		times: list of times at which the data were sampled. 
			If None defaults to list of integers.
	"""

	length = np.shape(data)[0] 
	distance_matrix = np.zeros((length,length))

	for i in range(length):

		print(i)
		for j in range(length):
			distance_matrix[i,j] = _norm(data[i,:], data[j,:])
			
	if epsilon!=None:
		mp =  distance_matrix <= epsilon
	elif mode=='dist':
		mp = distance_matrix
	elif mode=='infer':
		epsilon = np.mean(distance_matrix) - np.std(distance_matrix)
		print(epsilon)
		mp =  distance_matrix <= epsilon
		print(mp[:10,:10])

	return mp

def _diagonals(rm):
	"""Method returns a list of the lengths all lines parallel to the leading diagonal (45degrees)
	
	Args:
		rm: the binary recurrence matrix

	Returns:
		list: lengths of all diagonals

	""" 
	diagonals = []	

	length = np.shape(rm)[0]
	for i in range(1,length-1):
		#print(len(rm.diagonal(i)))
		Diag = rm.diagonal(i)

		d_len = 0
		for s in Diag:
			if s==1:
				d_len+=1
			elif s==0 and d_len>0:
				if d_len>=2: 
					diagonals.append(d_len)
				d_len = 0

		if d_len>=2:
			diagonals.append(d_len)

	return diagonals

def _surrogate(data):
	"""Creates surrogate white noise data of the same length and width as your data, with same mean and variance in each dimension.

	Args:
		data (numpy array): original data i.e.LxN representing dynamics

	Returns
		numpy array: LxN white noise, each column ni has same mean and variance as in original data
	"""

	wn = np.zeros((np.shape(data)))

	for n in range(np.shape(data)[1]):
		np.random.shuffle(data[:,n])
		#me = np.mean(data[:,n])
		#sd = np.std(data[:,n])
		#for l in range(np.shape(data)[0]):
		#	wn[l,n] = rand.gauss(me,sd)

	return data #wn


if __name__=="__main__":


	epsilon = 1000  ## threshold for heaviside function


	#f = "../steady_state/test_files/highIM/output_pops_long.csv"
	f = "../steady_state/test_files/lowIM/output_pops_long.csv"
	pops = np.genfromtxt(f, delimiter=',')
	pops = pops[1000:,:]

	pops, new_times = _sample(pops,50)

	

	length = 1000
	pops = pops[:length,:]
	#mp = recurrence_matrix(pops, None, 'infer')
	
	mp = recurrence_matrix(pops, epsilon)
	D = _diagonals(mp)	
	print(np.mean(D))
	
	#rpops = _surrogate(pops)
	#mp = recurrence_matrix(rpops, epsilon)
	#_diagonals(mp)	
	
	#check = np.sqrt(np.sum(pops**2,1))
	#plt.plot(check)
	#check = np.sqrt(np.sum(rpops**2,1))
	#plt.plot(check,'r')
	#plt.show()

	plt.imshow(mp)
	plt.show()
		
