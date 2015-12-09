from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#fig, axes = plt.subplots(2,2, figsize=(10,6))
#AX = axes.flatten()
#dir = '../network_7_highIM/'
dir = './'

fsa = 15
#leg = ['TL1', 'TL2', 'TL3', 'TL4']

pops = np.genfromtxt(dir + 'output_pops_long.csv', delimiter=',')
sps = np.genfromtxt(dir + 'output_species_long.csv', delimiter=',', skip_header=1)

#pops = np.genfromtxt(dir + 'output_pops.csv', delimiter=',')
#sps = np.genfromtxt(dir + 'output_species.csv', delimiter=',', skip_header=1)

tls = sps[:,1]
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
print(tls)

pops0 = pops[:,tls==0]
pops1 = pops[:,tls==1]
pops2 = pops[:,tls==2]
pops3 = pops[:,tls==3]

abun = dict()
for i in range(60):
	abun[np.mean(pops[2000:,i])] = i+1

sor = sorted(abun.items())
print(sorted(abun.items()))

print("%d : %d" %(sor[-1][1],tls[sor[-1][1]-1]))
print("%d : %d" %(sor[-2][1],tls[sor[-2][1]-1]))
print("%d : %d" %(sor[-3][1],tls[sor[-3][1]-1]))
print("%d : %d" %(sor[-4][1],tls[sor[-4][1]-1]))
print("%d : %d" %(sor[-5][1],tls[sor[-5][1]-1]))

print('least abundant...')
print("%d : %d" %(sor[0][1],tls[sor[0][1]-1]))
print("%d : %d" %(sor[1][1],tls[sor[1][1]-1]))
print("%d : %d" %(sor[2][1],tls[sor[2][1]-1]))
print("%d : %d" %(sor[3][1],tls[sor[3][1]-1]))
print("%d : %d" %(sor[4][1],tls[sor[4][1]-1]))

print(sor[:][1])


#3d plot test:
#st = 1000
#en = 10000
#fig = plt.figure()
#ax = fig.add_subplot(121, projection='3d')
#ax.plot(pops[st:en,sor[-1][1]-1], pops[st:en,sor[-2][1]-1],pops[st:en,sor[-3][1]-1])
#ax = fig.add_subplot(122)
#ax.plot(pops[st:en,sor[-1][1]-1], pops[st:en,sor[-2][1]-1])
#plt.show()
#

## now lets apply the moving average window
wl = 4000
en = 10000 - wl

ma0id = sor[-1][1]-1
ma1id = sor[-2][1]-1
ma2id = sor[-3][1]-1

la0id = sor[0][1]-1
la1id = sor[1][1]-1
la2id = sor[2][1]-1

t = []
ma0 = []
ma1 = []
ma2 = []
la0 = []
la1 = []
la2 = []

for i in range(en):
	t.append((i+wl)/2.0)
	ma0.append(np.mean(pops[i:i+wl,ma0id]))	
	ma1.append(np.mean(pops[i:i+wl,ma1id]))	
	ma2.append(np.mean(pops[i:i+wl,ma2id]))	
	la0.append(np.mean(pops[i:i+wl,la0id]))	
	la1.append(np.mean(pops[i:i+wl,la1id]))	
	la2.append(np.mean(pops[i:i+wl,la2id]))	

fig,axes = plt.subplots(1,2,figsize=(12,6), sharey=False)
AX= axes.flatten()
AX[0].plot(t,ma0)
AX[0].plot(t,ma1, 'g')
AX[0].plot(t,ma2, 'r')
AX[0].set_xlabel('iterations')
AX[0].set_ylabel('individuals')
AX[0].legend(['most abundant species (TL1)', 'second species (TL2)', 'third species (TL3)'])
AX[0].grid()
#AX[0].set_ylim([0,10000])
#plt.plot(pops[0:10000,19])
AX[1].plot(pops[0:en,sor[0][1]-1])
AX[1].plot(pops[0:en,sor[1][1]-1],'g')
AX[1].plot(pops[0:en,sor[2][1]-1],'r')
AX[1].set_xlabel('iterations')
AX[1].legend(['least abundant species (TL1)', 'second species (TL2)', 'third species (TL3)'])
AX[1].grid()
AX[1].set_ylim([0,150])
#plt.ylim([0,10000])
plt.show()
