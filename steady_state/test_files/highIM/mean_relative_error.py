import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
 
#fig, axes = plt.subplots(2,2, figsize=(10,6)) 
#AX = axes.flatten() 
#dir = '../network_7_highIM/' 
dir = './' 
 
fsa = 15 
#leg = ['TL1', 'TL2', 'TL3', 'TL4'] 
 
pops = np.genfromtxt(dir + 'output_pops_long.csv', delimiter=',')

estimators = np.zeros((4,60))  ## 1st row = mean (\mu_i), rows 2-4 are estimators 1-3 as described in text.

st = 1000

for i in range(60):

	estimators[0,i] = np.mean(pops[st:,i])
	estimators[1,i] = pops[5000,i]
	estimators[2,i] = np.mean(pops[1000:5000,i])
	estimators[3,i] = np.mean(pops[1000:30000,i])


fig, axes = plt.subplots(1,3, figsize=(18,6))
AX = axes.flatten()

ymax = 1500

AX[0].plot(range(60), np.abs(estimators[0,:]-estimators[1,:])/estimators[0,:], 'o')
AX[0].axhline(0,color='k')
#AX[0].plot(range(ymax), range(ymax), '--k')
AX[0].grid()
#x = estimators[0,:]
#y = estimators[1,:]
#A = np.vstack([x, np.ones(len(x))]).T
#mc, sr, r, s = np.linalg.lstsq(A, y)
#m = mc[0]
#c = mc[1]
#AX[0].plot(x, m*x + c, 'r', label='Fitted line')
#AX[0].set_title('Grad = %f, Res = %f' %(m,sr))

#AX[1].plot(estimators[0,:], estimators[2,:], 'o')
#AX[1].plot(range(ymax), range(ymax), '--k')
AX[1].plot(range(60), np.abs(estimators[0,:]-estimators[2,:])/estimators[0,:], 'o')
AX[1].grid()
AX[1].axhline(0,color='k')

#AX[2].plot(estimators[0,:], estimators[3,:], 'o')
#AX[2].plot(range(ymax), range(ymax), '--k')
AX[2].plot(range(60), np.abs(estimators[0,:]-estimators[3,:])/estimators[0,:], 'o')
AX[2].grid()
AX[2].axhline(0,color='k')

plt.show()



