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


fig, axes = plt.subplots(1,3, figsize=(18,6), sharey=True)
AX = axes.flatten()

ymax = 2500

AX[0].plot(estimators[0,:], estimators[1,:], 'o')
AX[0].plot(range(ymax), range(ymax), '--k')
AX[0].grid()
x = estimators[0,:]
y = estimators[1,:]
A = np.vstack([x, np.ones(len(x))]).T
mc, sr, r, s = np.linalg.lstsq(A, y)
m = mc[0]
c = mc[1]
Rsq = 1 - (sr / np.sum((estimators[1,:] - np.mean(estimators[1,:]*np.ones(len(x))))**2) )
AX[0].plot(x, m*x + c, 'r', label='Fitted line')
#AX[0].set_title('Grad = %f, Res = %f' %(m,sr))
AX[0].legend(['estimator e1', 'y = x', 'regression fit \n($R^2$ = %f)' %Rsq], loc=2)
AX[0].set_ylabel('e$_i$ (estimator value)', fontsize=fsa)
AX[0].set_xlabel('$\mu_i$ (mean species abundance)', fontsize=fsa)
AX[0].annotate("A", (0,0), (0.9,0.05), color='black', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')

AX[1].plot(estimators[0,:], estimators[2,:], 'o')
AX[1].plot(range(ymax), range(ymax), '--k')
AX[1].grid()
x = estimators[0,:]
y = estimators[2,:]
A = np.vstack([x, np.ones(len(x))]).T
mc, sr, r, s = np.linalg.lstsq(A, y)
m = mc[0]
c = mc[1]
Rsq = 1 - (sr / np.sum((estimators[2,:] - np.mean(estimators[2,:]*np.ones(len(x))))**2) )
AX[1].plot(x, m*x + c, 'r', label='Fitted line')
#AX[1].set_title('Grad = %f, Res = %f' %(m,sr))
AX[1].legend(['estimator e2', 'y = x', 'regression fit \n($R^2$ = %f)' %Rsq], loc=2)
AX[1].set_xlabel('$\mu_i$ (mean species abundance)', fontsize=fsa)
AX[1].annotate("B", (0,0), (0.9,0.05), color='black', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')



AX[2].plot(estimators[0,:], estimators[3,:], 'o')
AX[2].plot(range(ymax), range(ymax), '--k')
AX[2].grid()
x = estimators[0,:]
y = estimators[3,:]
A = np.vstack([x, np.ones(len(x))]).T
mc, sr, r, s = np.linalg.lstsq(A, y)
m = mc[0]
c = mc[1]
Rsq = 1 - (sr / np.sum((estimators[3,:] - np.mean(estimators[3,:]*np.ones(len(x))))**2) )
AX[2].plot(x, m*x + c, 'r', label='Fitted line')
#AX[2].set_title('Grad = %f, Res = %f' %(m,sr))
AX[2].legend(['estimator e3', 'y = x', 'regression fit \n($R^2$ = %f)' %Rsq], loc=2)
AX[2].set_xlabel('$\mu_i$ (mean species abundance)', fontsize=fsa)
AX[2].annotate("C", (0,0), (0.9,0.05), color='black', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')

plt.show()



