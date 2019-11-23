import networkx as nx
import matplotlib.pyplot as plt

# i.e. central start node, k arms with m intermediate nodes on each arm between start and home
# one home per arm
# optimal solution: drop off everyone at start and let them walk?

# rewritten, utilize formula: locations = 1 + homes * (intermediates + 1)
def snowflake_maker(locations, homes, intermediates):
    # initialize starting values
    G = nx.Graph()

    # color map to distinguish homes from start from intermediate locations
    color_map = []

    # let start be numbered 0
    G.add_node(0)
    color_map.append('green')

    # let homes be numbered (1 -> # homes)
    G.add_nodes_from(range(1, homes + 1))
    color_map += ['red' for i in range(1, homes + 1)]

    # let intermediate nodes be numbered (# homes + 1 -> # locations)
    G.add_nodes_from(range(homes + 1, locations))
    color_map += ['blue' for i in range(homes + 1, locations)]

    # add edges
    for i in range(1, homes + 1):
        v = homes + i
        G.add_edge(0, v)

    for j in range(1, intermediates):
        for i in range(1, homes + 1):
            u = j * homes + i
            v = ((j + 1) * homes) + i
            G.add_edge(u, v)

    for j in range(1, homes + 1):
        u = (intermediates * homes) + j
        G.add_edge(u, j)

    # draw and return graph
    plot_graph(G, color_map)
    return G

# plot the graph
def plot_graph(G, color_map):
    nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=labels)
    plt.show()

