import numpy as np
from ss_utilities import stats_at_discrete_times, compare_plot_state_and_stats, plot_state_and_stats, plot_zscore

pops1 = np.genfromtxt("test_files/highIM/output_pops_long.csv", delimiter=',')
#pops1 = np.genfromtxt("test_files/lowIM/output_pops_long.csv", delimiter=',')
#pops1 = np.genfromtxt("test_files/lowIM/output_pops.csv", delimiter=',')
#pops2 = np.genfromtxt("test_files/highIM/output_pops.csv", delimiter=',')

biomass1= np.sum(pops1,1)
biomass1 = np.genfromtxt("test_files/random_walk.csv", delimiter=',')
#biomass1 = np.genfromtxt("test_files/normal_series.csv", delimiter=',')
#biomass2 = np.sum(pops2,1)
#print(np.shape(biomass))

#stats_at_discrete_times(biomass, [1000, 5000, 40000], 1000, print_flag=True)

#compare_plot_state_and_stats(biomass1, biomass2, range(1000, 4000, 100), 1000)

#plot_state_and_stats(biomass, range(1000,4000,100), 1000)
#plot_state_and_stats(biomass1, range(1000,47000,100), 3000)
plot_zscore(biomass1, range(1000,47000,100), 1000)

print(np.mean(biomass1[1000:-1]))
print(np.std(biomass1[1000:-1]))

plot_state_and_stats(biomass1, range(1000,47000,100), 1000)
