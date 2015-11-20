## script to plot the performance of statistical tests (ADF and KPSS) versus length of window. 
## calcuations were originally conducted in R using the time series highIM/output_pos_long (see notes.txt therein)

import matplotlib.pyplot as plt
import numpy as np

fsa = 15

res1 = np.genfromtxt('tl0_stat_tests_v_length_hi_long.csv', delimiter=',')
res2 = np.genfromtxt('tl1_stat_tests_v_length_hi_long.csv', delimiter=',')
res3 = np.genfromtxt('tl2_stat_tests_v_length_hi_long.csv', delimiter=',')
res4 = np.genfromtxt('tl3_stat_tests_v_length_hi_long.csv', delimiter=',')

lens = np.copy(res1[:,0])
res1[res1>0.2] = 0.2
res2[res2>0.2] = 0.2
res3[res3>0.2] = 0.2
res4[res4>0.2] = 0.2

fig, axes = plt.subplots(2,1, figsize=(10,6))
AX = axes.flatten()

AX[0].plot(lens, res1[:,2], 'o', fillstyle='none')
AX[0].plot(lens, res2[:,2], '+')
AX[0].plot(lens, res3[:,2], 'v', fillstyle='none')
AX[0].plot(lens, res4[:,2], '^', fillstyle='none')

AX[0].legend(['TL 1', 'TL 2', 'TL 3', 'TL 4'])

AX[0].fill_between(range(50000), 0, 0.012, color='green', alpha=0.4)
AX[0].fill_between(range(50000), 0.012, 0.052, color='yellow', alpha=0.4)
#AX[0].axhline(0.01)
AX[0].set_xlim([0.00,50000])
AX[0].set_ylim([0.00,0.25])
AX[0].grid()
AX[0].set_ylabel('p-value (ADF test)', fontsize=fsa)
AX[0].annotate("A", (0,0), (0.02,0.9), color='black', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')


AX[1].plot(lens, res1[:,4], 'o', fillstyle='none')
AX[1].plot(lens, res2[:,4], '+')
AX[1].plot(lens, res3[:,4], 'v', fillstyle='none')
AX[1].plot(lens, res4[:,4], '^', fillstyle='none')
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
