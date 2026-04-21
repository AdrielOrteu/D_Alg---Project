import graph
import math
import sys
import queue
import dijkstra
from copy import deepcopy

def SalesmanTrackBacktracking(g,visits):
    track = graph.Track(g)
    track.Vertices.add(visits[0])
    return track

# CHANGE TO COMMIT
def recc_backtracking_salesman(g, track: graph.Track, destinations):
    paths = []
    
    for v in g.get_Edges(track.Edges[-1].Destination):
        tmp_track = deepcopy(track)
        if v in destinations:
            tmp_track.Vertices.add(v)
            return
        elif v in track.Vertices:
            continue
        
        
    
    best_path = min(paths, key=lambda x: x[1])
    return best_path

# ==============================================================================

def SalesmanTrackBacktrackingGreedy(g, visits):
    return graph.Track(g)

