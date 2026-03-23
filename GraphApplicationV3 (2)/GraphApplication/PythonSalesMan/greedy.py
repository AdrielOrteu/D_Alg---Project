
import math
import sys
import queue
import heapq

# SalesmanTrackGreedy ==========================================================

def dijkstra (g, start, Visitas):

    if not g.Vertices or start is None:
        return None
        
    g.set_Edge_dict()
    g.set_Dijkstra_Distance(start)
    g.set_Dijkstra_Visit()
    primer = True
    while Visitas:
        fora = 0
        if primera :
            cua_prioritat = []
            heapq.heappush(cua_prioritat, (0.0, start))
            primera = False
        else:
            maxim = sys.float_info.max
            node = None
            for vertex in Visitas:
                if vertex.DijkstraDistance < maxim:
                    maxim = vertex.DijkstraDistance
                    node = vertex
            Visitas.remove(node)
            cua_prioritat = []
            heapq.heappush(cua_prioritat, (0.0, node))
        while cua_prioritat and fora < len(Visitas):
            dist_actual, actual = heapq.heappop(cua_prioritat)
            if actual.DijktraVisit:
                continue
            
            actual.DijktraVisit = True
            if actual in Visitas:
                fora += 1
            for destination, edge in g.get_Edges(actual):
                if not destination.DijktraVisit:
                    # Calculem la nova distància potencial
                    nova_distancia = dist_actual + edge.Length
                    
                    # Si millorem la distància coneguda del destí
                    if nova_distancia < destination.DijkstraDistance:
                        destination.DijkstraDistance = nova_distancia
                        # Afegim a la cua amb heapq
                        heapq.heappush(cua_prioritat, (nova_distancia, destination))
                        
        return None
def SalesmanTrackGreedy(g,visits):

    return graph.Track(g)
