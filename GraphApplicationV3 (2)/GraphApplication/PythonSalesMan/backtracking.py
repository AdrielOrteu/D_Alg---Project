import graph
import math
import sys
import queue
import dijkstra

def SalesmanTrackBacktracking(g,visits):
    return graph.Track(g)

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
    best_cost = 
    dijkstra.DijkstraQueue(graph, node_actual)
    if visitas == []:
        return []
    for node in visitas:
        visitas.remove(node)
        cami, cost = SalesmanBackGreedyRec(node, visitas, graph, final)
        visitas.append(node)


