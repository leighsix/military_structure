import matplotlib.pyplot as plt
import networkx as nx
import PIL

# Image URLs for graph nodes
# icons = {
#     "router": "icons/router_black_144x144.png",
#     "switch": "icons/switch_black_144x144.png",
#     "PC": "icons/computer_black_144x144.png",
# }

# Load images
# images = {k: PIL.Image.open(fname) for k, fname in icons.items()}

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

# Get a reproducible layout and create figure
pos = nx.spring_layout(G, seed=1734289230)
fig, ax = plt.subplots()

# Note: the min_source/target_margin kwargs only work with FancyArrowPatch objects.
# Force the use of FancyArrowPatch for edge drawing by setting `arrows=True`,
# but suppress arrowheads with `arrowstyle="-"`
nx.draw_networkx_edges(
    G,
    pos=pos,
    ax=ax,
    arrows=True,
    arrowstyle="-",
    min_source_margin=15,
    min_target_margin=15,
)
nx.draw_networkx(G, pos)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
