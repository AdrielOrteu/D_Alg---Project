import graph
import math
import sys
import queue
import heapq
from tracemalloc import start

# SalesmanTrackGreedy ==========================================================

def dijkstra (g, start, Visitas):
        cua_prioritat = []
        camino = []
        g.set_Dijkstra_Distance(start)
        g.set_Dijkstra_Visit()
        heapq.heappush(cua_prioritat, (0.0, start))
        while cua_prioritat:
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
        max_dist = sys.float_info.max
        next_jump = None
        for node in Visitas:
             if node.DijkstraDistance < max_dist:
                max_dist = node.DijkstraDistance
                next_jump = node

        return next_jump , camino
    
def SalesmanTrackGreedy(g,visits):
        if not g.Vertices or visits is None:
            return None
        g.set_Edge_dict()
        next_jump = visits[0]
        camino_total = []
        while visits:
            visits.remove(next_jump)
            next_jump, camino = dijkstra(g, visits[0], visits)
            camino_total.extend(camino)

        return graph.Track(g)
