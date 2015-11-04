import igraph as igr
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import random as rnd
from web import Network

base_dir = "/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/network_structure_vs_persistence/rewired/bad_net_59/"
#base_dir = "/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/network_structure_vs_persistence/rewired/good_net_52/"

#graphml_file = "/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/network_structure_vs_persistence/noconstraints/bad_net_54/new_network_53_wtl.graphml"
#graphml_file = "/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/network_structure_vs_persistence/noconstraints/good_net_74/new_network_73_wtl.graphml"
#graphml_file = "/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/network_structure_vs_persistence/rewired/good_net_52/rewired_network_51.graphml"
graphml_file = base_dir + "rewired_network_58.graphml"
#graphml_file = base_dir + "rewired_network_51.graphml"

all_results = np.zeros((3,7))

for rr in range(1):


	G = nx.read_graphml(graphml_file)
	Net = Network(G)
	G = nx.Graph(G)
	
	#find modularity
	#net = Network(G)
	#tls = net.get_trophic_levels()
	#part = community.best_partition(G)
	#IG = igr.read_graphml(graphml_file)
	IG = igr.load(graphml_file)
	IG.to_undirected() # = IG0.to_undirected()
	membs = IG.community_multilevel()
	mod = IG.modularity(membs)
	#mod = modularity(part, G)
	print("Modularity:")
	print(mod)
	print(IG.transitivity_undirected())
	print(Net.connectance())
	Net.get_trophic_levels()
	Net.find_trophic_positions()
	#print(Net.omnivory())
	print(Net.generality_vulnerability_sd())
	print(Net.maximum_similarity())

	gsd, vsd = Net.generality_vulnerability_sd()

	all_results[0,0] = G.number_of_nodes() #/ 120.0 Now normalising all elements
	all_results[0,1] = Net.connectance()
	all_results[0,2] = mod
	all_results[0,3] = IG.transitivity_undirected()
	all_results[0,4] = gsd
	all_results[0,5] = vsd
	all_results[0,6] = Net.maximum_similarity()



base_dir = "/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/network_structure_vs_persistence/rewired/good_net_52/"
graphml_file = base_dir + "rewired_network_51.graphml"


for rr in range(1):

	G = nx.read_graphml(graphml_file)
	Net = Network(G)
	G = nx.Graph(G)



	#find modularity
	#net = Network(G)
	#tls = net.get_trophic_levels()
	#part = community.best_partition(G)
	#IG = igr.read_graphml(graphml_file)
	IG = igr.load(graphml_file)
	IG.to_undirected() # = IG0.to_undirected()
	membs = IG.community_multilevel()
	mod = IG.modularity(membs)
	#mod = modularity(part, G)
	print("Modularity:")
	print(mod)
	print(IG.transitivity_undirected())
	print(Net.connectance())
	Net.get_trophic_levels()
	Net.find_trophic_positions()
	#print(Net.omnivory())
	print(Net.generality_vulnerability_sd())
	print(Net.maximum_similarity())

	gsd, vsd = Net.generality_vulnerability_sd()

	all_results[1,0] = G.number_of_nodes() #/ 120.0
	all_results[1,1] = Net.connectance()
	all_results[1,2] = mod
	all_results[1,3] = IG.transitivity_undirected()
	all_results[1,4] = gsd
	all_results[1,5] = vsd
	all_results[1,6] = Net.maximum_similarity()



base_dir = "/MyFiles/cm1788/Documents/prunning_for_stability/bc3_results/network_structure_vs_persistence/rewired/good_net_52/"
graphml_file = base_dir + "rewired_network_51.graphml"

n_rep = 1

for rr in range(n_rep):

	G = nx.read_graphml(graphml_file)

	IG = igr.load(graphml_file)
	IG.to_undirected() # = IG0.to_undirected()
	
	#print(IG.vs['id']=='1')
	#print(IG.vertex_attributes())

	## this finds out which species have gone extinct and removes them
	rep_id = rr #rnd.randint(0,99)
	rep_dirs = os.listdir(base_dir)
	rep_dir = rep_dirs[rep_id]

	tl_file = base_dir + rep_dirs[rep_id] + "/output_species.csv" 

	eco = np.genfromtxt(tl_file, delimiter=',', skip_header=1)
	S = eco[:,8]
	sp_sim_ids = eco[:,0]
	index = 0
	for s in S:
		if s==0.0:
			G.remove_node("%d" %sp_sim_ids[index])
			IG.delete_vertices(IG.vs['id']== sp_sim_ids[index] ) #"%d" %sp_sim_ids[index])
		index += 1

	Net = Network(G)
	G = nx.Graph(G)

	#find modularity
	#net = Network(G)
	#tls = net.get_trophic_levels()
	#part = community.best_partition(G)
	#IG = igr.read_graphml(graphml_file)

	membs = IG.community_multilevel()
	mod = IG.modularity(membs)
	#mod = modularity(part, G)
	#print("Modularity:")
	#print(mod)
	#print(IG.transitivity_undirected())
	#print(Net.connectance())
	Net.get_trophic_levels()
	Net.find_trophic_positions()
	#print(Net.omnivory())
	#print(Net.generality_vulnerability_sd())
	#print(Net.maximum_similarity())

	gsd, vsd = Net.generality_vulnerability_sd()

	all_results[2,0] += G.number_of_nodes() #/ 120.0
	all_results[2,1] += Net.connectance()
	all_results[2,2] += mod
	all_results[2,3] += IG.transitivity_undirected()
	all_results[2,4] += gsd
	all_results[2,5] += vsd
	all_results[2,6] += Net.maximum_similarity()

all_results[2,:] /= n_rep


## normalise all metrics by the largest one
raw_results = np.copy(all_results)

for ri in range(7):
	ma = max(max(all_results[0,ri], all_results[1,ri]), all_results[2,ri])
	all_results[0,ri] = all_results[0,ri] / ma
	all_results[1,ri] = all_results[1,ri] / ma
	all_results[2,ri] = all_results[2,ri] / ma

#np.savetxt("summary_results_prune.csv", all_results, delimiter=',')

fig, ax = plt.subplots()
fig.canvas.draw()

#labels = [item.get_text() for item in ax.get_xticklabels()]
#labels[1] = 'Testing'

plt.xlim([-1,7])
labs = ['', 'N', 'C', 'Mod', 'Clu', 'GSD', 'VSD', 'MS', '']
plt.plot(np.arange(7), all_results[0,:], 'r^', ms=15)
plt.plot(np.arange(7), all_results[1,:], 'g^', ms=15)
plt.plot(np.arange(7), all_results[2,:], 'k^', ms=15)
#plt.xticks(labs)

ax.set_xticklabels(labs)
plt.xlabel("metric")
plt.ylabel("value")
plt.legend(["bad network", "good network", "pruned network"], loc=2)

#plt.savefig("summary_metrics_good_bad_pruned.png")
plt.show()


