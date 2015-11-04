

import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import stats

import itertools

type = 'rr'  ## either plot results from mai_v_persistence OR rr_v_persistence simulation runs.

mut_for_rr = '0/'  ## used only to choose the mai ratio at which the rr simulations were run

if type == 'mut':
        base_dir = "/MyFiles/cm1788/Documents/parameter_fiddling/bc3_results/mai_v_persistence/"
        dir_Ext = 'mut_'
        m_range = np.linspace(0.0, 1.0, 11)
        muts = ['0', '.1', '.2', '.3', '.4', '.5', '.6', '.7', '.8', '.9', '1']
        xlab = 'MAI ratio'
        xlimm = [-0.2, 1.2]
        xtlabs = ['', 0, 0.2, 0.4, 0.6, 0.8, 1.0, '']
if type == 'rr':
        base_dir = "/MyFiles/cm1788/Documents/parameter_fiddling/bc3_results/rr_v_persistence/mut_" + mut_for_rr  
        dir_Ext = 'rr_'
        m_range = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2]
        muts = ['0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08', '0.09', '0.1', '0.11', '0.12', '0.13', '0.14', '0.15', '0.16', '0.17', '0.18', '0.19', '0.2']
        xlab = 'reproduction rate'
        xlimm = [0, 0.22]
        xtlabs = ['', 0, 0.05, 0.10, 0.15, 0.20, 0.22, '']

n_plots = len(m_range)
n_rows = np.ceil(n_plots/2.0)


p_id = 1

mut_id = 0
#offset = 1   # 1-> plot abundances, 0-> plot richness

# to store all results:
res_mai = []
prop_basal = []
prop_top = []
prop_herb = []
prop_int = []

for mai in m_range:

	temp_basal = []
	temp_top = []
	temp_mai = []
	temp_herb = []
	temp_int = []
	
	dir_name = base_dir + dir_Ext + muts[mut_id]
	os.chdir(dir_name)
	rep_dirs = os.listdir('.')

	rep_count = 0
	for d in rep_dirs:
		if d!='src':
			os.chdir(d)
			try:
				eco = np.genfromtxt('output_ecosystem.csv', delimiter=',', skip_header=1)	

				temp_basal.append((eco[-1,3] + eco[-1,5])) #/eco[-1,2])
				temp_top.append((eco[-1,13]))#/eco[-1,2])
				temp_herb.append((eco[-1,7] + eco[-1,9]))#/eco[-1,2])
				temp_int.append((eco[-1,11]))#/eco[-1,2])
				temp_mai.append(float(mai))

				rep_count += 1

			except:
				print('whoops ' + d)

			os.chdir('..')			
			if rep_count>=22:
				break


	print(str(rep_count) + " repeats")

	res_mai.append(temp_mai)

	prop_basal.append(temp_basal)
	prop_top.append(temp_top)
	prop_herb.append(temp_herb)
	prop_int.append(temp_int)

	os.chdir('..')
	mut_id += 1

#flatten:
res_mai = list(itertools.chain(*res_mai))
prop_top = list(itertools.chain(*prop_top))
prop_herb = list(itertools.chain(*prop_herb))
prop_basal = list(itertools.chain(*prop_basal))
prop_int = list(itertools.chain(*prop_int))

res_mai = np.asarray(res_mai)
prop_top = np.asarray(prop_top)
prop_herb = np.asarray(prop_herb)
prop_basal = np.asarray(prop_basal)
prop_int = np.asarray(prop_int)


## do the following for all three:
## BASAL:
#regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(res_mai, prop_basal)
line = slope * res_mai + intercept

plt.subplot(2, 2, 1)
plt.scatter(res_mai, prop_basal)
lli = plt.plot(res_mai,line,'r-', label= "P = %f \nslope = %f" %(p_value, slope))
#plt.xlabel("MAI ratio")
plt.ylabel("species persistence")
plt.title("(A) Trophic level 1")
plt.legend()
plt.grid()
plt.ylim([0,35])
plt.xlim(xlimm)
locs, labels = plt.xticks()
plt.xticks(locs, xtlabs)

## HERB:
#regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(res_mai, prop_herb)
line = slope * res_mai + intercept

plt.subplot(2, 2, 2)
plt.scatter(res_mai, prop_herb)
lli = plt.plot(res_mai,line,'r-', label= "P = %f \nslope = %f" %(p_value, slope))
plt.title("(B) Trophic level 2")
plt.legend()
plt.grid()
plt.ylim([0,35])
plt.xlim(xlimm)
locs, labels = plt.xticks()
plt.xticks(locs, xtlabs)

#plt.ylim([0,40000])

## Intermediate:
#regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(res_mai, prop_int)
line = slope * res_mai + intercept

plt.subplot(2, 2, 3)
plt.scatter(res_mai, prop_int)
lli = plt.plot(res_mai,line,'r-', label= "P = %f \nslope = %f" %(p_value, slope))
plt.xlabel(xlab)
plt.ylabel("species persistence")
plt.title("(C) Trophic level 3") 
plt.grid()
plt.legend()
plt.ylim([0,35])
plt.xlim(xlimm)
locs, labels = plt.xticks()
plt.xticks(locs, xtlabs)


## TOP:
#regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(res_mai, prop_top)
line = slope * res_mai + intercept

plt.subplot(2, 2, 4)
plt.scatter(res_mai, prop_top)
lli = plt.plot(res_mai,line,'r-', label= "P = %f \nslope = %f" %(p_value, slope))
plt.xlabel(xlab)
plt.title("(D) Trophic level 4")
plt.legend()
plt.grid()
plt.ylim([0,35])
plt.xlim(xlimm)
locs, labels = plt.xticks()
plt.xticks(locs, xtlabs)

plt.tight_layout()
#plt.savefig("species_richness_per_trophic_level")
plt.show()
