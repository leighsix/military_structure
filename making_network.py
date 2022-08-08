import matplotlib.pyplot as plt
import networkx as nx

# Generate the computer network graph
G = nx.Graph()

G.add_node("command")
for i in range(1, 6):
    G.add_node(f"decision_{i}")
    for j in range(1, 2):
        G.add_node("action_" + str(i) + "_" + str(j))
        G.add_node("recon_" + str(i) + "_" + str(j))

for u in range(1, 6):
    G.add_edge("command", "decision_" + str(u))
    for v in range(1, 2):
        G.add_edge("decision_" + str(u), "action_" + str(u) + "_" + str(v))
        G.add_edge("decision_" + str(u), "recon_" + str(u) + "_" + str(v))
        G.add_edge("action_" + str(u) + "_" + str(v), "recon_" + str(u) + "_" + str(v))


centrality = nx.betweenness_centrality(G)
node_size = [v * 5000 for v in centrality.values()]

# Get a reproducible layout and create figure
pos = nx.spring_layout(G, seed=1734289230)
fig, ax = plt.subplots()

# Note: the min_source/target_margin kwargs only work with FancyArrowPatch objects.
# Force the use of FancyArrowPatch for edge drawing by setting `arrows=True`,
# but suppress arrowheads with `arrowstyle="-"`

nx.draw_networkx(G, pos, ax=ax, arrows=True, arrowstyle="-", node_size=node_size,
                 min_source_margin=15,
                 min_target_margin=15)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
