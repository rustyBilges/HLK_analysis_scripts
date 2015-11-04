

import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import stats

import itertools

m_range = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2]
muts = ['0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08', '0.09', '0.1', '0.11', '0.12', '0.13', '0.14', '0.15', '0.16', '0.17', '0.18', '0.19', '0.2']

#m_range = [0, 0.1, 0.2]
#muts = ['0', '.1', '.2']

n_plots = len(m_range)
n_rows = np.ceil(n_plots/2.0)

base_dir = "/MyFiles/cm1788/Documents/parameter_fiddling/bc3_results/rr_v_persistence/mut_0/"

p_id = 1

mut_id = 0
#offset = 1   # 1-> plot abundances, 0-> plot richness

# to store all results:
res_mai = []
prop_prod = []
prop_mut = []
prop_mutprod = []
prop_herb = []
prop_int = []
prop_top = []

for mai in m_range:

	temp_prod = []
	temp_mut = []
	temp_mai = []
	temp_mutprod = []
	temp_herb = []
	temp_int = []
	temp_top = []
	
	dir_name = base_dir + "rr_" + muts[mut_id]
	os.chdir(dir_name)
	rep_dirs = os.listdir('.')

	rep_count = 0
	for d in rep_dirs:
		if d!='src':
			os.chdir(d)
			try:
				eco = np.genfromtxt('output_ecosystem.csv', delimiter=',', skip_header=1)	

				temp_prod.append((eco[-1,4])/eco[-1,2])
				temp_mut.append((eco[-1,10])/eco[-1,2])
				temp_mutprod.append((eco[-1,6])/eco[-1,2])
				temp_herb.append((eco[-1,8])/eco[-1,2])
				temp_int.append((eco[-1,12])/eco[-1,2])
				temp_top.append((eco[-1,14])/eco[-1,2])
				temp_mai.append(float(mai))

				rep_count += 1

			except:
				print('whoops ' + d)

			os.chdir('..')			
			if rep_count>=22:
				break


	print(str(rep_count) + " repeats")

	res_mai.append(temp_mai)

	prop_prod.append(temp_prod)
	prop_mut.append(temp_mut)
	prop_mutprod.append(temp_mutprod)
	prop_herb.append(temp_herb)
	prop_int.append(temp_int)
	prop_top.append(temp_top)

	os.chdir('..')
	mut_id += 1

#flatten:
res_mai = list(itertools.chain(*res_mai))
prop_mut = list(itertools.chain(*prop_mut))
prop_mutprod = list(itertools.chain(*prop_mutprod))
prop_prod = list(itertools.chain(*prop_prod))
prop_herb = list(itertools.chain(*prop_herb))
prop_int = list(itertools.chain(*prop_int))
prop_top = list(itertools.chain(*prop_top))

res_mai = np.asarray(res_mai)
prop_mut = np.asarray(prop_mut)
prop_mutprod = np.asarray(prop_mutprod)
prop_prod = np.asarray(prop_prod)
prop_herb = np.asarray(prop_herb)
prop_int = np.asarray(prop_int)
prop_top = np.asarray(prop_top)


## do the following for all three:
## PRODUCERS:
#regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(res_mai, prop_prod)
line = slope * res_mai + intercept

plt.subplot(3, 2, 1)
plt.scatter(res_mai, prop_prod)
plt.plot(res_mai,line,'r-')
plt.xlabel("reproduction rate")
plt.ylabel("frac. ind.")
plt.title("Producers.  (P = %f)" %p_value)

## HERB:
#regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(res_mai, prop_mutprod)
line = slope * res_mai + intercept

plt.subplot(3, 2, 2)
plt.scatter(res_mai, prop_mutprod)
plt.plot(res_mai,line,'r-')
plt.xlabel("reproduction rate")
plt.ylabel("frac. ind.")
plt.title("Mutualist Producers.  (P = %f)" %p_value)
#plt.ylim([0,40000])

## Intermediate:
#regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(res_mai, prop_herb)
line = slope * res_mai + intercept

plt.subplot(3, 2, 3)
plt.scatter(res_mai, prop_herb)
plt.plot(res_mai,line,'r-')
plt.xlabel("reproduction rate")
plt.ylabel("frac. ind.")
plt.title("Herbivores.  (P = %f)" %p_value)
#plt.ylim([0,40000])


## TOP:
#regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(res_mai, prop_mut)
line = slope * res_mai + intercept

plt.subplot(3, 2, 4)
plt.scatter(res_mai, prop_mut)
plt.plot(res_mai,line,'r-')
plt.xlabel("reproduction rate")
plt.ylabel("frac. ind.")
plt.title("Mutualist animals.  (P = %f)" %p_value)
#plt.ylim([0,40000])

## TOP:
#regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(res_mai, prop_int)
line = slope * res_mai + intercept

plt.subplot(3, 2, 5)
plt.scatter(res_mai, prop_int)
plt.plot(res_mai,line,'r-')
plt.xlabel("reproduction rate")
plt.ylabel("frac. ind.")
plt.title("Primary Predators.  (P = %f)" %p_value)
#plt.ylim([0,40000])

## TOP:
#regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(res_mai, prop_top)
line = slope * res_mai + intercept

plt.subplot(3, 2, 6)
plt.scatter(res_mai, prop_top)
plt.plot(res_mai,line,'r-')
plt.xlabel("reproduction rate")
plt.ylabel("frac. ind.")
plt.title("Top predators.  (P = %f)" %p_value)
#plt.ylim([0,40000])

plt.tight_layout()
#plt.savefig("proportion_per_functional_group")
plt.show()
