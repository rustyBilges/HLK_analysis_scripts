
## plotting trophic dynamics for a range of parameter values....

import numpy as np
import matplotlib.pyplot as plt
import os

type = 'rr'  ## either plot results from mai_v_persistence OR rr_v_persistence simulation runs.

mut_for_rr = '0/'  ## only used to select mai ratio used in rr simulations

if type == 'mut':
        base_dir = "/MyFiles/cm1788/Documents/parameter_fiddling/bc3_results/mai_v_persistence/"
        dir_Ext = 'mut_'
	m_range = [0, 0.3, 0.6, 0.9]
	muts = ['0', '.3', '.6', '.9']
        xlab = 'MAI ratio = '
if type == 'rr':
        base_dir = "/MyFiles/cm1788/Documents/parameter_fiddling/bc3_results/rr_v_persistence/mut_" + mut_for_rr 
        dir_Ext = 'rr_'
        m_range = [0.01,  0.07, 0.13, 0.19]
	muts = ['0.01', '0.07', '0.13', '0.19']
        xlab = 'rep. rate = '


n_plots = len(m_range)
n_rows = np.ceil(n_plots/2.0)
#print(n_rows)

p_id = 1
panel = ['(A) ', '(B) ', '(C) ', '(D) ']
mut_id = 0
offset = 1   # 1-> plot abundances, 0-> plot richness

labels = ['producer', 'mutualist producer', 'herbivore', 'mutualist animal', 'primary predator', 'top predator']
lines = []

for mai in m_range:

	# store results:		
	results = np.zeros((5001, 6))
	
	dir_name = base_dir + dir_Ext + muts[mut_id]
	os.chdir(dir_name)
	rep_dirs = os.listdir('.')

	rep_count = 0
	for d in rep_dirs:
		if d!='src':
			os.chdir(d)
			try:
				eco = np.genfromtxt('output_ecosystem.csv', delimiter=',', skip_header=1)	
				results[:,0] += eco[:,3 + offset]
				results[:,1] += eco[:,5 + offset]
				results[:,2] += eco[:,7 + offset]
				results[:,3] += eco[:,9 + offset]
				results[:,4] += eco[:,11 + offset]
				results[:,5] += eco[:,13 + offset]
				rep_count += 1
			except:
				print('whoops' + d)

			os.chdir('..')

	results /= rep_count

	plt.subplot(n_rows, 2, p_id)
	l1 = plt.plot(results[:,0], label='producer')
	l2 = plt.plot(results[:,1], label='mutualist-prodcuer')
	l3 = plt.plot(results[:,2], label='herbivore')
	l4 = plt.plot(results[:,3], label='mutualist-animal')
	l5 = plt.plot(results[:,4], label = 'omnivore')
	l6 = plt.plot(results[:,5], label = 'top predator')
	plt.ylabel('number of individuals')
	plt.title(panel[p_id - 1] + xlab + str(mai))
	plt.ylim([0, 40000])
	plt.grid()

	if p_id ==1:
		#plt.legend(['producer', 'mutualist producer', 'herbivore', 'mutualist animal', 'primary predator', 'top predator'], fontsize=10)
		#lines.append(l1)
		#lines.append(l2)
		##lines.append(l3)
		#lines.append(l4)
		#lines.append(l5)
		#lines.append(l6)
		#lines = (l1,l2,l3,l4,l5,l6)
		ax = plt.gca()
		h, l = ax.get_legend_handles_labels()
	if p_id == 3 or p_id == 4:
		plt.xlabel('iterations')

	os.chdir('..')
	mut_id += 1
	p_id += 1

	#fname = base_dir + "output_ecosystem_%f.csv" %p

	#try:
		#eco = np.genfromtxt(fname, delimiter=',', skip_header=1)

		#print(np.shape(eco))

		#plt.subplot(2, n_rows, p_id)
		#plt.ylim([0,60])
		#plt.plot(eco[:,0], eco[:, 3 + offset])
		#plt.plot(eco[:,0], eco[:, 5 + offset])
		#plt.plot(eco[:,0], eco[:, 7 + offset])
		#plt.plot(eco[:,0], eco[:, 9 + offset])
		#plt.plot(eco[:,0], eco[:, 11 + offset])
		#plt.plot(eco[:,0], eco[:, 13 + offset])

		#if p_id == 1:
	#		plt.legend(['prod', 'mut_prod', 'herb', 'mut_sp', 'prim_pred', 'sec_pred'])

	#except:
	#	print("Whoops")

#	p_id += 1
plt.subplots_adjust(bottom=0.2, wspace = 0.5, hspace = 0.5)
plt.figlegend( h, l,  loc = 'lower center', ncol=3, labelspacing=0. )
#plt.tight_layout()
#plt.savefig("mean_trophic_dynamics")
plt.show()
