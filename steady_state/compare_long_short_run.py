import numpy as np
from ss_utilities import stats_at_discrete_times, compare_plot_state_and_stats
import matplotlib.pyplot as plt

pops1 = np.genfromtxt("test_files/lowIM/output_pops.csv", delimiter=',')
pops2 = np.genfromtxt("test_files/lowIM/output_pops_long.csv", delimiter=',')

biomass1= np.sum(pops1,1)
biomass2 = np.sum(pops2,1)
#print(np.shape(biomass))

biomass1 = biomass1[1000:-1]
biomass2 = biomass2[1000:-1]

diff1 = np.diff(biomass1)
diff2 = np.diff(biomass2)


fig, axes = plt.subplots(3,2,figsize=(10,13))

AX = axes.flatten()

n, bins, patches = AX[0].hist(biomass1, 50, normed=1, facecolor='green', alpha=0.75)
AX[0].set_title('Short run (5000 iterations)')
AX[0].set_xlabel('number of individuals')
AX[0].set_ylabel('frequency')

n, bins, patches = AX[1].hist(biomass2, 50, normed=1, facecolor='red', alpha=0.75)
AX[1].set_title('Long run (50000 iterations)')
AX[1].set_xlabel('number of individuals')
AX[1].set_ylabel('frequency')
#stats_at_discrete_times(biomass, [1000, 5000, 40000], 1000, print_flag=True)
#compare_plot_state_and_stats(biomass1, biomass2, range(1000, 4000, 100), 1000)
#plot_state_and_stats(biomass, range(1000,4000,100), 1000)
n, bins, patches = AX[2].hist(diff1, 50, normed=1, facecolor='green', alpha=0.75)
AX[2].set_xlabel('change in number of individuals')
AX[2].set_ylabel('frequency')

n, bins, patches = AX[3].hist(diff2, 50, normed=1, facecolor='red', alpha=0.75)
AX[3].set_xlabel('change in number of individuals')
AX[3].set_ylabel('frequency')

AX[4].plot(biomass1, 'r')
AX[4].set_xlabel('iteration')
AX[4].set_ylabel('biomass')

AX[5].plot(biomass2, 'r')
AX[5].set_xlabel('iteration')
AX[5].set_ylabel('biomass')

plt.subplots_adjust(wspace=0.5)
plt.show()
