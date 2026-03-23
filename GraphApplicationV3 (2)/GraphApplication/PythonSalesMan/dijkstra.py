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
	if g.Vertices == [] or start == None:
		return None
	g.set_Dijkstra_Visit()
	cua_distancias = queue.PriorityQueue()
	cua_distancias.put((0,start))
	acumulada = 0
	while cua_distancias.empty() == False:
		dist , actual = cua_distancias.get()
		if actual.DijktraVisit == True:
			continue
		actual.DijktraVisit = True
		for destination, edge in g.get_Edges(actual):
				if destination.DijktraVisit == False:
					acumulada = dist + edge.Length
					if acumulada < destination.DijkstraDistance:
						destination.DijkstraDistance = acumulada
						cua_distancias.put((acumulada, destination))
	return None