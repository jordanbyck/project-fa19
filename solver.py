import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
import graph_maker
import student_utils
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
    # print("locations", list_of_locations)
    # print("homes", list_of_homes)
    # print("start", starting_car_location)
    # print("adj matrix", adjacency_matrix)
    # print("params", params)
    #
    # # lets try some Astar wooooooo
    #
    # # the number of TAs. Used for the goal test
    # numTAs = len(list_of_homes)
    #
    # # initially only add the start to the set of discovered nodes
    # openSet = {starting_car_location}
    #
    # # maps a node to the node that came before it in the path
    # path = {}
    #
    # # for a node, this is the cost of the cheapest path to that node
    # bestPathToNode = {}
    #
    # # this is the heuristics for each node. f = g + h
    # heuristics = {}
    #
    # # initialize all to infinity
    # for i in list_of_locations:
    #     bestPathToNode[i] = float("inf")
    #     heuristics[i] = float("inf")
    #
    # # set start to 0
    # bestPathToNode[starting_car_location] = 0
    # heuristics[starting_car_location] = 0
    #
    # while len(openSet) > 0:
    #
    #     # current is the node with the lowest heuristic value
    #     currentLowest = float("inf")
    #     current = None
    #     for key in heuristics.keys():
    #         if currentLowest > heuristics[key]:
    #             currentLowest = min(currentLowest, heuristics[key])
    #             current = key
    #
    #     # if we're at the goal, do some stuff
    #     if numTAs <= 0:
    #         # reconstruct the path
    #         return
    #
    #     openSet.remove(current)
    #     neighbors = findNeighbors(current)
    #
    #     # loop through all neighbors
    #     for neighbor in neighbors:
    #
    #         # dist(current, neighbor) is the weight of the edge from current to neighbor
    #         # possibleBestDist could be better than our known best distance in bestPathToNode
    #         possibleBestDist = bestPathToNode[current] + dist(current, neighbor)
    #
    #         if possibleBestDist < bestPathToNode[current]:
    #             # it is better so change the stuff
    #             path[neighbor] = current
    #             bestPathToNode[neighbor] = possibleBestDist
    #             heuristics[neighbor] = bestPathToNode[neighbor] + heuristicVal(neighbor)
    #
    #             if neighbor not in openSet:
    #                 openSet.add(neighbor)
    #
    # # failed

    # homes = []
    # for i in list_of_homes:
    #     homes.append(int(i))
    # print(practiceSolver.tspRepeats(adjacency_matrix, 0))
    # return [practiceSolver.tspRepeats(adjacency_matrix, 0)], {0: homes}

    #return trivial_output_solver(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix)


    # graphModifier.graphClusterer(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix)
    # practiceSolver.tspRepeats(adjacency_matrix)
    return trivial_output_solver(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix)

    # graphModifier.graphClusterer(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix)
    # practiceSolver.tspRepeats(adjacency_matrix)
    # return trivial_output_solver(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix)




def heuristicVal(node):
    return "yeeeeeee bro this is it"

def findNeighbors(node):
    return

def dist(node1, node2):
    # using networkx shortest_path function
    return nx.shortest_path()

def trivial_output_solver(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    G = student_utils.adjacency_matrix_to_graph(adjacency_matrix)[0]

    # helper function with access to G
    def distance_between_locations(a, b):
        path_dist = nx.shortest_path_length(G, a, b)
        print("distance from " + str(a) + " to " + str(b) +  ": ", path_dist)
        return path_dist

    # either proceed linearly through list of homes or through shuffled list of homes
    randomized_homes = np.random.shuffle(list_of_homes)
    homes = list_of_homes

    # using A* from start to each node
    total_path = []
    current_home = homes[0]
    total_path += nx.astar_path(G, int(starting_car_location), int(current_home), distance_between_locations)
    for next_home in homes[1:]:
        print("finding path between " + str(current_home) + " and " + str(next_home))
        path_between = nx.astar_path(G, int(starting_car_location), int(current_home), distance_between_locations)
        total_path += path_between
        current_home = next_home
    total_path += nx.astar_path(G, int(current_home), int(starting_car_location), distance_between_locations)
    print("total path: " + str(total_path))

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
