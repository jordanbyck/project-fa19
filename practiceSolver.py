import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
import graph_maker
#sys.path.append("/Users/jordanbyck/anaconda3/lib/python3.6/site-packages/")
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

def TSPSolver():
    G = nx.Graph()
    edges = {""}
    edges.pop()
    for _ in range(3):
        for __ in range(3):
            if not (_, __, .1) in edges and not (__, _, .1) in edges and not __ == _:
                edges.add((_, __, .1))


    G.add_weighted_edges_from(edges)
    print(G.number_of_nodes())
    print(G.number_of_edges())
    print(edges)
    h = {'a': -0.5, 'b': 1.0}
    J = {('a', 'b'): -1.5}
    """sampler = dimod.RandomSampler()
    h = {0: -1, 1: -1}
    J = {(0, 1): -1}
    bqm = dimod.BinaryQuadraticModel(h, J, -0.5, dimod.SPIN)"""
    """#result = dnx.traveling_salesperson(G, dimod.ExactPolySolver(), start=0)
    result = dnx.traveling_salesperson_qubo(G)#, dimod.SimulatedAnnealingSampler().sample_ising(h, J), start=0)
    answer = QBSolv().sample_qubo(result, 50)

    #result = dnx.traveling_salesperson(G, sampler.sample(bqm, num_reads=3), start=0)"""
    return

def tspRepeats():

    G = nx.Graph()
    edges = {(0, 1, 1), (1, 2, 1), (2, 3, 1)}
    G.add_weighted_edges_from(edges)


    #predecessors = nx.floyd_warshall_predecessor_and_distance(G)
    all_distances = dict(nx.floyd_warshall(G))

    B = nx.Graph()
    edges = {""}
    edges.pop()
    for _ in G.nodes:
        for __ in G.nodes:
            if not (_, __, all_distances[_][__]) in edges and not (__, _, all_distances[_][__]) in edges and not __ == _:
                edges.add((_, __, all_distances[_][__]))

    B.add_weighted_edges_from(edges)
    #predecessors = nx.floyd_warshall_predecessor_and_distance(B)
    all_distances = dict(nx.floyd_warshall(B))
    return dnx.traveling_salesperson(B, dimod.ExactPolySolver(), start=1)


tspRepeats()



