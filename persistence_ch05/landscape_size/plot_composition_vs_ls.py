
## plotting trophic dynamics for a range of parameter values....

import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import stats

import itertools

species = [100, 200, 300, 400, 500, 600, 800, 1000]  ## by species of course, we mean landscape (size)

web_type = 'standard'  ## no problem with standard constraints for 60sp, therefore only these were used for lsvp sims.
mut_level = '0.5/'  ## '0.0/'

fs = 15 ## font size

if web_type == 'standard':
	base_dir = "/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/landscape_size_vs_persistence/mut_" + mut_level

total_abundance = np.zeros((5, len(species)))  # 0-th for initial number species size 1,2-nd for total individuals, 3-4th for number of species remaining

basal_abundance = np.zeros((5, len(species)))  # as above but only looking at species with TL = 0
herb_abundance = np.zeros((5, len(species)))  # as above but only looking at species with TL = 1
int_abundance = np.zeros((5, len(species)))  # as above but only looking at species with TL = 2
top_abundance = np.zeros((5, len(species)))  # as above but only looking at species with TL = 3

# to calculate the sdevs:
sd0 = []
sd1 = []
sd2 = []
sd3 = []
sdT = []

sp_id = 0
for sp in species:

	total_abundance[0, sp_id] = sp
	basal_abundance[0, sp_id] = sp
	herb_abundance[0, sp_id] = sp
	int_abundance[0, sp_id] = sp
	top_abundance[0, sp_id] = sp
	
	dir_name = base_dir + "landscape_%d" %sp
	os.chdir(dir_name)
	rep_dirs = os.listdir('.')

	sdev0 = []	
	sdev1 = []	
	sdev2 = []	
	sdev3 = []	
	sdevT = []	

	rep_count = 0
	for d in rep_dirs:
		
		if d!='src' and d!= 'find_networks_noconstraints.png'and d!= 'find_networks_rewired.png':
			os.chdir(d)
			try:
				eco = np.genfromtxt('output_species.csv', delimiter=',', skip_header=1)	

				S = np.sum(eco[:,8])  # total number of individuals at the end of this simulation
				total_abundance[1,sp_id] += float(S)

				sp_count = 0
				for i in eco[:,8]:
					if i>0.0:
						sp_count += 1

				total_abundance[3, sp_id] += sp_count

				## look at only basal species:
				S = eco[:,8]
				TL = eco[:,1]
				tl_id = 0
				
				## to calculate sdevs:
			        cnt0 = 0			
			        cnt1 = 0			
			        cnt2 = 0			
			        cnt3 = 0			
				
				for s in S:
					if s != 0.0:
						if TL[tl_id]==0:
							basal_abundance[1,sp_id] += s
							basal_abundance[3,sp_id] += 1
							cnt0 += 1
						elif TL[tl_id]==1:
							herb_abundance[1,sp_id] += s
							herb_abundance[3,sp_id] += 1
							cnt1 += 1
						elif TL[tl_id]==2:
							int_abundance[1,sp_id] += s
							int_abundance[3,sp_id] += 1
							cnt2 += 1
						elif TL[tl_id]==3:
							top_abundance[1,sp_id] += s
							top_abundance[3,sp_id] += 1
							cnt3 += 1

					tl_id += 1

				
				sdev0.append(cnt0)	
				sdev1.append(cnt1)	
				sdev2.append(cnt2)	
				sdev3.append(cnt3)	
				sdevT.append(cnt0 + cnt1 + cnt2 + cnt3)	
				rep_count += 1

			except:
				print('whoops ' + d)

			os.chdir('..')			
			#if rep_count>=22:
		#		break

	sd0.append(np.std(sdev0))
	sd1.append(np.std(sdev1))
	sd2.append(np.std(sdev2))
	sd3.append(np.std(sdev3))
	sdT.append(np.std(sdevT))


	total_abundance[1,sp_id] = float(total_abundance[1,sp_id])/float(rep_count)
	total_abundance[3,sp_id] = float(total_abundance[3,sp_id])/float(rep_count)

	basal_abundance[1,sp_id] = float(basal_abundance[1,sp_id])/float(rep_count)
	basal_abundance[3,sp_id] = float(basal_abundance[3,sp_id])/float(rep_count)

	herb_abundance[1,sp_id] = float(herb_abundance[1,sp_id])/float(rep_count)
	herb_abundance[3,sp_id] = float(herb_abundance[3,sp_id])/float(rep_count)

	int_abundance[1,sp_id] = float(int_abundance[1,sp_id])/float(rep_count)
	int_abundance[3,sp_id] = float(int_abundance[3,sp_id])/float(rep_count)

	top_abundance[1,sp_id] = float(top_abundance[1,sp_id])/float(rep_count)
	top_abundance[3,sp_id] = float(top_abundance[3,sp_id])/float(rep_count)
	print(str(rep_count) + " repeats")
	
	os.chdir('..')
	sp_id += 1


print(sdT)
#plt.plot(total_abundance[0,:], total_abundance[3,:], 'ko-')
plt.errorbar(total_abundance[0,:], total_abundance[3,:], yerr=sdT, fmt='ko-')
plt.errorbar(basal_abundance[0,:], basal_abundance[3,:], fmt='go--', yerr=sd0)
plt.errorbar(herb_abundance[0,:], herb_abundance[3,:], fmt='bo--', yerr=sd1)
plt.errorbar(int_abundance[0,:], int_abundance[3,:], fmt='yo--', yerr=sd2)
plt.errorbar(top_abundance[0,:], top_abundance[3,:], fmt='ro--', yerr=sd3)

plt.legend(['All TL', 'TL = 0', 'TL = 1', 'TL = 2', 'TL = 3'], loc=2)

plt.xlabel('landscape size', fontsize=fs)
plt.ylabel('number of persistent species', fontsize=fs)
#plt.title('MAI = 0.5  Niche web.', fontsize=fs)
plt.ylim([0,35])
plt.grid()
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
#plt.savefig('numsp_v_composition_mut05_niche.png')
plt.show()
