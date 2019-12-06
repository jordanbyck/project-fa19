import student_utils
from student_utils import *
import community
from networkx import dijkstra_path_length
# using python-louvain: https://github.com/taynaud/python-louvain

def find_community_mappings(list_of_homes, G):
    # returns a mapping from community label : nodes in that community
    #G = student_utils.adjacency_matrix_to_graph(adjacency_matrix)[0]

    # using approximated average clustering for G (for verification)
    clustering_coeffs = nx.clustering(G)
    home_coeffs = {int(h): clustering_coeffs[int(h)] for h in list_of_homes}
    print("home clustering coeffs:", home_coeffs)

    # approach using python-louvain (community)
    partition = community.best_partition(G, weight='weightoo')
    all_communities = set(partition.values())
    community_mappings = {}
    for comm_label in all_communities:
        community_mappings[comm_label] = [node for node in partition.keys() if partition[node] == comm_label]

    print("python-louvain community mappings: ", community_mappings)
    return community_mappings

def find_dropoff_locations(list_of_homes, G, start, community_mappings):
    # returns a mapping from community label: dropoff location for that community
    dropoffs = {}
    for label in community_mappings.keys():
        # picks a location from each community at random to start

        current_location = np.random.choice(community_mappings[label])
        while current_location in list_of_homes:
            current_location = np.random.choice(community_mappings[label])
        if current_location == start:
            dropoffs[label] = start
        else:
            dropoffs[label] = current_location
    return dropoffs

# modify to have multiple drop offs
def find_optimal_dropoff_within_cluster(list_of_homes, adjacency_matrix, community_mappings):
    # returns one optimal drop off within a cluster

    graph = student_utils.adjacency_matrix_to_graph(adjacency_matrix)[0]

    dropoffs = {}

    print(community_mappings)
    print(list_of_homes)
    for label in community_mappings.keys():
        curr_homes = []
        curr_locations = community_mappings[label]
        # find the homes within the current community
        for node in curr_locations:
            if str(node) in list_of_homes:
                curr_homes.append(node)

        neighbors = {}
        curr_neighbors = []
        # create a mapping between nodes and their neighbors
        # nodes are mapped to a list of tuples that contains the neighboring node and the weight
        for node in curr_locations:
            for i in range(len(adjacency_matrix[node])):
                if type(adjacency_matrix[node][i]) != str:
                    curr_neighbors.append((i, adjacency_matrix[node][i]))

            neighbors[node] = curr_neighbors

        # find the costs of dropping off at each location
        dropoff_costs = find_cost_of_dropoff_within_cluster(graph, curr_homes, curr_locations, neighbors)

        # find the minimum cost dropoff
        min_drop_cost = float("inf")
        min_drop = None
        for key in dropoff_costs.keys():
            if dropoff_costs[key] < min_drop_cost:
                min_drop_cost = dropoff_costs[key]
                min_drop = key

        dropoffs[label] = min_drop

    return dropoffs

def find_cost_of_dropoff_within_cluster(graph, homes, locations, neighbors):
    # returns a mapping of dropoffs to costs
    dropoff_costs = {}

    for location in locations:
        dropoff_costs[location] = 0
        for home in homes:
            dropoff_costs[location] += nx.dijkstra_path_length(graph, location, home)

    print(dropoff_costs)
    return dropoff_costs

def visualize_communities_and_dropoffs():
    # draw each community in a different color with its dropoff node
    return

def visualize_communities_and_dropoffs(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix):
    # draw each community in a different color with its dropoff node
    G = student_utils.adjacency_matrix_to_graph(adjacency_matrix)[0]
    comm_mappings = find_community_mappings(list_of_homes, adjacency_matrix)
    comm_dropoffs = find_dropoff_locations(list_of_homes, adjacency_matrix, starting_car_location, comm_mappings)
    color_map = [0 for n in range(len(list_of_locations))]
    current_color = 0
    for comm_label in comm_mappings:
        locs = comm_mappings[comm_label]
        for loc in locs:
            color_map[loc] = current_color
        current_color += 1.0/len(comm_mappings.keys())
    color_map[int(starting_car_location)] = 1
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=labels)
    plt.show()
