import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2,2, figsize=(10,6))
AX = axes.flatten()
dir = '../network_7_highIM/'

fsa = 15
#leg = ['TL1', 'TL2', 'TL3', 'TL4']

#pops = np.genfromtxt(dir + 'output_pops_long.csv', delimiter=',')
#sps = np.genfromtxt(dir + 'output_species.csv', delimiter=',', skip_header=1)

pops = np.genfromtxt(dir + 'output_pops.csv', delimiter=',')
sps = np.genfromtxt(dir + 'output_species.csv', delimiter=',', skip_header=1)
#tls = sps[:,1]
#tls = sps3[:,1]
tls = dict()
ii = 0
tlss = sps[:,1]
ids = sps[:,0]
for i in ids:
        tls[i] = tlss[ii]
        ii+=1

sor = sorted(tls.items())
tls = []
ids = []
for s in sor:
        tls.append(s[1])
        ids.append(s[0])
tls = np.asarray(tls)


print(np.shape(pops))
print(tls==2)
pops0 = pops[:,tls==0]
pops1 = pops[:,tls==1]
pops2 = pops[:,tls==2]
pops3 = pops[:,tls==3]

biomass = np.sum(pops,1)

#plt.subplot(1,2,1)
plt_to = 10000
for i in range(np.shape(pops0)[1]):

	AX[0].plot(pops0[0:plt_to,i])
	AX[0].set_xlabel("iteration", fontsize=fsa)
	AX[0].set_ylabel("total abundance", fontsize=fsa)
	AX[0].set_ylim([0,5000])
	#AX[0].legend(leg)
	AX[0].set_title("(A) TL 1", fontsize=fsa)
#dir = 'IM_0.0001/'

for i in range(np.shape(pops1)[1]):

	AX[1].plot(pops1[0:plt_to,i])
	AX[1].set_xlabel("iteration", fontsize=fsa)
	AX[1].set_ylabel("total abundance", fontsize=fsa)
	AX[1].set_ylim([0,5000])
	#AX[0].legend(leg)
	AX[1].set_title("(B) TL 2")
for i in range(np.shape(pops2)[1]):

	AX[2].plot(pops2[0:plt_to,i])
	AX[2].set_xlabel("iteration", fontsize=fsa)
	AX[2].set_ylabel("total abundance", fontsize=fsa)
	AX[2].set_ylim([0,5000])
	#AX[0].legend(leg)
	AX[2].set_title("(C) TL 3", fontsize=fsa)
for i in range(np.shape(pops3)[1]):

	AX[3].plot(pops3[0:plt_to,i])
	AX[3].set_xlabel("iteration", fontsize=fsa)
	AX[3].set_ylabel("total abundance", fontsize=fsa)
	AX[3].set_ylim([0,5000])
	#AX[0].legend(leg)
	AX[3].set_title("(D) TL 4", fontsize=fsa)
#ent = 1000
AX[0].grid()
AX[1].grid()
AX[2].grid()
AX[3].grid()
#AX[1].plot(pops0[0:ent], 'g')
#AX[1].plot(pops1[0:ent], 'y')
#AX[1].plot(pops2[0:ent], 'b')
#AX[1].plot(pops3[0:ent], 'r')
#AX[1].plot(biomass[0:ent], 'k')
#AX[1].set_xlabel("iteration")
#AX[1].set_ylabel("total abundance")
#AX[1].set_ylim([0,40000])
#AX[1].grid()
#AX[1].legend(leg)
#AX[1].set_title("transience")


#pops = np.genfromtxt(dir + 'output_pops.csv', delimiter=',')
#pops = np.genfromtxt(dir + 'output_pops2.csv', delimiter=',')
#pops = np.genfromtxt(dir + 'output_pops3.csv', delimiter=',')

#sps = np.genfromtxt(dir + 'output_species.csv', delimiter=',', skip_header=1)
#sps2 = np.genfromtxt(dir + 'output_species2.csv', delimiter=',', skip_header=1)
#sps3 = np.genfromtxt(dir + 'output_species3.csv', delimiter=',', skip_header=1)

#tls = sps[:,1]
#tls = sps2[:,1]
#tls = sps3[:,1]
#
#pops0 = np.sum(pops[:,tls==0], 1)
#pops1 = np.sum(pops[:,tls==1], 1)
#pops2 = np.sum(pops[:,tls==2], 1)
#pops3 = np.sum(pops[:,tls==3], 1)

#plt.subplot(1,2,2)
#AX[1].plot(pops0, 'g')
#AX[1].plot(pops1, 'y')
#AX[1].plot(pops2, 'b')
#AX[1].plot(pops3, 'r')
#AX[1].set_xlabel("iteration")
#AX[1].set_ylim([0,40000])
#AX[1].legend(leg)
#AX[1].set_title("Immigration = 0.0001")

plt.tight_layout()
plt.show()
                                                                                                                                                               

