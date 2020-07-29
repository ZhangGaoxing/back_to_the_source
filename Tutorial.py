#import matplotlib.pyplot as plt
#nx.draw(g)

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import random
import networkx as nx


# %%
import dynamic
import spread 
import static


# %%
# generate a graph from Barabasi-Albert algorithm
n = 500 #number of nodes
m = 3 #number of new edges per added node
g = nx.barabasi_albert_graph(n, m)
d = nx.shortest_path_length(g)
paths = nx.all_pairs_dijkstra_path(g)


# %%
# generate an epidemic starting from a random source
noise = 0.3 # noise parameter for transmission delays
infected, source = spread.spread(g, noise, delay_type='uniform')


# %%
# 'infected' is a dictionary of infection times, the source has infection time 0 by this is not used by the algo
print 'Node 0 was infected at ', infected[0]
print 'The infection time of the source is', infected[source]
print 'The source was', source


# %%
# generate static sensors randomly 
ks = 10 # number of static sensors
static_sensors = random.sample(g.nodes(), ks)
print 'Static sensors:', static_sensors


# %%
# run source localization with STATIC algorithm
cand_sources, seq_cand_sources, time, infected_nodes, success = static.static(g, d, static_sensors, infected, noise=noise)


# %%
# set of candidate sources
print cand_sources
print source in cand_sources, '(If True the source is in the set)'


# %%
#'seq_cand_sources' is the list of the set of candidates at every algotithm step
print seq_cand_sources


# %%
#'time' is the time (after the epidemic started) at which the final set of candidates was produced
print time


# %%
# 'infected_nodes' is the list of the numbers of infected nodes at every algorithm step
print infected_nodes


# %%
# 'success' is a variable used for debugging: check if at every step the source is still among candidates 
# (to use it you need to pass the real source to the algo, otherwise 0 at each step by default)
#print success


# %%
# run source localization with DYNAMIC algorithm
delay = 0.3 # delay between to dynamic sensor placements
kd = 10 # budget for dynamic sensors
d_1 = d # unweighted distance matrix (if the graph is unweighted it is equal to d)
sensors, cand_sources, seq_cand_sources, time, infected_nodes, success = dynamic.dynamic(g, d, d_1, paths, static_sensors, infected, kd, delay, 
                                                                                         noise=noise, real_source=source)


# %%
print sensors # set of static and dynamic sensors


# %%
print cand_sources


# %%
print seq_cand_sources


# %%
print success


# %%


