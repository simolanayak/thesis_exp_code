import networkx as nx
import matplotlib.pyplot as plt

from egg import core

nodenames = ['alpha','beta','gamma','delta','epsilon','zeta','eta','theta']
G = nx.complete_graph(nodenames)
print(nx.adjacency_matrix(G))
nx.draw(G)
plt.show()