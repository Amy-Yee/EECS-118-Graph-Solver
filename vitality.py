import pylab
import networkx as nx
import csv
import numpy as np

G = nx.Graph()

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

#add nodes to the graph
for i in range(0, np.size(target) + 1):
    G.add_node(i)

#add weighted edges to the graph
for i in range(np.size(source)):
    G.add_weighted_edges_from([(source[i], target[i], value[i])])
    print(source[i],target[i],value[i])


selected_node = int(input("Enter the vitality of the node you wish to see: "))
print(nx.closeness_vitality(G,selected_node))

# shows graph with the node removed
G.remove_node(selected_node)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='b', edge_color='k', node_size=200, alpha=0.5)
pylab.title('Self_Define Net', fontsize=15)
pylab.show()