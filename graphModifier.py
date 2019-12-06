import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import solver
import student_utils
from networkx.algorithms import community

def graphClusterer(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix):

    graph = student_utils.adjacency_matrix_to_graph(adjacency_matrix)[0]

    # this is used to draw the graph
    # labels = nx.get_edge_attributes(graph, 'weight')
    # nx.draw(graph, with_labels=True, font_weight='bold')
    # nx.draw_networkx_edge_labels(graph, pos=nx.spring_layout(graph), edge_labels=labels)
    # plt.show()

    num_clusters = (len(list_of_locations) // 10) + 1
    list_of_locations = [int(i) for i in list_of_locations]
    starting_car_location = int(starting_car_location)
    list_of_homes = [int(i) for i in list_of_homes]


    # will return a list a clusters
    print("homes", list_of_homes)
    clusters = findClusterCenters(graph, list_of_locations, num_clusters, adjacency_matrix, starting_car_location)

    return

def findClusterCenters(graph, list_of_locations, num_clusters, adjacency_matrix, starting_car_location):

    # start by just adding the starting position mapped to its neighbors
    clusters = {}

    print(list(graph.neighbors(starting_car_location)))
    clusters[starting_car_location] = list(graph.neighbors(starting_car_location))

    all_max_cliques = nx.find_cliques(graph)
    all_cliques = nx.enumerate_all_cliques(graph)

    print("====")

    for cliq in all_max_cliques:
        print(cliq)

    print("===")

    # for cliq in all_cliques:
    #     print(cliq)

    # maps nodes to a list which is their clique
    seen_nodes = {}

    for cliq in all_cliques:
        cliq_len = len(cliq)

        for node in cliq:
            if node in set(seen_nodes.keys()):
                if len(seen_nodes[node]) < cliq_len:
                    seen_nodes[node] = cliq
            else:
                seen_nodes[node] = cliq

    print(seen_nodes)

    return

if __name__ == "__main__":
    solver.solve_from_file("inputs/10_50.in", "outputs")
