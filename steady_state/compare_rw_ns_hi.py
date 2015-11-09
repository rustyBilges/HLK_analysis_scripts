import numpy as np
import matplotlib.pyplot as plt
from ss_utilities import stats_at_discrete_times, compare_plot_state_and_stats, plot_state_and_stats, plot_zscore
from ss_utilities import  _autocorr, stats_at_discrete_times

plot_dynamics = False
plot_corr = False
plot_zscore = False
plot_fft = True

pops1 = np.genfromtxt("test_files/highIM/output_pops_long.csv", delimiter=',')
#pops1 = np.genfromtxt("test_files/lowIM/output_pops_long.csv", delimiter=',')
#pops1 = np.genfromtxt("test_files/lowIM/output_pops.csv", delimiter=',')
#pops2 = np.genfromtxt("test_files/highIM/output_pops.csv", delimiter=',')

hi = np.sum(pops1,1)
rw = np.genfromtxt("test_files/random_walk.csv", delimiter=',')
ns = np.genfromtxt("test_files/normal_series.csv", delimiter=',')

hi = hi[1000:-1]
rw = rw[1000:-1]
ns = ns[1000:-1]

hi_corr = _autocorr(hi)
rw_corr = _autocorr(rw)
ns_corr = _autocorr(ns)


if plot_corr:

	plt.plot(hi_corr, 'r', label='IBM simulation (high IR)')
	plt.plot(rw_corr, 'g', label='random walk')
	plt.plot(ns_corr, 'b', label='normal distribution')
	plt.legend()
	plt.grid()
	plt.xlabel('lag')
	plt.ylabel('autocorreltaion at lag')
	plt.show()

if plot_dynamics:

	fig,axes = plt.subplots(3,1,figsize=(10,6))

	AX = axes.flatten()

	AX[0].plot(hi, 'r', label= 'IBM simulation (high IR)')
	AX[0].set_ylabel('abundance')
	AX[0].grid()
	AX[0].set_ylim([8000,26000])
	AX[0].set_title('IBM simulation (high IR)')
	AX[1].plot(rw, 'g', label= 'random walk')
	AX[1].set_ylabel('abundance')
	AX[1].grid()
	AX[1].set_ylim([8000,26000])
	AX[1].set_title('random walk')
	AX[2].plot(ns, 'b', label= 'normal distribution')
	AX[2].set_ylim([8000,26000])
	AX[2].set_title('normal distribution')
	AX[2].set_xlabel('iterations')
	AX[2].set_ylabel('abundance')
	AX[2].grid()
	#plt.legend()
	plt.tight_layout()
	plt.show()


def z_score(series, times, window_length):

        mu = np.mean(series)
        sig = np.std(series)
        SE = sig / np.sqrt(window_length)

        res = stats_at_discrete_times(series, times, window_length)
        zsc = []
        for r in res[:,0]:
                zsc.append( (r-mu)/SE )
	return zsc

if plot_zscore:



	fig,axes = plt.subplots(3,1,figsize=(10,6))

	AX = axes.flatten()


 	zhi = z_score(hi, range(1000,47000,100), 1000)
	AX[0].plot( range(1000,47000,100), zhi, 'ro')
	AX[0].axhline(1.96)
	AX[0].axhline(-1.96)
	
	cnt = np.ones(len(zhi))
	count = np.sum(cnt[np.abs(zhi)>1.96])
	AX[0].set_title("IBM simulation (high IR) \n reject h0 = %d out of %d" %(count, len(zhi)))
	AX[0].grid()
	AX[0].set_ylabel("z-score")

 	zrw = z_score(rw, range(1000,47000,100), 1000)
	AX[1].plot(zrw, 'go')
	AX[1].axhline(1.96)
	AX[1].axhline(-1.96)
	
	cnt = np.ones(len(zrw))
	count = np.sum(cnt[np.abs(zrw)>1.96])
	AX[1].set_title("Random walk \n reject h0 = %d out of %d" %(count, len(zhi)))

	AX[1].grid()
	AX[1].set_ylabel("z-score")

 	zns = z_score(ns, range(1000,47000,100), 1000)
	AX[2].plot(zns, 'bo')
	AX[2].axhline(1.96)
	AX[2].axhline(-1.96)
	
	cnt = np.ones(len(zns))
	count = np.sum(cnt[np.abs(zns)>1.96])
	AX[2].set_title("Normal distribution \n reject h0 = %d out of %d" %(count, len(zhi)))

	AX[2].grid()
	AX[2].set_xlabel("iteration")
	AX[2].set_ylabel("z-score")

	plt.tight_layout()
	plt.show()

if plot_fft:

	fig,axes = plt.subplots(3,1,figsize=(10,6))

	AX = axes.flatten()


 	zhi = np.fft.rfft(hi) #z_score(hi, range(1000,47000,100), 1000)
	zhi[0] = 0
	AX[0].plot( np.abs(zhi), 'r')
	#AX[0].axhline(1.96)
	#AX[0].axhline(-1.96)
	
	cnt = np.ones(len(zhi))
	count = np.sum(cnt[np.abs(zhi)>1.96])
	AX[0].set_title("IBM simulation (high IR) \n reject h0 = %d out of %d" %(count, len(zhi)))
	AX[0].grid()
	AX[0].set_ylabel("power")


 	zhi = np.fft.rfft(rw) #z_score(hi, range(1000,47000,100), 1000)
	zhi[0] = 0
	AX[1].plot( np.abs(zhi), 'b')
	#AX[0].axhline(1.96)
	#AX[0].axhline(-1.96)
	
	cnt = np.ones(len(zhi))
	count = np.sum(cnt[np.abs(zhi)>1.96])
	AX[1].set_title("IBM simulation (high IR) \n reject h0 = %d out of %d" %(count, len(zhi)))
	AX[1].grid()
	AX[1].set_ylabel("power")


 	zhi = np.fft.rfft(ns) #z_score(hi, range(1000,47000,100), 1000)
	zhi[0] = 0
	AX[2].plot( np.abs(zhi), 'g')
	#AX[0].axhline(1.96)
	#AX[0].axhline(-1.96)
	
	cnt = np.ones(len(zhi))
	count = np.sum(cnt[np.abs(zhi)>1.96])
	AX[2].set_title("IBM simulation (high IR) \n reject h0 = %d out of %d" %(count, len(zhi)))
	AX[2].grid()
	AX[2].set_ylabel("z-score")


	plt.tight_layout()
	plt.show()
        #fig, axes = plt.subplots(1,4)
        #AX = axes.flatten()

        #AX[0].plot(np.abs(zsc))
        #AX[0].axhline(1.96)



#biomass1 = np.genfromtxt("test_files/normal_series.csv", delimiter=',')
#biomass2 = np.sum(pops2,1)
#print(np.shape(biomass))

#stats_at_discrete_times(biomass, [1000, 5000, 40000], 1000, print_flag=True)

#compare_plot_state_and_stats(biomass1, biomass2, range(1000, 4000, 100), 1000)

#plot_state_and_stats(biomass, range(1000,4000,100), 1000)
#plot_state_and_stats(biomass1, range(1000,47000,100), 3000)
#plot_zscore(biomass1, range(1000,47000,100), 1000)

#print(np.mean(biomass1[1000:-1]))
#print(np.std(biomass1[1000:-1]))

#plot_state_and_stats(biomass1, range(1000,47000,100), 1000)
