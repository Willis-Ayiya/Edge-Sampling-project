import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def draw_and_annotate(G, Es, out="graph.png"):
    """Draw graph and sampled edges, then annotate with PIL."""
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(6,6))
    nx.draw(G, pos, node_size=20, alpha=0.2)
    nx.draw_networkx_edges(Es, pos, width=2, edge_color='red')
    plt.axis("off")
    plt.savefig(out, dpi=200)
    plt.close()

    im = Image.open(out)
    draw = ImageDraw.Draw(im)
    draw.text((10, 10), "Sampled Graph", fill=(255,0,0))
    im.save(out.replace(".png", "_annot.png"))