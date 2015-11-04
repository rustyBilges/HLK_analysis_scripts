

import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import stats

import itertools

type = 'rr'  ## either plot results from mai_v_persistence OR rr_v_persistence simulation runs.

mut_for_rr = '.5/'

if type == 'mut':
        base_dir = "/MyFiles/cm1788/Documents/parameter_fiddling/bc3_results/mai_v_persistence/"
        dir_Ext = 'mut_'
	m_range = [0, 0.5, 1.0]
	muts = ['0', '.5', '1']
        xlab = 'MAI ratio'
        xlimm = [-0.2, 1.2]
        xtlabs = ['', 0, 0.2, 0.4, 0.6, 0.8, 1.0, '']
if type == 'rr':
        base_dir = "/MyFiles/cm1788/Documents/parameter_fiddling/bc3_results/rr_v_persistence/mut_" + mut_for_rr
        dir_Ext = 'rr_'
        m_range = [0.01, 0.1, 0.2]
        muts = ['0.01', '0.1', '0.2']
        xlab = 'reproduction rate'
        xlimm = [0, 0.22]
        xtlabs = ['', 0, 0.05, 0.10, 0.15, 0.20, 0.22, '']


mut_id = 0

mai0 = np.zeros((2,4))
mai5 = np.zeros((2,4))
mai1 = np.zeros((2,4))

for mai in m_range:

	
	dir_name = base_dir + dir_Ext + muts[mut_id]
	os.chdir(dir_name)
	rep_dirs = os.listdir('.')

	rep_count = 0

	temp_tl0 = []
	temp_tl1 = []
	temp_tl2 = []
	temp_tl3 = []
	for d in rep_dirs:
		if d!='src':
			os.chdir(d)
			try:
                                eco = np.genfromtxt('output_ecosystem.csv', delimiter=',', skip_header=1)
				
				n0 = (eco[-1,3] + eco[-1,5])
				n1 = (eco[-1,11])
                                n2 = (eco[-1,7] + eco[-1,9])
				n3 = (eco[-1,13])
				
				n0_in = (eco[0,3] + eco[0,5])
				n1_in = (eco[0,11])
                                n2_in = (eco[0,7] + eco[0,9])
				n3_in = (eco[0,13])

                                temp_tl0.append(n0/float(n0_in)) #/eco[-1,2])
                                temp_tl3.append(n1/float(n1_in))#/eco[-1,2])
                                temp_tl2.append(n2/float(n2_in))#/eco[-1,2])
                                temp_tl1.append(n3/float(n3_in))#/eco[-1,2])
                                #temp_mai.append(float(mai))

				rep_count += 1

			except:
				print('whoops ' + d)

			os.chdir('..')			
			if rep_count>=22:
				break


	if mut_id==0:
		mai0[0,0] = np.mean(temp_tl0)
		mai0[1,0] = np.std(temp_tl0)
		mai0[0,1] = np.mean(temp_tl1)
		mai0[1,1] = np.std(temp_tl1)
		mai0[0,2] = np.mean(temp_tl2)
		mai0[1,2] = np.std(temp_tl2)
		mai0[0,3] = np.mean(temp_tl3)
		mai0[1,3] = np.std(temp_tl3)

	elif mut_id==1:
		mai5[0,0] = np.mean(temp_tl0)
		mai5[1,0] = np.std(temp_tl0)
		mai5[0,1] = np.mean(temp_tl1)
		mai5[1,1] = np.std(temp_tl1)
		mai5[0,2] = np.mean(temp_tl2)
		mai5[1,2] = np.std(temp_tl2)
		mai5[0,3] = np.mean(temp_tl3)
		mai5[1,3] = np.std(temp_tl3)

	elif mut_id==2:
		mai1[0,0] = np.mean(temp_tl0)
		mai1[1,0] = np.std(temp_tl0)
		mai1[0,1] = np.mean(temp_tl1)
		mai1[1,1] = np.std(temp_tl1)
		mai1[0,2] = np.mean(temp_tl2)
		mai1[1,2] = np.std(temp_tl2)
		mai1[0,3] = np.mean(temp_tl3)
		mai1[1,3] = np.std(temp_tl3)

	print(str(rep_count) + " repeats")
	os.chdir('..')
	mut_id += 1



N = 4               # number of data entries
ind = np.arange(N)              # the x locations for the groups
width = 0.25                    # bar width

fig, ax = plt.subplots()

rects1 = ax.bar(ind, mai0[0,:],                  # data
                width,                          # bar width
                color='MediumSlateBlue',        # bar colour
                yerr=mai0[1,:],                  # data for error bars
                error_kw={'ecolor':'Black',    # error-bars colour
                          'linewidth':2})       # error-bar width

rects2 = ax.bar(ind + width, mai5[0,:], 
                width, 
                color='Tomato', 
                yerr=mai5[1,:], 
                error_kw={'ecolor':'Black',
                          'linewidth':2})


rects3 = ax.bar(ind + width + width, mai1[0,:], 
                width, 
                color='Palegreen', 
                yerr=mai1[1,:], 
                error_kw={'ecolor':'Black',
                          'linewidth':2})

axes = plt.gca()
axes.set_ylim([0,1])

ax.set_ylabel('Fraction of initial species that persist')
ax.set_xticks(ind + width + (width/2.0))
ax.set_xticklabels(('TL 1', 'TL 2', 'TL 3', 'TL 4'))

if type=='mut':
	ax.legend( ('MAI = 0.0', 'MAI = 0.5', 'MAI = 1.0'))
elif type=='rr':
	ax.legend( ('Rep. rate = 0.01', 'Rep. rate = 0.1', 'Rep. rate = 0.2'))
#plt.savefig('hist_species_per_tl_zeroIR')
plt.show()
