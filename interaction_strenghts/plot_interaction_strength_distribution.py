
import sys, os
import matplotlib.pyplot as plt
import numpy as np

it_num = 5000 # iteration number adjancecny to use

is_num = 3

#root_dir = '/home/rusty/Documents/phd files/habitat_loss_project/IBM/random_results/run1'
#HL = [0,50,90]
#HL = [0,10, 20, 30, 40, 50, 60, 70, 80, 90]
#MAI = ['0', '.2', '.4', '.6', '.8', '1']
MAI = ['0', '1']
plot_id = 1

round_off = 0.1 #1000 # 0.1 # different for contiguous and random because very different strengths

for mai in MAI:
    #HL = [0]
    HL = [0, 20, 40, 60, 80]
    HL_data = []

    for hl in HL:
        print(hl)
        dir = '/home/rusty/Documents/phd files/habitat_loss_project/IBM/random_results/run1/HL_%d/mut_' %hl + mai
        Data = np.zeros(0)

        os.chdir(dir)
        sub_dirs = os.listdir('.')

        for d in sub_dirs:
            if d != 'src' and d!='.Rhistory' and d!='network_sim.log' and d!='output' and d!='qsub_network_sim' and d!='network_sim-first.log':
                print(d)
                os.chdir(d)
                #cols = np.linspace(1,60,60)
                with open('adjacency_%d_is%d.csv' %(it_num,is_num)) as f:
                    num_cols = len(f.readline().split(','))
                    f.seek(0)
                #data = np.genfromtxt('adjacency_%d_is3.csv' %it_num, delimiter=',', skip_header=1, usecols=cols.astype(int))
                data = np.genfromtxt('adjacency_%d_is%d.csv' %(it_num,is_num), delimiter=',', skip_header=1, usecols=range(1,num_cols))
                data = data.flatten()
                for i in data:
                    if i>0.00:
                        #print(i)
                        if i >round_off:
                            Data = np.append(Data, round_off)
                        else:
                            Data = np.append(Data, i)
                
                #print(np.shape(data.flatten()))
        #        np.append(Data, data.flatten())
                
                os.chdir('..')
        HL_data.append(Data)
        os.chdir('..')
            
    plt.subplot(1,2,plot_id)
    plt.xlim([0,0.01])
    plt.title("MAI = " + mai)
    plt.xlabel("interaction strength (IS3)")
    plt.ylabel("frequency")
    for h in range(len(HL)):

        hist, edges = np.histogram(HL_data[h], bins=100)

        # convert bin_edges to bin_centres
        centres = []
        for b in range(len(edges)-1):
            centres.append((edges[b+1]+edges[b])/2)
            
        plt.plot(centres, hist)
    plt.legend(HL, title="HL %")    
    plot_id += 1


plt.tight_layout()
plt.show()

#print(os.listdir('.'))
