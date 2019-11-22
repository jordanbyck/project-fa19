import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
# import solver

def make_graph():
    np.set_printoptions(threshold=sys.maxsize)


    #LOCATIONS
    l = 50

    #HOMES
    h = 25

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
    #
    for i in range(0,l):
        for j in range(0,l):
            if adj_list[i][j] == 0:
                adj_list[i][j] = 'x'

    print(l)
    print(h)
    print(*locations, sep=" ")
    print(*homes, sep=" ")
    print(np.random.randint(1,l+1))
    #print('\n'.join([' '.join(['{:1}'.format(item) for item in row])
    #for row in adj_list]))

def print_input_file(numLocations, numHomes, locationNames, homeNames, adjList):
    file = open("50.in", "w+")
    file.write(numLocations)
    file.write(numHomes)
    file.write(locationNames)
    file.write(homeNames)


if __name__ == "__main__":
    make_graph()
    #solver.solve_from_file()
