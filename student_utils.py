import networkx as nx
import numpy as np
import scipy as sp


def decimal_digits_check(number):
    number = str(number)
    parts = number.split('.')
    if len(parts) == 1:
        return True
    else:
        return len(parts[1]) <= 5


def data_parser(input_data):
    number_of_locations = int(input_data[0][0])
    number_of_houses = int(input_data[1][0])
    list_of_locations = input_data[2]
    list_of_houses = input_data[3]
    starting_location = input_data[4][0]

    adjacency_matrix = [[entry if entry == 'x' else float(entry) for entry in row] for row in input_data[5:]]
    return number_of_locations, number_of_houses, list_of_locations, list_of_houses, starting_location, adjacency_matrix


def adjacency_matrix_to_graph(adjacency_matrix):
    node_weights = [adjacency_matrix[i][i] for i in range(len(adjacency_matrix))]
    adjacency_matrix_formatted = [[0 if entry == 'x' else entry for entry in row] for row in adjacency_matrix]

    for i in range(len(adjacency_matrix_formatted)):
        adjacency_matrix_formatted[i][i] = 0

    G = nx.convert_matrix.from_numpy_matrix(np.matrix(adjacency_matrix_formatted))

    message = ''

    for node, datadict in G.nodes.items():
        if node_weights[node] != 'x':
            message += 'The location {} has a road to itself. This is not allowed.\n'.format(node)
        datadict['weight'] = node_weights[node]

    return G, message

#Adds 50 nodes to the graph G, with one node in the middle where all the other nodes are coming from

def fiftygraphmaker(G, a):
    G.add_nodes_from(range(a, 50 + a))
    for _ in range(6):
        G.add_edge((_ * 7) + 1 + a, (_ * 7) + 2 + a)
        G.add_edge((_ * 7) + 2 + a, (_ * 7) + 3 + a)
        G.add_edge((_ * 7) + 3 + a, (_ * 7) + 4 + a)
        G.add_edge((_ * 7) + 4 + a, (_ * 7) + 5 + a)
        G.add_edge((_ * 7) + 5 + a, (_ * 7) + 6 + a)
        G.add_edge((_ * 7) + 6 + a, (_ * 7) + 7 + a)
    G.add_edge(a, 1 + a)
    G.add_edge(a, 8 + a)
    G.add_edge(a, 15 + a)
    G.add_edge(a, 22 + a)
    G.add_edge(a, 29 + a)
    G.add_edge(a, 36 + a)
    G.add_edge(a, 43 + a)
    return G

#Generates a graph with 50 nodes, using 50graphmaker

def fiftygraph():
    G = nx.Graph()
    G = fiftygraphmaker(G, 0)
    return G

#Same as fiftygraph, but graph be more bigger

def hundredgraph():
    G = nx.Graph()
    G = fiftygraphmaker(G, 0)
    G = fiftygraphmaker(G, 50)
    G.add_edge(0, 50)
    return G

#CHONK

def twohundredgraph():
    G = nx.Graph()
    G = fiftygraphmaker(G, 0)
    G = fiftygraphmaker(G, 50)
    G = fiftygraphmaker(G, 100)
    G = fiftygraphmaker(G, 150)
    G.add_edge(0, 50)
    G.add_edge(50, 100)
    G.add_edge(100, 150)
    return G

#prints the graph in the correct format for the

def graph_printer(G):
    matrix = nx.adjacency_matrix(G).toarray()
    #print(matrix)
    printlist = ""
    for _ in range(len(matrix)):
        for x in range(len(matrix)):
            printlist += matrix[_][x]
        print(printlist)
        printlist = ""
    return

def is_metric(G):
    shortest = dict(nx.floyd_warshall(G))
    for u, v, datadict in G.edges(data=True):
        if abs(shortest[u][v] - datadict['weight']) >= 0.00001:
            return False
    return True


def adjacency_matrix_to_edge_list(adjacency_matrix):
    edge_list = []
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[0])):
            if adjacency_matrix[i][j] == 1:
                edge_list.append((i, j))
    return edge_list


def is_valid_walk(G, closed_walk):
    return all([(closed_walk[i], closed_walk[i+1]) in G.edges for i in range(len(closed_walk) - 1)])


def get_edges_from_path(path):
    return [(path[i], path[i+1]) for i in range(len(path) - 1)]

"""
G is the adjacency matrix.
car_cycle is the cycle of the car in terms of indices.
dropoff_mapping is a dictionary of dropoff location to list of TAs that got off at said droppoff location
in terms of indices.
"""
def cost_of_solution(G, car_cycle, dropoff_mapping):
    cost = 0
    message = ''
    dropoffs = dropoff_mapping.keys()
    if not is_valid_walk(G, car_cycle):
        message += 'This is not a valid walk for the given graph.\n'
        cost = 'infinite'

    if not car_cycle[0] == car_cycle[-1]:
        message += 'The start and end vertices are not the same.\n'
        cost = 'infinite'
    if cost != 'infinite':
        if len(car_cycle) == 1:
            car_cycle = []
        else:
            car_cycle = get_edges_from_path(car_cycle[:-1]) + [(car_cycle[-2], car_cycle[-1])]
        driving_cost = sum([G.edges[e]['weight'] for e in car_cycle]) * 2 / 3
        walking_cost = 0
        shortest = dict(nx.floyd_warshall(G))

        for drop_location in dropoffs:
            for house in dropoff_mapping[drop_location]:
                walking_cost += shortest[drop_location][house]

        message += f'The driving cost of your solution is {driving_cost}.\n'
        message += f'The walking cost of your solution is {walking_cost}.\n'
        cost = driving_cost + walking_cost

    message += f'The total cost of your solution is {cost}.\n'
    return cost, message


def convert_locations_to_indices(list_to_convert, list_of_locations):
    return [list_of_locations.index(name) if name in list_of_locations else None for name in list_to_convert]
