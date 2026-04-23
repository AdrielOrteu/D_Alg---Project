import graph
import math
import sys
import queue
import dijkstra



def SalesmanTrackBacktracking(g,visits):
    track = graph.Track(g)
    
    recc_backtracking_salesman(g=g,
                               track=track,
                               destinations=set(visits[1:-1]),
                               final_destination=visits[-1],
                               seen=set(),
                               best_len=math.inf,
                               position=visits[0])
    return track

def recc_backtracking_salesman(g: graph.Graph, track: graph.Track, destinations: set, final_destination: graph.Vertex, seen: set, best_len: float, position=None):
    paths = []
    best_track = track
    if position is None: position = track.Edges[-1].Destination
    for v, e in g.Edge_dict[position].items():
        if v in seen: continue
        if track.Length + e.Length >= best_len: continue
        
        n_track = graph.Track(g)
        paths.append(n_track)
        n_track.AddLast(e)
        if v is final_destination and destinations == set():
            track.Append(n_track)
            return track.Length
        if v in destinations:
            destinations.remove(v)
            seen.clear()
        tmp_len = recc_backtracking_salesman(g, track, destinations, final_destination, seen) #TODO: recursion
        if tmp_len < best_len:
            best_len = tmp_len
            best_track = n_track
    
    track.Append(best_track)
    return best_len

# ==============================================================================

def SalesmanTrackBacktrackingGreedy(g, visits):
    track = graph.Track(g)
    if not g.Vertices or visits is None or  visits.Vertices == []:
        return track
    best_cami = SalesmanBackGreedyRec(visits.Vertices[0], visits.Vertices[1:], 0, g, visits.Vertices[-1])
    for e in best_cami:
        track.add_Edge(e)
    return graph.Track(g)

def reconstrueix_cami(start, node):
    cami = []
    while node != start:
        edge = node.WhereFrom
        cami.append(edge)
        node = edge.Origin
    cami.reverse()
    return cami

def SalesmanBackGreedyRec(node_actual, visitas, graph, final):
    best_cost = math.inf
    dijkstra.DijkstraQueue(graph, node_actual)
    if visitas == []:
        return []
    for node in visitas:
        visitas.remove(node)
        cami, cost = SalesmanBackGreedyRec(node, visitas, graph, final)
        visitas.append(node)


