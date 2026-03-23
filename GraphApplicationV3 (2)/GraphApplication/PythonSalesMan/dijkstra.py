import graph
import math
import sys
import queue

# Dijkstra =====================================================================

def Dijkstra(g,start):
	return None

# DijkstraQueue ================================================================

def DijkstraQueue(g ,start ):
	g.set_Edge_dict()
	g.set_Dijkstra_Distance(start)
	g.set_Dijkstra_Visit()
	cua_distancias = queue.PriorityQueue()
	cua_distancias.put((0,start))
	acumulada = 0
	while cua_distancias.empty() == False:
		actual = cua_distancias.get()
		if actual[1].DijktraVisit == True:
			continue
		actual[1].DijktraVisit = True
		for destination, edge in g.get_Edges(actual[1]):
				if destination.DijktraVisit == False:
					acumulada = actual[1].DijkstraDistance + edge.Length
					if acumulada < destination.DijkstraDistance:
						destination.DijkstraDistance = acumulada
						cua_distancias.put((edge.Length, destination))
	return None