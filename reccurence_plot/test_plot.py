import numpy as np
import matplotlib.pyplot as plt

epsilon = 1000  ## threshold for heaviside function

length = 1000

#f = "../steady_state/test_files/highIM/output_pops_long.csv"
f = "../steady_state/test_files/lowIM/output_pops_long.csv"
pops = np.genfromtxt(f, delimiter=',')

new_pops = pops[1000:,:]
pops = []
for i in range(length):
	pops.append(new_pops[i*10,:])

pops = np.asarray(pops)

check = np.sqrt(np.sum(pops**2,1))
plt.plot(check)
plt.show()


#pops = pops[-length:,:]

def norm(v1,v2):

	if len(v1)!=len(v2):
		print("warning: vectors not same length")
		return 0

	#res = 0

	#for i in range(len(v1)):
	#	res += (v2[i] - v1[i])**2

	return np.sqrt(np.sum((v2-v1)**2))  #np.sqrt(res)


mp = np.zeros((length,length))


for i in range(length):
	print(i)
	for j in range(length):
		#mp[i,j] = norm(pops[i,:], pops[j,:])
		if  norm(pops[i,:], pops[j,:]) <= epsilon:
			mp[i,j] = 1


#plt.pcolor(mp)
#plt.colorbar()
plt.imshow(mp)
plt.show()
		
