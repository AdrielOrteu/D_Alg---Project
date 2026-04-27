from multiprocessing import heap

import graph
import math
import sys
import queue
import dijkstra
import heapq
from backtracking import reconstrueix_cami, dijkstra
   
# SalesmanTrackBranchAndBound1 ===================================================

def SalesmanTrackBranchAndBound1(g, visits):
    track = graph.Track(g)
    dict_espai = [[math.inf] * len(visits.Vertices) for _ in range(len(visits.Vertices))]
    where_from = [{} for _ in range(len(visits.Vertices))]
    for index, node in enumerate(visits.Vertices):
        dijkstra(g, node)
        dict_espai[index][index] = 0
        for index2, node2 in enumerate(visits.Vertices):
            dict_espai[index][index2] = node2.DijkstraDistance
            path = reconstrueix_cami(node, node2)
            where_from[index][index2] = path
    
    start = 0
    final = len(visits.Vertices)-1
    visitas = [n for n in range(1, len(visits.Vertices)-1)]
    siguiente = start
    camino_final = []
    camino = []
    cua = []
    heuristica = 0
    tupla = (heuristica, camino, siguiente, visitas)
    heapq.heappush(cua, tupla)

    solucio = True
    while solucio:
        heuritica, camino, siguiente, visitas = heapq.heappop(cua)
        if siguiente == final:
            camino_final = camino 
            solucio = False
        elif visitas == []:
            heuristica = heuristica + dict_espai[siguiente][final]
            camino += where_from[siguiente][final]
            siguiente = final
            visitas = []
            heapq.heappush(cua, (heuristica, camino, siguiente, visitas))
        else:
            for node in visitas:
                nou_camino = camino + where_from[siguiente][node]
                heuritsica = heuristica + dict_espai[siguiente][node]
                visitas = [v for v in visitas if v != node]
                heapq.heappush(cua, (heuritsica, nou_camino, node, visitas))
    for e in camino_final:
        track.AddLast(e)

    return track



# SalesmanTrackBranchAndBound2 ===================================================

def SalesmanTrackBranchAndBound2(g, visits):
    return graph.Track(g)

# SalesmanTrackBranchAndBound3 ===================================================

def SalesmanTrackBranchAndBound3(g, visits):
    return graph.Track(g)
	