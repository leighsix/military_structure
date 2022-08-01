import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

G = nx.random_regular_graph(3, 20)
G1 = nx.barabasi_albert_graph(20, 3)
G2 = nx.watts_strogatz_graph(20, 4, 0)
G3 = nx.complete_graph(20)
G4 = nx.erdos_renyi_graph(20, 0.15)
nx.draw_circular(G2, with_labels=False, node_color='#0165fc', edge_color='#0165fc')
# nx.draw_circular(G1, with_labels=False)
# nx.draw_circular(G2, with_labels=False)
# nx.draw_circular(G3, with_labels=False)
# nx.draw_circular(G4, with_labels=False)
plt.show()
