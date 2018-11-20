import pylab
import matplotlib.cm as cm
import networkx as nx


# Generates the nodes
G = nx.path_graph(40)
center_nodes = {0, 2, 27}
cells = nx.voronoi_cells(G, center_nodes)
partition = set(map(frozenset, cells.values()))
sorted(map(sorted, partition))
temp_list = list(map(sorted,partition))

color_map = []

A = nx.DiGraph()

ctr_node_list = list(center_nodes)

# for center_node in ctr_node_list:
#     A.add_node(center_node)
#     color_map.append('black')

# add nodes to the graph in corresponding colors
for i in range(0,len(center_nodes)):
    nodes = temp_list[i]
    for node in nodes:
        A.add_node(node)
        color_map.append(cm.hsv(1/(i+.5)))



pos = nx.spring_layout(A)
nx.draw_networkx_nodes(A, pos, node_color=color_map, with_labels=True)
pylab.title('Voronoi cells', fontsize=15)
pylab.show()
