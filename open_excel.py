import csv
import pylab
import matplotlib.cm as cm
import networkx as nx
import tkinter as tk
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

# G = nx.DiGraph()
#
# with open(input("Please enter your filepath: ")) as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader)
#     source = []
#     target = []
#     value = []
#     for row in reader:
#         source.append(int(row[0]))
#         target.append(int(row[1]))
#         value.append(int(row[2]))
#
#     #add nodes to the graph
#     for i in range(0, np.size(target) + 1):
#         G.add_node(i)
#
#     #add weighted edges to the graph
#     for i in range(np.size(source)):
#         G.add_weighted_edges_from([(source[i], target[i], value[i])])
#         print(row)
#
# print(nx.strongly_connected_components(G))

G = nx.cycle_graph(3)
pos = nx.spring_layout(G)
print(nx.closness_vitality(G))
nx.draw(G, pos, with_labels=True, node_color='b', edge_color='k', node_size=200, alpha=0.5)
pylab.title('Self_Define Net', fontsize=15)
pylab.show()

