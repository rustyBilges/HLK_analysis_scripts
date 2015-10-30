import numpy as np
from ss_utilities import stats_at_discrete_times, compare_plot_state_and_stats

pops1 = np.genfromtxt("test_files/lowIM/output_pops.csv", delimiter=',')
pops2 = np.genfromtxt("test_files/highIM/output_pops.csv", delimiter=',')

biomass1= np.sum(pops1,1)
biomass2 = np.sum(pops2,1)
#print(np.shape(biomass))

#stats_at_discrete_times(biomass, [1000, 5000, 40000], 1000, print_flag=True)
compare_plot_state_and_stats(biomass1, biomass2, range(1000, 4000, 100), 1000)
#plot_state_and_stats(biomass, range(1000,4000,100), 1000)
