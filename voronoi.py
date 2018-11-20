import pylab
import networkx as nx
import csv
import numpy as np
import matplotlib.cm as cm

# placeholder graph
G = nx.DiGraph()
center_nodes = []
color_map = []

def main():
    # generate a fresh DiGraph
    generatedigraph(G)

    # user inputs center nodes
    node = input("Please enter a center node, or press ENTER to quit: ")
    while (node != ""):
        center_nodes.append(int(node))
        node = input("Please enter a center node, or press ENTER to quit: ")

    # obtains the Voronoi cells
    cells = nx.voronoi_cells(G, center_nodes)
    partition = set(map(frozenset,cells.values()))
    cells_list = list(sorted(map(sorted, partition)))
    print(cells_list)

    # adds color corresponding to Voronoi cell
    for i in range(0, len(cells_list)):
        for j in range(0, len(cells_list[i])):
            color_map.append(cm.hsv(1 / (i + .5)))

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, with_labels=True, node_color=color_map, edge_color='k', node_size=200, alpha=0.5)
    pylab.title('Voronoi cells', fontsize=15)
    pylab.show()

def generatedigraph(G):
    G.clear()

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
        G.add_node(i)

    for i in range(np.size(source)):
        G.add_weighted_edges_from([(source[i], target[i], value[i])])
        print(source[i],target[i],value[i])

main()