import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import solver
import input_validator
import output_validator
import student_utils
import snowflake_graph_maker

def make_random_graph(locations, homes):
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

    adj_list = adj.tolist()

    for i in range(0,l):
        for j in range(0,l):
            if adj_list[i][j] == 0:
                adj_list[i][j] = 'x'
            else:
                adj_list[i][j] = '1'

    print_input(locations, homes, adj_list)

def make_custom_graph(locations, homes):

    # num locations
    l = locations

    # num homes
    h = homes




# prints output and writes to a file "[number of locations].in"
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
    newline = "\n"
    for row in adj_list:
        print(separator.join(row))

    # create a file
    file = open(str(len(locations)) + ".in", "w+")

    # write the number of locations
    file.write(str(len(locations)) + newline)

    # write the number of homes
    file.write(str(len(homes)) + newline)

    # write the locations
    file.write(separator.join(str(location) for location in locations) + newline)

    # write the homes
    file.write(separator.join(str(home) for home in homes) + newline)

    # write starting location
    file.write(str(np.random.choice(locations)) + newline)

    # write the adj list
    for row in adj_list:
        file.write(separator.join(row) + newline)
    file.close()

# this is going to move 1 node away from start, drop everyone off, then return to start
def print_trivial_output(numLocations, startingLocation, taHomes):

    # create the file
    file = open(str(numLocations) + ".out", "w+")

    separator = " "
    newLine = "\n"

    # write the path
    file.write(str(startingLocation) + newLine)

    # write the number of drop offs which is 1
    file.write("1" + newLine)

    # write the drop off location, followed by every TA's home
    file.write(str(startingLocation))
    for home in taHomes:
        file.write(separator + str(home))

    file.close()

if __name__ == "__main__":
    make_random_graph(locations=50, homes=25)
    input_validator.validate_input(input_file="50.in")
    solver.solve_from_file("50.in", "project-fa19")
    output_validator.validate_output(input_file="50.in", output_file="50.out")

    # make_random_graph(locations=50, homes=25)
    # input_validator.validate_input(input_file="50.in")

    # twentyfive_graph = snowflake_graph_maker.snowflake_maker(locations=25, homes=8, intermediates=2)
    hundred_graph = snowflake_graph_maker.snowflake_maker(locations=100, homes=33, intermediates=2)

