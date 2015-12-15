import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
 
dir = './HIensemble/' 
 
fsa = 15 
 
results = np.genfromtxt(dir + 'error_versus_estimator.csv', delimiter=',')
rows = np.shape(results)[0]
rsq = results[range(0,rows,2),:]
mre = results[range(1,rows,2),:]

print(np.mean(rsq,0))
print(np.shape(mre))
E = np.asarray(range(np.shape(results)[1]))+1
print(E)
fig, axes = plt.subplots(1,1) #, figsize=(18,6), sharey=True)
AX = [axes] #.flatten()


AX[0].errorbar(E, np.mean(rsq,0), yerr=np.std(rsq,0),fmt='o', label='$R^2$ (HI ensemble)')
AX[0].errorbar(E, np.mean(mre,0), yerr=np.std(mre,0),fmt='o', label='M.R.E (HI ensemble)')
#AX[0].plot(E, np.mean(rsq,0))
#AX[0].plot(range(ymax), range(ymax), '--k')
AX[0].grid()
AX[0].set_ylim([0.0,1.1])

#AX[0].plot(x, m*x + c, 'r', label='Fitted line')
#AX[0].set_title('Grad = %f, Res = %f' %(m,sr))
#AX[0].legend(['estimator e1', 'y = x', 'regression fit \n($R^2$ = %f)' %Rsq], loc=2)
AX[0].set_ylabel('error value', fontsize=fsa)
AX[0].set_xlabel('estimator ID', fontsize=fsa)

dir = './LIensemble/' 
results = np.genfromtxt(dir + 'error_versus_estimator.csv', delimiter=',')
rows = np.shape(results)[0]
rsq = results[range(0,rows,2),:]
mre = results[range(1,rows,2),:]
AX[0].errorbar(E, np.mean(rsq,0), yerr=np.std(rsq,0),fmt='o', label='$R^2$ (LI ensemble)')
AX[0].errorbar(E, np.mean(mre,0), yerr=np.std(mre,0),fmt='o', color='k', label='M.R.E. (LI ensemble)')
AX[0].legend(loc=7)

plt.show()



