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
	cua_distancias.put((start, 0))
	acumulada = 0
	while cua_distancias:
		actual = cua_distancias.get()
		if actual[0].DijktraVisit == False:
			actual[0].DijktraVisit
			acumulada += actual[1]
			for destination, edge in g.get_Edges(actual):
				if destination.DijkstraVisit == False:
					cua_distancias.put(edge.Origin, edge.Length)
					if acumulada + edge.Length < destination.DijkstraDistance:
						destination.DijkstraDistance = acumulada + edge.Length
	return None