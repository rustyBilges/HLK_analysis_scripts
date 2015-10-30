## methods to use for steady state analysis

import numpy as np
import matplotlib.pyplot as plt

def return_basic_stats(series):
	"""Simply takes a biomass timeseries and returns the basic stats: mean and variance (more to follow?)"""
	return (np.mean(series), np.std(series))

def stats_at_discrete_times(series, times, window_length, print_flag=False):
	"""Calculates stats at discrete times from series, using windows of given length"""
	if times[-1]+window_length > len(series):
		print("Cannot use these times, they exceed length of series")
		return 0

	return_value = np.zeros((len(times),2))
	t_id = 0
	for t in times:
		sub_series = series[t : t+window_length]

		mean, std = return_basic_stats(sub_series)	
		return_value[t_id,0] = mean
		return_value[t_id,1] = std
		t_id += 1

	if print_flag:
		print(return_value)

	return return_value


def plot_state_and_stats(series, times, window_length):
	"""Plot method"""

	fig, axes = plt.subplots(1,3)
	AX = axes.flatten()
	
	AX[0].plot(series)

	res = stats_at_discrete_times(series, times, window_length)
	AX[1].plot(res[:,0])
	AX[1].axhline(np.mean(series[1000:-1]))
	AX[2].plot(res[:,1])
	AX[2].axhline(np.std(series[1000:-1]))
	plt.show()

def compare_plot_state_and_stats(series1, series2, times, window_length):
        """Plot method"""

        fig, axes = plt.subplots(1,3, figsize=(13,5))
        AX = axes.flatten()

        AX[0].plot(series1, 'g')
        AX[0].plot(series2, 'r')
	AX[0].legend(['low IR', 'high IR'])
	AX[0].set_xlabel('iteration')
	AX[0].set_ylabel('total biomass')

        res1 = stats_at_discrete_times(series1, times, window_length)
        res2 = stats_at_discrete_times(series2, times, window_length)

        AX[1].plot(np.asarray(times) + (window_length/2), res1[:,0], 'go')
        AX[1].plot(np.asarray(times) + (window_length/2), res2[:,0], 'ro')
        AX[1].axhline(np.mean(series1[1000:-1]), color='g')
        AX[1].axhline(np.mean(series2[1000:-1]), color='r')

	AX[1].set_xlabel('iteration')
	AX[1].set_ylabel('mean biomass around iteration')

        AX[2].axhline(np.std(series1[1000:-1]), color='g')
        AX[2].axhline(np.std(series2[1000:-1]), color='r')
        AX[2].plot(np.asarray(times) + (window_length/2), res1[:,1], 'go')
        AX[2].plot(np.asarray(times) + (window_length/2), res2[:,1], 'ro')
	AX[2].set_xlabel('iteration')
	AX[2].set_ylabel('stdev in biomass around iteration')
	plt.subplots_adjust(wspace=0.5)
        plt.show()

