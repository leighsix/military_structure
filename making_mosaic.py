import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
for i in range(1, 5):
    G.add_node(f"command_{i}")
for i in range(1, 5):
    G.add_node(f"decision_{i}")
for i in range(1, 5):
    G.add_node(f"action_{i}")
for i in range(1, 5):
    G.add_node(f"recon_{i}")
for i in range(1, 5):
    G.add_edge(f"command_{i}", f"decision_{i}")
    G.add_edge(f"command_{i}", f"action_{i}")
    G.add_edge(f"decision_{i}", f"recon_{i}")
    G.add_edge(f"recon_{i}", f"action_{i}")
G.add_edge("command_2", "action_1")
G.add_edge("command_3", "decision_2")
G.add_edge("command_3", "action_4")
G.add_edge("command_4", "decision_1")
G.add_edge("decision_2", "recon_1")
G.add_edge("recon_1", "action_4")
G.add_edge("recon_2", "action_3")
G.add_edge("decision_3", "recon_4")
centrality = nx.betweenness_centrality(G)
node_size = [v * 5000 for v in centrality.values()]

pos = nx.spring_layout(G, seed=1734289230)
fig, ax = plt.subplots()

nx.draw_networkx(G, pos=pos, ax=ax, arrows=True, arrowstyle="-",
                 min_source_margin=15,
                 min_target_margin=15, node_size=node_size)

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
