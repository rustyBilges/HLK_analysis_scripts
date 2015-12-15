import numpy as np
import os


#dir = "HL_type_1/HL_0/IM_0.001/mut_0/"
home_dir = os.getcwd()

HL = [0,10,20,30,40,50,60,70,80,90]
IM = [0.0001,0.0002,0.0003,0.0004,0.0005,0.001,0.002,0.003,0.004,0.005]
#IM = [0.00001, 0.0001, 0.0002,0.0003, 0.0004, 0.0005, 0.001,0.002,0.003,0.004,0.005]  ## additon of lower IR


map_mean = np.zeros((len(IM), len(HL)))
map_sd = np.zeros((len(IM), len(HL)))

#mai = 0
#mai = 1.0
mai = 0.5
type = 1

base_dir = "HL_type_" + str(type) + "/"

crash_file = open("crash_report.txt", 'w')

hl_id = 0
for hl in HL:
	print("habitat loss = %d" %hl)
	im_id = 0
	for im in IM:

		dir = base_dir + "HL_" + str(hl) + "/IM_" + str(im) + "/mut_" + str(mai)
		os.chdir(dir)

		rep_dirs = os.listdir('.')
		rep_count = 0
		
		L = []
		for r in rep_dirs:
			if r != 'src':
				os.chdir(r)
				#print(r)
				outputs = os.listdir('.')
				if 'adjacency_5000_is1.csv' in outputs:

	                                A = np.genfromtxt("adjacency_5000_is1.csv" , delimiter=',', skip_header=1)
                                        A = A[:,1:]     
                	                B = np.sum(A!=0)
                        	        L.append(B)

					rep_count += 1
				else:
					#print("crash here")
					crash_file.write(os.getcwd())
					crash_file.write("\n")
				os.chdir('..')
				#rep_count += 1
			
		#print(rep_count)

		map_mean[im_id, hl_id] = np.mean(L)
		map_sd[im_id, hl_id] = np.std(L)
	
		im_id += 1
		os.chdir(home_dir)

	hl_id += 1


np.savetxt('mean_numlinks_map_mai' + str(mai) + '.csv', map_mean, delimiter=',')
np.savetxt('sd_numlinks_map_mai' + str(mai) + '.csv', map_sd, delimiter=',')

