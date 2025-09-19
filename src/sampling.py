import networkx as nx

def sample_edges_by_smoothness(G, r=0.3):
    """Sample r fraction of edges with smallest smoothness, ensure connectivity."""
    edges_sorted = sorted(G.edges(data='s'), key=lambda t: t[2])
    k = max(1, int(r * G.number_of_edges()))
    selected = [(u, v, {'s': s}) for u, v, s in edges_sorted[:k]]

    Es = nx.Graph()
    Es.add_nodes_from(G.nodes(data=True))
    Es.add_edges_from(selected)

    if not nx.is_connected(Es):
        for u, v, data in nx.minimum_spanning_edges(G, data=True, weight='s'):
            if not Es.has_edge(u, v):
                Es.add_edge(u, v, **data)
            if nx.is_connected(Es):
                break
    return Es