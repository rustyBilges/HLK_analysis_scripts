import matplotlib.pyplot as plt
import numpy as np


mean = np.genfromtxt('compare_mean.csv', delimiter=',')
ids = np.genfromtxt('compare_mean_ids.csv', delimiter=',')


l_means = dict()
ii = 0
for i in ids[0,:]:
	l_means[i] = mean[0,ii]
	ii +=1

h_means = dict()
ii = 0
for i in ids[1,:]:
	h_means[i] = mean[1,ii]
	ii +=1

print(np.mean(mean[0,:]))
print(np.mean(mean[1,:]))


print(h_means)

plt.plot(mean[0,:], mean[1,:], 'o')
#plt.plot(mean[0,:], mean[1,:], 'o')
plt.xlabel('simulation mean for low IR')
plt.ylabel('simulation mean for high IR')
#
a,b = plt.xlim()
plt.plot([a,b], [a,b], 'k')
plt.show()


