import networkx as nx
n = 10
G = nx.complete_graph(n)
nx.wiener_index(G) == n * (n - 1) / 2