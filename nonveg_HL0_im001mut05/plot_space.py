import matplotlib.pyplot as plt
import numpy as np


time = range(200,5200,200)
#time = [200,400]

id = 0

for t in time:
	
	inh = np.genfromtxt('output_inhabitant_%d.csv' %t, delimiter=',')
	vis = np.genfromtxt('output_visitor_%d.csv'%t, delimiter=',')

	plt.subplot(1,2,1)
	plt.pcolor(inh)
	plt.subplot(1,2,2)
	plt.pcolor(vis)
	#plt.colorbar()
	plt.savefig('%d.png' %id)
	#plt.show()
	print(id)
	id += 1


