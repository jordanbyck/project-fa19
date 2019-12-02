import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
import graph_maker
#sys.path.append("/Users/jordanbyck/anaconda3/lib/python3.6/site-packages")
import networkx as nx
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import dwave_networkx as dnx
import dimod

from student_utils import *


"""def jordanSolve(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    dnx.traveling_salesperson(G, dimod.ExactSolver(), start=0)
    return"""

def jordanHelper():
    G = nx.Graph()
    G.add_weighted_edges_from({(0, 1, .1), (0, 2, .5), (0, 3, .1), (1, 2, .1), (1, 3, .5), (2, 3, .1)})

    result = dnx.traveling_salesperson(G, dimod.ExactSolver(), start=0)
    print(result)
    return result