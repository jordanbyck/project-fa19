import sys, os, traceback, optparse
import time
import re
import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt

#from myUtility import *


def apprAlgorithm(G):
    # Find a minimum spanning tree T of G
    T = nx.minimum_spanning_tree(G, weight='weight')

    dfs = nx.dfs_preorder_nodes(T, '0');
    listnode = [];
    for item in dfs:
        listnode += [item]

    # Create the hamiltonian tour
    L = nx.Graph()
    L.add_nodes_from(G.nodes(data=True))

    cost = 0
    weight = nx.get_edge_attributes(G, 'weight')
    for index, item in enumerate(listnode):
        if index < len(G) - 1:
            L.add_edge(item, listnode[index + 1])
            cost += G[str(item)][str(listnode[index + 1])]['weight']
        else:
            L.add_edge(item, listnode[0])
            cost += G[str(item)][str(listnode[0])]['weight']

    return (cost, T, L, listnode)


def main():
    global options, args

    G = nx.read_graphml(args[0] + ".graphml")


    (cost, T, L, path) = apprAlgorithm(G)

    print("The cost of this tour:", cost)
    print("The tour:", path)

    # draw(G, L)


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'],
                                       version='$Id$')
        parser.add_option('-v', '--verbose', action='store_true', default=False, help='verbose output')
        (options, args) = parser.parse_args()
        # if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose: print(time.asctime())
        main()
        if options.verbose: print(time.asctime())
        if options.verbose: print('TOTAL TIME IN MINUTES:'),
        if options.verbose: print((time.time() - start_time) / 60.0)
        sys.exit(0)
    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
    except SystemExit as e:  # sys.exit()
        raise e
    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(str(e))
        traceback.print_exc()
        os._exit(1)