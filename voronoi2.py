import pylab
import networkx as nx
import csv
import numpy as np
import matplotlib.cm as cm

D = nx.DiGraph()
color_map = []

# generates a fresh graph
def newdigraph(D, color_map):
    D.clear()
    with open(input("Please enter your filepath: ")) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        source = []
        target = []
        value = []

        for row in reader:
            source.append(int(row[0]))
            target.append(int(row[1]))
            value.append(int(row[2]))

    for i in range(0, np.size(target) + 1):
        D.add_node(i)
        color_map.append(cm.hsv(1 / (i + .5)))

    for i in range(np.size(source)):
        D.add_weighted_edges_from([(source[i], target[i], value[i])])
        print(source[i],target[i],value[i])

def voronoi(D, color_map):
    newdigraph(D, color_map)
    #color_map = []
    center_nodes = []
    i = 0

    while(i<2):
        center_nodes.append(int(input("Please enter a center node.")))
        i += 1

    cells = nx.voronoi_cells(D, center_nodes)
    partition = set(map(frozenset,cells.values()))
    print(sorted(map(sorted, partition)))
    # draw the graph
    pos = nx.spring_layout(D)
    nx.draw(D, pos, with_labels=True, node_color=color_map, edge_color='k', node_size=200, alpha=0.5)
    pylab.title('Self_Define Net', fontsize=15)
    pylab.show()

#def colornodes(D, center_nodes):


voronoi(D, color_map)
