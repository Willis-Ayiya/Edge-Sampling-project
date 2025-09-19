from src.graph_build import build_graph, compute_edge_smoothness
from src.sampling import sample_edges_by_smoothness
from src.viz import draw_and_annotate

def main():
    
    G = build_graph(n=100, radius=0.15, seed=1)
    G = compute_edge_smoothness(G)

    Es = sample_edges_by_smoothness(G, r=0.3)
    print(f"Original edges: {G.number_of_edges()}, Sampled: {Es.number_of_edges()}")

    draw_and_annotate(G, Es, out="output_graph.png")
    print("Graph visualization saved as output_graph.png")

if __name__ == "__main__":
    main()