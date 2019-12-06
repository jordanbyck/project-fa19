import student_utils
from student_utils import *

def use_clustering(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    G = student_utils.adjacency_matrix_to_graph(adjacency_matrix)[0]

    # using approximated average clustering for G:
    clustering_coeffs = nx.clustering(G)
    print("approximated average clustering coefficient:", clustering_coeffs)
    home_coeffs = {int(h): clustering_coeffs[int(h)] for h in list_of_homes}
    print("home clustering coeffs:", home_coeffs)

    # using the Girvan–Newman method to find communities of graphs
    # define custom function for how to select edges to remove in the algorithm
    def most_central_edge(G):
        centrality = nx.edge_betweenness_centrality(G)
        max_cent = max(centrality.values())
        # scale the centrality values so they are between 0 and 1, and add some random noise.
        centrality = {e: c / max_cent for e, c in centrality.items()}
        # add some random noise.
        centrality = {e: c + np.random.random() for e, c in centrality.items()}
        return max(centrality, key=centrality.get)

    # get only the first k tuples of communities
    k = int(len(list_of_locations) / 10)
    communities = ()
    comp = algos.community.centrality.girvan_newman(G, most_valuable_edge=most_central_edge)
    for comms in itertools.islice(comp, k):
        comms = tuple(sorted(c) for c in comms)
        print("communities: ", comms)



