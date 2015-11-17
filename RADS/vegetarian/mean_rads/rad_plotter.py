## this	
import numpy as np
import matplotlib.pyplot as plt   ## comment out for use on BC3
import matplotlib as mpl
import operator
import math
import itertools



#r = Rad_calculator(False)
	#r.from_output_species('/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/200sp_rewired/mut_0/sp_60/3120931_26/')
	#r2 = Rad_calculator(False)
	#r2.from_output_species('/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/200sp_rewired/mut_0/sp_60/3120931_27/')

	#r1 = np.genfromtxt('RAD_im_0.0001_hl_0_mai_0.csv', delimiter=',')
	#rp.single_plot(r1)

	#rp.combined_plot([r.distribution, r2.distribution], ['one', 'two'])

fig, axes = plt.subplots(3,3, figsize=(13,21))
f_id = 0
IM = [0.005, 0.0005, 0.0001]
HL = [0,40,80]
for im in IM:
	for hl in HL:


		r1 = np.genfromtxt('mean_RAD_im_' + str(im) + '_hl_%d_mai_0.csv' %hl, delimiter=',')
		r2 = np.genfromtxt('mean_RAD_im_' + str(im) + '_hl_%d_mai_0.5.csv' %hl, delimiter=',')
		r3 = np.genfromtxt('mean_RAD_im_' + str(im) + '_hl_%d_mai_1.0.csv' %hl, delimiter=',')
#rp.combined_plot([r1, r2, r3], ['HL = 0', 'HL = 40', 'HL = 80'], 'Single RAD. Immigration = 0.0001. MAI = 0.0')
#rp.multi_tl_plot([r1, r2, r3], ['HL = 0', 'HL = 40', 'HL = 80'], 'Single RAD. Immigration = 0.0001. MAI = 0.0')
		ax = axes.flatten()
		ax = ax[f_id]
#fig, ax = plt.subplots(1,1, figsize=(6,6))
#ax.set_title(title)
		if im == 0.0001:
			ax.set_xlabel('rank')
		if hl==0:
			ax.set_ylabel('log10 (% relative abundance)')
#colors = itertools.cycle(["r", "b", "g"])
		colors = ["r", "g", "b"]
		names = ['MAI = 0.0', 'MAI = 0.5', 'MAI = 1.0' ]
		dists = [r1,r2,r3]
		d_id = 0
		for d in dists:
			distribution = d

			tls = distribution[2,:]

			sc = ax.scatter(distribution[0,:], distribution[1,:], c=colors[d_id])
			#sc = ax.scatter(,_y, c=colors[d_id], marker=_s)
			d_id += 1

#red_patch = mpatches.Patch(color='red', label='The red data')
#plt.legend()
#plt.legend(handle= [ired_patch, blue_patch, green_patch])
		ax.set_xlim([0,60])
		ax.set_ylim([-4.0, 2.0])
		ax.set_title('IM = ' + str(im) + '  HL = ' + str(hl))
		ax.grid()
		f_id += 1
#plt.tight_layout()
plt.subplots_adjust(hspace=0.3)
plt.show()


