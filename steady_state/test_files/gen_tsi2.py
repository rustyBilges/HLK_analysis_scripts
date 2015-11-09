import numpy as np


t = range(50000)

t = np.asarray(t)*0.0001

y = []

me = 0 #np.mean(y)
st = 0 #np.std(y)

for i in t:
	r = np.random.normal(15915, 1545 )
	y.append(r)


#print(t[0:10])
#y = 1+  np.sin(t)
#print(y[0:10])

print(np.mean(y))
print(np.std(y))

np.savetxt("correlated_series.csv", y, delimiter=',')
