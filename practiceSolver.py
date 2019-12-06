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
    solver.solve_from_file("test_inputs/test_10.in", "test_outputs")

def naiveSolve(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    G = student_utils.adjacency_matrix_to_graph(adjacency_matrix)
    print(G)
    return 0

def tspRepeats(G, start):
    #make a graph out of the matrix
    all_distances = dict(nx.floyd_warshall(G))

    #initialize graph of distances (complete graph with shortest paths as edges)
    B = G.copy()
    edges = {""}
    edges.pop()
    for _ in G.nodes:
        for __ in G.nodes:
            if not B.has_edge(_, __) and not __ == _:
                edges.add((_, __, all_distances[_][__]))
    B.add_weighted_edges_from(edges)
    #predecessors = nx.floyd_warshall_predecessor_and_distance(B)

    all_distances = dict(nx.floyd_warshall(B))

    #creates returner, a two-opt algorithm version of TSP on the shortest paths graph
    returner = two_opt(B)

    #shifts the array so the starting node is at the beginning of the array
    def shift(seq, n):
        n = n % len(seq)
        return seq[n:] + seq[:n]
    for _ in range(len(returner)):
        if returner[_] == start:
            returner = shift(returner, _)

    finalList = [returner[0]]
    for i in range(len(returner)-1):
        finalList += nx.shortest_path(G, returner[i], returner[i+1], weight='weight')[1:]
    finalList += nx.shortest_path(G, returner[-1], returner[0], weight='weight')[1:]

    return finalList

#copied from internet
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





