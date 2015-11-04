## this class produces rank abundance distributions

import numpy as np
import matplotlib.pyplot as plt   ## comment out for use on BC3
import matplotlib as mpl
import operator
import math
import itertools

from rad_calculator import Rad_calculator

class Rad_plotter:

	def __init__(self, save_flag=True, save_name='./rad_plot'):
		self.save_flag = save_flag
		self.save_name = save_name

		self.distribution = None	

        def single_plot(self, dist):

			self.distribution = dist     
                        # setup the plot
                        fig, ax = plt.subplots(1,1, figsize=(6,6))
			
                        cmap = plt.cm.jet
                        cmaplist = [(.0,1.0,.0,1.0), (.0,.0,1.0,1.0), (1.0,1.0,.0,1.0), (1.0,.0,.0,1.0)]
                        cmap = cmap.from_list('Custom cmap', cmaplist, 4)

                        bounds = np.linspace(0,4,5)
                        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

                        sc = plt.scatter(self.distribution[0,:], self.distribution[1,:], c = self.distribution[2,:], vmin = 0, vmax = 3, cmap=cmap)# cmap = ['green', 'blue', 'yellow', 'red'])

                        # create a second axes for the colorbar
                        plt.subplots_adjust(left=0.10, right=0.85)
                        ax2 = fig.add_axes([0.9, 0.1, 0.03, 0.8])
                        cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, spacing='proportional', ticks=bounds+0.5, boundaries=bounds, format='%1i')

                        ax.set_title('Rank abundance distribution')
                        ax.set_xlabel('rank')
                        ax.set_ylabel('log abundance')
                        ax2.set_ylabel('Species trophic level', size=12)

                        if self.save_flag:
                                plt.savefig(self.save_name + '.png')
                        else:
                                plt.show()

        def combined_plot(self, dists, names, title="RAD"):  ## here a list of the dists to combine on single plot, and names is the labels for these distributions

                        # setup the plot
                        fig, ax = plt.subplots(1,1, figsize=(6,6))                      

                        ax.set_title(title)
                        ax.set_xlabel('rank')
                        ax.set_ylabel('log10 (% relative abundance)')

                        colors = itertools.cycle(["r", "b", "g"])
			for d in dists:
	                         self.distribution = d     
				 sc = plt.scatter(self.distribution[0,:], self.distribution[1,:], c=next(colors))

			plt.legend(names)

                        if self.save_flag:
                                plt.savefig(self.save_name + '.png')
                        else:
                                plt.show()

        def multi_tl_plot(self, dists, names, title="RAD"):

                        # setup the plot
                        fig, ax = plt.subplots(1,1, figsize=(6,6))
			
                        cmap = plt.cm.jet
                        cmaplist = [(.0,1.0,.0,1.0), (.0,.0,1.0,1.0), (1.0,1.0,.0,1.0), (1.0,.0,.0,1.0)]
                        cmap = cmap.from_list('Custom cmap', cmaplist, 4)

                        bounds = np.linspace(0,4,5)
                        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

                        #sc = plt.scatter(self.distribution[0,:], self.distribution[1,:], c = self.distribution[2,:], vmin = 0, vmax = 3, cmap=cmap)# cmap = ['green', 'blue', 'yellow', 'red'])
                        colors = itertools.cycle(["r", "b", "g"])
			marks = ['8', 's', 'p', 'h', 'D']
			m_id = 0
			for d in dists:
	                         self.distribution = d     
				 sc = plt.scatter(self.distribution[0,:], self.distribution[1,:], c=self.distribution[2,:], vmin=0, vmax=3, cmap=cmap, marker=marks[m_id])
				 m_id += 1

			plt.legend(names)


                        # create a second axes for the colorbar
                        plt.subplots_adjust(left=0.10, right=0.85)
                        ax2 = fig.add_axes([0.9, 0.1, 0.03, 0.8])
                        cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, spacing='proportional', ticks=bounds+0.5, boundaries=bounds, format='%1i')

                        ax.set_title('Rank abundance distribution')
                        ax.set_xlabel('rank')
                        ax.set_ylabel('log abundance')
                        ax2.set_ylabel('Species trophic level', size=12)

                        if self.save_flag:
                                plt.savefig(self.save_name + '.png')
                        else:
                                plt.show()
if __name__=='__main__':

	#r = Rad_calculator(False)
	#r.from_output_species('/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/200sp_rewired/mut_0/sp_60/3120931_26/')
	#r2 = Rad_calculator(False)
	#r2.from_output_species('/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/200sp_rewired/mut_0/sp_60/3120931_27/')

	rp = Rad_plotter(False)	
	#r1 = np.genfromtxt('RAD_im_0.0001_hl_0_mai_0.csv', delimiter=',')
	#rp.single_plot(r1)
	#rp.combined_plot([r.distribution, r2.distribution], ['one', 'two'])

	r1 = np.genfromtxt('RAD_im_0.0001_hl_0_mai_0.csv', delimiter=',')
	r2 = np.genfromtxt('RAD_im_0.0001_hl_40_mai_0.csv', delimiter=',')
	r3 = np.genfromtxt('RAD_im_0.0001_hl_80_mai_0.csv', delimiter=',')
	rp.combined_plot([r1, r2, r3], ['HL = 0', 'HL = 40', 'HL = 80'], 'Single RAD. Immigration = 0.0001. MAI = 0.0')
	#rp.multi_tl_plot([r1, r2, r3], ['HL = 0', 'HL = 40', 'HL = 80'], 'Single RAD. Immigration = 0.0001. MAI = 0.0')
	
	#r1 = np.genfromtxt('mean__RAD_im_0.0001_hl_0_mai_0.csv', delimiter=',')
	#r2 = np.genfromtxt('mean__RAD_im_0.0001_hl_40_mai_0.csv', delimiter=',')
	#r3 = np.genfromtxt('mean__RAD_im_0.0001_hl_80_mai_0.csv', delimiter=',')
	#rp.combined_plot([r1, r2, r3], ['HL = 0', 'HL = 40', 'HL = 80'], 'Mean RAD. Immigration = 0.0001. MAI = 0.0')
	#rp.multi_tl_plot([r1, r2, r3], ['HL = 0', 'HL = 40', 'HL = 80'], 'Mean RAD. Immigration = 0.0001. MAI = 0.0')

        r1 = np.genfromtxt('RAD_im_0.0001_hl_0_mai_0.csv', delimiter=',')
        r2 = np.genfromtxt('RAD_im_0.0005_hl_0_mai_0.csv', delimiter=',')
        r3 = np.genfromtxt('RAD_im_0.001_hl_0_mai_0.csv', delimiter=',')
        #rp.combined_plot([r1, r2, r3], ['IM = 0.0001', 'IM = 0.0005', 'IM = 0.001'], 'Single RAD. HL = 0. MAI = 0.0')
        #r1 = np.genfromtxt('mean__RAD_im_0.0001_hl_0_mai_0.csv', delimiter=',')
        #r2 = np.genfromtxt('mean__RAD_im_0.0005_hl_0_mai_0.csv', delimiter=',')
        #r3 = np.genfromtxt('mean__RAD_im_0.001_hl_0_mai_0.csv', delimiter=',')
        #rp.combined_plot([r1, r2, r3], ['IM = 0.0001', 'IM = 0.0005', 'IM = 0.001'], 'Mean RAD. HL = 0. MAI = 0.0')
        rp.multi_tl_plot([r1, r2, r3], ['IM = 0.0001', 'IM = 0.0005', 'IM = 0.001'], 'Mean RAD. HL = 0. MAI = 0.0')

