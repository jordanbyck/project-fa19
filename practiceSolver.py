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
# import dwave_networkx as dnx
# import dimod
import solver
import student_utils



from student_utils import *

if __name__ == "__main__":
    solver.solve_from_file("inputs/10_50.in", "outputs")


def tspRepeats(matrix, start):

    """G = nx.Graph()
    edges = {(0, 1, 1), (1, 2, 1), (2, 3, 1)}
    G.add_weighted_edges_from(edges)"""
    G = student_utils.adjacency_matrix_to_graph(matrix)[0]


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
    returner = two_opt(B)

    def shift(seq, n):
        n = n % len(seq)
        return seq[n:] + seq[:n]
    for _ in range(len(returner)):
        if returner[_] == start:
            returner = shift(returner, _)

    #returner = shift(returner, 21)
    #print(returner)

    """path = []
    returnlen = len(returner)
    for _ in range(returnlen):"""


    return returner

def two_opt(graph, weight='weight'):
  num_nodes = graph.number_of_nodes()
  tour = list(graph.nodes())
  # min_cost = compute_tour_cost(graph, tour)
  start_again = True
  while start_again:
    start_again = False
    for i in range(0, num_nodes-1):
      for k in range(i+1, num_nodes):
        # 2-opt swap
        a, b = tour[i-1], tour[i]
        c, d = tour[k], tour[(k+1)%num_nodes]
        if (a == c) or (b == d):
          continue
        ab_cd_dist = graph.edges[a, b]['weight'] + graph.edges[c, d]['weight']
        ac_bd_dist = graph.edges[a, c]['weight'] + graph.edges[b, d]['weight']
        if ab_cd_dist > ac_bd_dist:
          tour[i:k+1] = reversed(tour[i:k+1])
          start_again = True
        if start_again:
          break
      if start_again:
        break
  return tour





