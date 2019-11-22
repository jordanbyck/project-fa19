import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils

from student_utils import *

def findClusters(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    G = adjacency_matrix.adjacency_matrix_to_graph()
    

    return