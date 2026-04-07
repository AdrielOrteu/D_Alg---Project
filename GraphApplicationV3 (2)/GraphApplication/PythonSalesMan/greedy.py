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
        fora = 0
        while cua_prioritat or fora < len(Visitas):
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

        min_dist = sys.float_info.max
        next_jump = None
        for node in Visitas:
             if node.DijkstraDistance < min_dist:
                min_dist = node.DijkstraDistance
                next_jump = node
                camino = g.get_Edge_from_dict(start, node)
        return next_jump , camino
    
def SalesmanTrackGreedy(g,visits):
        if not g.Vertices or visits is None or  visits.Vertices == []:
            return None
        track = graph.Track(g)
        next_jump = visits.Vertices[0]
        visitas = visits.Vertices[1:-2]
        while len(visits.Vertices) > 1: 
            visitas.remove(next_jump)
            track.AddVertex(next_jump)
            if next_jump != visits.Vertices[-1]:
                next_jump, camino = dijkstra(g, next_jump, visitas)
        track.AddLastVertex(camino)
        return track
