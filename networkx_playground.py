import networkx as nx
import matplotlib.pyplot as plt

from egg import core

G = nx.scale_free_graph(50)
G = nx.to_undirected(G)
nx.draw(G)
adj = nx.adjacency(G)
plt.show()