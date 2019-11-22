import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import solver

def print_map(locations, homes):
    np.set_printoptions(threshold=sys.maxsize)

    #LOCATIONS
    l = locations

    #HOMES
    h = homes

    #Names of Locations

    locations = list()
    for i in range(1,l+1):
        locations.append(i)

    #Names of Homes
    homes = random.sample(range(1,l),h)

    #first input param needs to be l, second is up to us
    #f = nx.dense_gnm_random_graph(l,100)
    f = nx.connected_watts_strogatz_graph(l,10,1)

    for i in f.edges():
        f[i[0]][i[1]]['weight'] = np.random.randint(100,199)

    labels = nx.get_edge_attributes(f, 'weight')
    nx.draw(f, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(f, pos=nx.spring_layout(f), edge_labels=labels)
    plt.show()

    adj = nx.to_numpy_matrix(f)
    #print(adj)
    #print("done")
    adj_list = adj.tolist()
    #print(adj_list)

    for i in range(0,l):
        for j in range(0,l):
            if adj_list[i][j] == 0:
                adj_list[i][j] = 'x'
            else:
                adj_list[i][j]= '1'

    print_input(locations, homes, adj_list)

def print_input(locations, homes, adj_list):
    # number of locations
    print(len(locations))
    # number of homes
    print(len(homes))
    # locations
    print(locations)
    # homes
    print(homes)
    # starting location
    print(np.random.choice(locations))
    # adjacency list
    separator = " "
    for row in adj_list:
        print(separator.join(row))

if __name__ == "__main__":
    print_map(locations=50, homes=25)
