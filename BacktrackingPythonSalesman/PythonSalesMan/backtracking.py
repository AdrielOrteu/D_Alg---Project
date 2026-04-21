import graph
import math
import sys
import queue
import dijkstra

def SalesmanTrackBacktracking(g,visits):
    return graph.Track(g)

def recc_backtracking_salesman(g, path, destinations):
    paths = []
    
    for n in g.get_Edges(path[-1]):
    
    best_path = min(paths, key=lambda x: x[1])
    return best_path

# ==============================================================================

def SalesmanTrackBacktrackingGreedy(g, visits):
    return graph.Track(g)

