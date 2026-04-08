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
    best_cami = SalesmanBackGreedyRec(visits.Vertices[0], visits.Vertices[1:], visits.Vertices[-1], g)
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

def SalesmanBackGreedyRec(node_actual, visitas,final, graph):
    dijkstra.DijkstraQueue(graph, node_actual)
    if visitas == []:
        cami_fi = reconstrueix_cami(node_actual, final)
        return (final.dijkstraDistance, cami_fi)
    best_distancia = sys.float_info.max
    best_cami = None
    for node in visitas:
        visitas.remove(node)
        distancia, cami = (node.DijkstraDistance + SalesmanBackGreedyRec(node, visitas, final, graph)[0], reconstrueix_cami(node_actual, node) + SalesmanBackGreedyRec(node, visitas, final, graph)[1])
        visitas.append(node)
        if distancia < best_distancia:
            best_distancia = distancia
            best_cami = cami
    return best_cami

