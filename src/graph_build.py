import networkx as nx
import numpy as np

def build_graph(n=200, radius=0.12, seed=42):
    """Create a random geometric graph with signals on nodes."""
    G = nx.random_geometric_graph(n, radius, seed=seed)
    rng = np.random.default_rng(seed)
    signals = {i: float(rng.normal(0,1)) for i in G.nodes()}
    nx.set_node_attributes(G, signals, 'x')
    return G

def compute_edge_smoothness(G):
    """Add smoothness score s(e) = (x_i - x_j)^2 to edges."""
    for u, v in G.edges():
        s = (G.nodes[u]['x'] - G.nodes[v]['x'])**2
        G[u][v]['s'] = s
    return G