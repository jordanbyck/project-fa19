import student_utils
from student_utils import *
import community
# using python-louvain: https://github.com/taynaud/python-louvain

def find_community_mappings(list_of_homes, adjacency_matrix):
    # returns a mapping from community label : nodes in that community
    G = student_utils.adjacency_matrix_to_graph(adjacency_matrix)[0]

    # using approximated average clustering for G (for verification)
    clustering_coeffs = nx.clustering(G)
    home_coeffs = {int(h): clustering_coeffs[int(h)] for h in list_of_homes}
    print("home clustering coeffs:", home_coeffs)

    # approach using python-louvain (community)
    partition = community.best_partition(G)
    all_communities = set(partition.values())
    community_mappings = {}
    for comm_label in all_communities:
        community_mappings[comm_label] = [node for node in partition.keys() if partition[node] == comm_label]

    print("python-louvain community mappings: ", community_mappings)
    return community_mappings

def find_dropoff_locations(list_of_homes, adjacency_matrix, start, community_mappings):
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

def visualize_communities_and_dropoffs(G, start):
    # draw each community in a different color with its dropoff node

    return



