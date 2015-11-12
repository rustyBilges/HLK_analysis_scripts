import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as ts
from ss_utilities import stats_at_discrete_times, compare_plot_state_and_stats, plot_state_and_stats, plot_zscore
from ss_utilities import  _autocorr, stats_at_discrete_times

#pops1 = np.genfromtxt("test_files/highIM/output_pops_long.csv", delimiter=',')
pops1 = np.genfromtxt("test_files/lowIM/output_pops_long.csv", delimiter=',')
#pops1 = np.genfromtxt("test_files/lowIM/output_pops.csv", delimiter=',')
#pops2 = np.genfromtxt("test_files/highIM/output_pops.csv", delimiter=',')


#   AX[0].plot(hi, 'r', label= 'IBM simulation (high IR)')

adfs0= []
adfs = []

for r in range(60):
	hi = pops1[-4000:-1, r] 
        result = ts.adfuller(hi)
        adfs.append(result[0])	
	print(result[0])
	
	hi2 = pops1[2000:6000, r] 
        result = ts.adfuller(hi2)
        adfs0.append(result[0])	


print(result)

plt.plot(adfs0, 'ro')
plt.plot(adfs, 'bo')
plt.axhline(-2.86)
plt.show()
