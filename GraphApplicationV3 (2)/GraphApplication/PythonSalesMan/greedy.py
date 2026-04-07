import math
import graph
import sys
import queue
import copy
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
                        destination.WhereFrom = edge
        min_dist = sys.float_info.max
        next_jump = None
        for node in Visitas:
            if node.DijkstraDistance < min_dist:
                min_dist = node.DijkstraDistance
                next_jump = node
        
        while next_jump != start:
            edge = next_jump.WhereFrom
            camino.append(edge)
            next_jump = edge.Origin
        camino.reverse()

        return camino[-1].Destination , camino
    
def SalesmanTrackGreedy(g,visits):
        track = graph.Track(g)
        if not g.Vertices or visits is None or  visits.Vertices == []:
            return track
        actual = visits.Vertices[0]
        visitas = visits.Vertices[1:-1]
        n_final = visits.Vertices[-1]
        while len(visitas) > 0:
            next_jump, camino = dijkstra(g, actual, visitas)
            visitas.remove(next_jump)
            for edge in camino:
                track.AddLast(edge)
            actual = next_jump
        _, camino = dijkstra(g, actual, [n_final])
        for edge in camino:
            track.AddLast(edge)
        return track
