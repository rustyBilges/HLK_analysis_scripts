import numpy as np


t = range(50000)

t = np.asarray(t)*0.0001


me = 0 #np.mean(y)
st = 0 #np.std(y)

def test(m, s):

	if m < 15000:
		return False
	if m > 16500:
		return False
	if s < 1500:
		return False
	if s > 1650:
		return False

	return True

while not test(me,st):

	y = []
	y0 = 15915 #100
	y.append(y0)

	for i in t:
		r = np.random.uniform()
		if r<= 0.5:
			y0 -= 50
		else:
			y0 += 50
		y.append(y0)

	me = np.mean(y)
	st = np.std(y)

	
#	y.append(r+1)


#print(t[0:10])
#y = 1+  np.sin(t)
#print(y[0:10])

print(np.mean(y))
print(np.std(y))

np.savetxt("correlated_series.csv", y, delimiter=',')
