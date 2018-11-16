import pylab
import matplotlib.cm as cm
import networkx as nx

G = nx.cycle_graph(3)
print(nx.closeness_vitality(G))