## script to plot the performance of statistical tests (ADF and KPSS) versus length of window. 
## calcuations were originally conducted in R using the time series highIM/output_pos_long (see notes.txt therein)

import matplotlib.pyplot as plt
import numpy as np

fsa = 15

res = np.genfromtxt('stat_tests_v_length_hi_long.csv', delimiter=',')
res_rw = np.genfromtxt('stat_tests_v_length_rw_long.csv', delimiter=',')
res_ns = np.genfromtxt('stat_tests_v_length_ns_long.csv', delimiter=',')

lens = np.copy(res[:,0])
res[res>0.2] = 0.2
res_rw[res_rw>0.2] = 0.2
res_ns[res_ns>0.2] = 0.2

fig, axes = plt.subplots(2,1, figsize=(10,6))
AX = axes.flatten()

AX[0].plot(lens, res[:,2], 'o', fillstyle='none')
AX[0].plot(lens, res_rw[:,2], '+')
AX[0].plot(lens, res_ns[:,2], 'v', fillstyle='none')
AX[0].legend(['HI', 'RW', 'NS'])
AX[0].fill_between(range(50000), 0, 0.012, color='green', alpha=0.4)
AX[0].fill_between(range(50000), 0.012, 0.052, color='yellow', alpha=0.4)
#AX[0].axhline(0.01)
AX[0].set_xlim([0.00,50000])
AX[0].set_ylim([0.00,0.25])
AX[0].grid()
AX[0].set_ylabel('p-value (ADF test)', fontsize=fsa)
AX[0].annotate("A", (0,0), (0.02,0.9), color='black', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')


AX[1].plot(lens, res[:,4], 'o', fillstyle='none')
AX[1].plot(lens, res_rw[:,4], '+')
AX[1].plot(lens, res_ns[:,4], 'v', fillstyle='none')
#AX[1].legend(['HI', 'RW', 'NS'])
AX[1].fill_between(range(50000), 0, 0.012, color='red', alpha=0.4)
AX[1].fill_between(range(50000), 0.012, 0.052, color='orange', alpha=0.4)
AX[1].set_xlim([0.00,50000])
AX[1].set_ylim([0.00,0.12])
AX[1].grid()
AX[1].set_xlabel('window length (iterations)', fontsize=fsa)
AX[1].set_ylabel('p-value (KPSS test)', fontsize=fsa)
AX[1].annotate("B", (0,0), (0.02,0.9), color='black', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')

plt.tight_layout()
plt.show()
