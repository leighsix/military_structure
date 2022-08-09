import matplotlib.pyplot as plt
import networkx as nx

# Generate the computer network graph
G1 = nx.Graph()

G1.add_node("command")
for i in range(1, 6):
    G1.add_node(f"decision_{i}")
    for j in range(1, 2):
        G1.add_node("action_" + str(i) + "_" + str(j))
        G1.add_node("recon_" + str(i) + "_" + str(j))

for u in range(1, 6):
    G1.add_edge("command", "decision_" + str(u))
    for v in range(1, 2):
        G1.add_edge("decision_" + str(u), "action_" + str(u) + "_" + str(v))
        G1.add_edge("decision_" + str(u), "recon_" + str(u) + "_" + str(v))
        G1.add_edge("action_" + str(u) + "_" + str(v), "recon_" + str(u) + "_" + str(v))

G2 = nx.Graph()
for i in range(1, 5):
    G2.add_node(f"command_{i}")
for i in range(1, 5):
    G2.add_node(f"decision_{i}")
for i in range(1, 5):
    G2.add_node(f"action_{i}")
for i in range(1, 5):
    G2.add_node(f"recon_{i}")
for i in range(1, 5):
    G2.add_edge(f"command_{i}", f"decision_{i}")
    G2.add_edge(f"command_{i}", f"action_{i}")
    G2.add_edge(f"decision_{i}", f"recon_{i}")
    G2.add_edge(f"recon_{i}", f"action_{i}")
G2.add_edge("command_2", "action_1")
G2.add_edge("command_3", "decision_2")
G2.add_edge("command_3", "action_4")
G2.add_edge("command_4", "decision_1")
G2.add_edge("decision_2", "recon_1")
G2.add_edge("recon_1", "action_4")
G2.add_edge("recon_2", "action_3")
G2.add_edge("decision_3", "recon_4")


# 중심성 분석 만들기
def computing_centrality(self, cent, graph):
    ce = 0
    if cent == "degree":
        ce = nx.degree_centrality(graph)
    elif cent == "between":
        ce = nx.betweenness_centrality(graph)
    elif cent == "close":
        ce = nx.closeness_centrality(graph)
    elif cent == "eigenvector":
        ce = nx.eigenvector_centrality(graph)
    elif cent == "pagerank":
        ce = nx.pagerank(graph)
    return ce

def computing_information_flow(self, graph,  ):
    for

# Visualization
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
