
## plotting trophic dynamics for a range of parameter values....

import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import stats

import itertools

type = 'rr'  ## either plot results from mai_v_persistence OR rr_v_persistence simulation runs.

if type == 'mut':
	base_dir = "/MyFiles/cm1788/Documents/parameter_fiddling/bc3_results/mai_v_persistence/"
	dir_Ext = 'mut_' 
	m_range = np.linspace(0.0, 1.0, 11)
	muts = ['0', '.1', '.2', '.3', '.4', '.5', '.6', '.7', '.8', '.9', '1']
	xlab = 'MAI ratio'
	xlimm = [-0.2, 1.2]
	xtlabs = ['', 0, 0.2, 0.4, 0.6, 0.8, 1.0, '']
if type == 'rr':
	base_dir = "/MyFiles/cm1788/Documents/parameter_fiddling/bc3_results/rr_v_persistence/mut_.5/"  ## change for other MAI ratios 
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

results = np.zeros((3, len(m_range)))  # 1: MAI; 2: meanProp; 3: sdProp

# to store all results:
res_mai = []
res_prop = []

for mai in m_range:

	results[0, mut_id] = mai
	temp = []
	temp_mai = []
	
	dir_name = base_dir + dir_Ext + muts[mut_id]
	os.chdir(dir_name)
	rep_dirs = os.listdir('.')

	rep_count = 0
	for d in rep_dirs:
		if d!='src':
			os.chdir(d)
			try:
				eco = np.genfromtxt('output_ecosystem.csv', delimiter=',', skip_header=1)	
#				temp.append(float(eco[-1,1]/60.0))
				temp.append(float(eco[-1,1]))
				temp_mai.append(float(mai))


				rep_count += 1

			except:
				print('whoops ' + d)

			os.chdir('..')			
			if rep_count>=22:
				break


	print(str(rep_count) + " repeats")
	results[1,mut_id] = np.mean(temp)
	results[2,mut_id] = np.std(temp)

	res_mai.append(temp_mai)
	res_prop.append(temp)

	os.chdir('..')
	mut_id += 1

#flatten:
res_mai = list(itertools.chain(*res_mai))
res_prop = list(itertools.chain(*res_prop))

res_mai = np.asarray(res_mai)
res_prop = np.asarray(res_prop)

print(res_mai)
print(res_prop)

#regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(res_mai, res_prop)
line = slope * res_mai + intercept

print("p = " + str(p_value))

print(np.shape(res_mai))
print(np.shape(line))

#plt.plot(results[0,:], results[1,:])
#plt.errorbar(results[0,:], results[1,:], yerr=results[2,:])
fig, axes = plt.subplots(figsize=(8,8))

plt.scatter(res_mai, res_prop)
#lli = plt.plot(res_mai,line,'r-', label="Linear regression fit. \nSlope = %f,  P = %f" %(slope,p_value))
lli = plt.plot(res_mai,line,'r-', label="Linear regression fit. \nSlope = %f,  P = %e" %(slope,p_value))
plt.xlabel(xlab, fontsize=15)
#plt.ylabel("persistence (fraction of species remaining)")
plt.ylabel("Fraction of initial species that persist", fontsize=15)
#plt.title("Slope = %f,  P = %f" %(slope,p_value))
plt.legend(handles=lli, fontsize=15)
locs, labels = plt.xticks()
plt.xticks(locs, xtlabs,fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(xlimm)
plt.ylim([0,40])
plt.grid()
plt.show()
