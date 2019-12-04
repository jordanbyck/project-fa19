import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import solver
import student_utils

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
    clusters = findClusterCenters(graph, list_of_locations, num_clusters, adjacency_matrix, starting_car_location)

    return

def findClusterCenters(graph, list_of_locations, num_clusters, adjacency_matrix, starting_car_location):

    # start by just adding the starting position mapped to its neighbors
    clusters = {}

    print(list(graph.neighbors(starting_car_location)))
    clusters[starting_car_location] = list(graph.neighbors(starting_car_location))

    cluster_coefficients = nx.clustering(graph, graph.nodes, "weight")
    
    print("c", cluster_coefficients)



    return

if __name__ == "__main__":
    solver.solve_from_file("inputs/10_50.in", "outputs")
