import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
import graph_maker
import student_utils
import clustering_approach
import graphModifier
import practiceSolver

from student_utils import *
"""
======================================================================
  Complete the following function.
======================================================================
"""

class Node:

    def __init__(self, name, position, parent):
        self.name = name
        self.position = position
        self.parent = parent


def solve(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    """
    Write your algorithm here.
    Input:
        list_of_locations: A list of locations such that node i of the graph corresponds to name at index i of the list
        list_of_homes: A list of homes
        starting_car_location: The name of the starting location for the car
        adjacency_matrix: The adjacency matrix from the input file
    Output:
        A list of locations representing the car path
        A dictionary mapping drop-off location to a list of homes of TAs that got off at that particular location
        NOTE: both outputs should be in terms of indices not the names of the locations themselves
    """
    #Do not delete next line
    # graphModifier.graphClusterer(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix)
    location_dict = {}
    car_start_int = 0
    list_of_homes_int = []
    list_of_locations_int = [_ for _ in range(len(list_of_locations))]
    for j in range(len(list_of_locations)):
        location_dict[j] = list_of_locations[j]
        if list_of_locations[j] == starting_car_location:
            car_start_int = j
        for _ in list_of_homes:
            if _ == list_of_locations[j]:
                list_of_homes_int += [j]




    #preProcess(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix)
    G = student_utils.adjacency_matrix_to_graph(adjacency_matrix)[0]
    B = clusterGraph(list_of_locations_int, list_of_homes_int, car_start_int, G)

    returner = practiceSolver.tspRepeats(B, car_start_int)

    finalList = [returner[0]]
    for i in range(len(returner)-1):
        finalList += nx.shortest_path(G, returner[i], returner[i+1], weight='weight')[1:]
    finalList += nx.shortest_path(G, returner[-1], returner[0], weight='weight')[1:]

    #clustering_approach.visualize_communities_and_dropoffs(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix)
    returnList = []
    for i in finalList:
        returnList.append(location_dict[i])

    return [int(_) for _ in finalList], {car_start_int: list_of_homes_int}


def clusterGraph(list_of_locations_int, list_of_homes_int, car_start_int, G):
    #G = student_utils.adjacency_matrix_to_graph(adjacency_matrix)[0]
    B = nx.Graph()
    clusterDict = clustering_approach.find_community_mappings(list_of_homes_int, G)
    dropoffs = clustering_approach.find_dropoff_locations(list_of_homes_int, G, car_start_int,
                                                          clusterDict)
    all_distances = dict(nx.floyd_warshall(G))
    edges = {""}
    edges.pop()
    for _ in dropoffs:
        for __ in dropoffs:
            if not B.has_edge(_, __) and not __ == _:
                edges.add((_, __, all_distances[_][__]))
    B.add_weighted_edges_from(edges)
    return B


#not working!!!! fix this
def preProcess(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    G = student_utils.adjacency_matrix_to_graph(adjacency_matrix)
    home_dict = {}
    for i in list_of_homes:
        for j in range(len(list_of_locations)):
            if list_of_locations[j] == i:
                home_dict[i] = j
                continue
    for i in home_dict:
        if G[0].degree[home_dict[i]] == 1:
            home_dict[i] = G.edges[home_dict[i]][0]
    print(1)
    return



def dist(node1, node2):
    # using networkx shortest_path function
    return nx.shortest_path()

def trivial_output_solver(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    G = student_utils.adjacency_matrix_to_graph(adjacency_matrix)[0]

    # helper function with access to G
    def distance_between_locations(a, b):
        path_dist = nx.shortest_path_length(G, a, b)
        # print("distance from " + str(a) + " to " + str(b) +  ": ", path_dist)
        return path_dist

    # either proceed linearly through list of homes or through shuffled list of homes
    randomized_homes = np.random.shuffle(list_of_homes)
    homes = list_of_homes

    # using approximated average clustering for G:
    clustering_coeffs = nx.clustering(G)
    print("approximated average clustering coefficient:", clustering_coeffs)
    home_coeffs = {int(h): clustering_coeffs[int(h)] for h in homes}
    print("home clustering coeffs:", home_coeffs)

    # using the Girvan–Newman method to find communities of graphs
    # define custom function for how to select edges to remove in the algorithm
    def most_central_edge(G):
        centrality = nx.edge_betweenness_centrality(G, normalized=False, weight='weight')
        max_cent = max(centrality.values())
        # Scale the centrality values so they are between 0 and 1,
        # and add some random noise.
        centrality = {e: c / max_cent for e, c in centrality.items()}
        # Add some random noise.
        centrality = {e: c + np.random.random() for e, c in centrality.items()}
        return max(centrality, key=centrality.get)

    # get only the first k tuples of communities
    k = 10

    comp = algos.community.centrality.girvan_newman(G, most_valuable_edge=most_central_edge)
    for communities in itertools.islice(comp, k):
        print("communities: ", tuple(sorted(c) for c in communities))

    # using A* from start to each node
    total_path = []
    current_home = homes[0]
    total_path += nx.astar_path(G, int(starting_car_location), int(current_home), distance_between_locations)
    for next_home in homes[1:]:
        # print("finding path between " + str(current_home) + " and " + str(next_home))
        path_between = nx.astar_path(G, int(starting_car_location), int(current_home), distance_between_locations)
        total_path += path_between
        current_home = next_home
    total_path += nx.astar_path(G, int(current_home), int(starting_car_location), distance_between_locations)
    print("total super shitty path: " + str(total_path))

    # locs = []
    # for i in list_of_locations:
    #     locs.append(int(i))
    #
    # homes = []
    # for i in list_of_homes:
    #     homes.append(int(i))

    # # first, find a node that is a neighbor of the start
    # dropOffIndex = None
    # for i in range(len(adjacency_matrix[0])):
    #     if adjacency_matrix[0][i] == 1:
    #         dropOffIndex = i
    #
    # dropOffNode = list_of_locations[dropOffIndex]

    graph_maker.print_trivial_output(len(list_of_locations), starting_car_location, list_of_homes)

    start = list_of_locations[int(starting_car_location)]
    # dropOffNode = list_of_locations[int(dropOffNode)]

    start = int(start)
    # dropOffNode = int(dropOffNode)
    return [start], {start: homes}

def compute_clustering_coefficient(G, trials=1000):
    n = len(G)
    triangles = 0
    nodes = G.nodes()
    for i in [np.random.randint(0, n) for i in range(trials)]:
        print([nodes[i]])
        nbrs = list(G[nodes[i]])
        if len(nbrs) < 2:
            continue
        u, v = np.random.choice(nbrs, 2)
        if u in G[v]:
            triangles += 1
    return triangles / float(trials)


"""
======================================================================
   No need to change any code below this line
======================================================================
"""

"""
Convert solution with path and dropoff_mapping in terms of indices
and write solution output in terms of names to path_to_file + file_number + '.out'
"""
def convertToFile(path, dropoff_mapping, path_to_file, list_locs):
    string = ''
    for node in path:
        string += list_locs[node] + ' '
    string = string.strip()
    string += '\n'

    dropoffNumber = len(dropoff_mapping.keys())
    string += str(dropoffNumber) + '\n'
    for dropoff in dropoff_mapping.keys():
        strDrop = list_locs[dropoff] + ' '
        for node in dropoff_mapping[dropoff]:
            strDrop += list_locs[node] + ' '
        strDrop = strDrop.strip()
        strDrop += '\n'
        string += strDrop
    utils.write_to_file(path_to_file, string)

def solve_from_file(input_file, output_directory, params=[]):
    print('Processing', input_file)

    input_data = utils.read_file(input_file)
    num_of_locations, num_houses, list_locations, list_houses, starting_car_location, adjacency_matrix = data_parser(input_data)
    car_path, drop_offs = solve(list_locations, list_houses, starting_car_location, adjacency_matrix, params=params)

    basename, filename = os.path.split(input_file)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_file = utils.input_to_output(input_file, output_directory)

    convertToFile(car_path, drop_offs, output_file, list_locations)


def solve_all(input_directory, output_directory, params=[]):
    input_files = utils.get_files_with_extension(input_directory, 'in')

    for input_file in input_files:
        solve_from_file(input_file, output_directory, params=params)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--all', action='store_true', help='If specified, the solver is run on all files in the input directory. Else, it is run on just the given input file')
    parser.add_argument('input', type=str, help='The path to the input file or directory')
    parser.add_argument('output_directory', type=str, nargs='?', default='.', help='The path to the directory where the output should be written')
    parser.add_argument('params', nargs=argparse.REMAINDER, help='Extra arguments passed in')
    args = parser.parse_args()
    output_directory = args.output_directory
    if args.all:
        input_directory = args.input
        solve_all(input_directory, output_directory, params=args.params)
    else:
        input_file = args.input
        solve_from_file(input_file, output_directory, params=args.params)
