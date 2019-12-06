import student_utils
from student_utils import *
import community
# using python-louvain: https://github.com/taynaud/python-louvain

def use_clustering(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    G = student_utils.adjacency_matrix_to_graph(adjacency_matrix)[0]

    # using approximated average clustering for G:
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
