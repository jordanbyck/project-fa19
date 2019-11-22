import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils


def findDistances(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    G = adjacency_matrix.adjacency_matrix_to_graph()
    graphSize = G.nodes.size()
    distances = {}
    for _ in G.nodes:
        print(1)
    return