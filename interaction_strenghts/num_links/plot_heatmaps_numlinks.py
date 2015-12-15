import matplotlib.pyplot as plt
import numpy as np

rows = 1
cols = 3

ytix_loc = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
xtix_loc = [0.5, 2.5, 4.5, 6.5, 8.5]
ytix = [0.0001,0.0002, 0.0003, 0.0004, 0.0005, 0.001, 0.002, 0.003, 0.004, 0.005]
xtix = [0,20,40,60,80, 100]

YY = np.log10(np.asarray([0.00005, 0.00015, 0.00025, 0.00035, 0.00045, 0.00055, 0.0015, 0.0025, 0.0035, 0.0045, 0.0055]))
XX = np.asarray( [0,10,20,30,40,50,60,70,80,90,100])

rect = 0.1,0.1,0.9,0.8
fig = plt.figure(figsize=(20,6))
ax = fig.add_axes(rect)
#cov = np.genfromtxt("cov_map.csv", delimiter=',')

e_min = 0
e_max = 270
a_min = 0
a_max = 55000
c_min = 0
c_max = 0.08

fs = 16 # font size
fsa = 18 # font size for annotation

#cov = cov[4:,:]
subd = './'
###################################################################################################
## EXTINCTIONS          
aa = plt.subplot(rows, cols,1)
ext = np.genfromtxt(subd + "mean_numlinks_map_mai0.csv", delimiter=',')
#im = plt.pcolor(ext)
im = plt.pcolor(ext, vmin=e_min, vmax=e_max)
#im = plt.pcolor(XX,YY,ext)

plt.ylabel("immigration", size=fsa)
plt.xlabel("habitat destruction", size=fs)
#ax.set_yticklabels([0.0001,0.0005,0.001, 0.002,0.003,0.004,0.005])
aa.set_xticks(xtix_loc)
aa.set_yticks(ytix_loc)
aa.set_yticklabels(ytix)
aa.set_xticklabels(xtix)
aa.annotate("A", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')
plt.title('MAI = 0.0', fontsize=fsa)
plt.colorbar(im)
###################################################################################################
## EXTINCTIONS          
aa = plt.subplot(rows, cols,2)
ext = np.genfromtxt(subd + "mean_numlinks_map_mai0.5.csv", delimiter=',')
#im = plt.pcolor(ext)
im = plt.pcolor(ext, vmin=e_min, vmax=e_max)
#im = plt.pcolor(XX,YY,ext)

#plt.ylabel("immigration", size=fs)
plt.xlabel("habitat destruction", size=fs)
#ax.set_yticklabels([0.0001,0.0005,0.001, 0.002,0.003,0.004,0.005])
aa.set_xticks(xtix_loc)
aa.set_yticks(ytix_loc)
aa.set_yticklabels(ytix)
aa.set_xticklabels(xtix)
#aa.annotate("MAI = 0.0", xy=(0.0, 0.5), size='x-large', ha='right', va='center', xytext= (-3, 5))#(-ax.yaxis.labelpad - pad, 0),xycoords=ax.yaxis.label, textcoords='offset points'
aa.annotate("B", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')
#plt.title('Mean number of extinctions')
plt.title('MAI = 0.5', fontsize=fsa)
plt.colorbar(im)

###################################################################################################
## EXTINCTIONS          
aa = plt.subplot(rows, cols,3)
ext = np.genfromtxt(subd + "mean_numlinks_map_mai1.0.csv", delimiter=',')
#im = plt.pcolor(ext)
im = plt.pcolor(ext, vmin=e_min, vmax=e_max)
#im = plt.pcolor(XX,YY,ext)

plt.xlabel("habitat destruction", size=fs)
#ax.set_yticklabels([0.0001,0.0005,0.001, 0.002,0.003,0.004,0.005])
aa.set_xticks(xtix_loc)
aa.set_yticks(ytix_loc)
aa.set_yticklabels(ytix)
aa.set_xticklabels(xtix)
aa.annotate("C", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')
plt.title('MAI = 1.0', fontsize=fsa)
plt.colorbar(im)


plt.tight_layout()
plt.show()
