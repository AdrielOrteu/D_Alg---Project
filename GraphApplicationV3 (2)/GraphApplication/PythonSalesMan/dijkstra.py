import graph
import math
import sys
import queue

# Dijkstra =====================================================================

def Dijkstra(g,start):
	pass

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

if __name__ == "__main__":
	vertices = [
		("Start", -17.03, 160.763),
		("V0002", 316.757, 177.112),
		("V0003", 444.823, 335.15),
		("V0004", -6.13079, 284.741)
	]
	edges = [
		("E0001", 0, "Start", "V0004"),
		("E0003", 0, "V0004", "V0002"),
		("E0005", 0, "Start", "V0003"),
		("E0007", 0, "V0002", "V0003"),
		("E0009", 0, "Start", "V0002")
	]
	
	from graph import Graph, Vertex, Edge
	g = Graph()
	for v in vertices:
		g.NewVertex(v[0], v[1], v[2])
	for e in edges:
		g.NewEdge(e[0], e[1], e[2], e[3])
	g.SetDistancesToEdgeLength()
	start = g.FindVertex("Start", g.Vertices[0])
	
	Dijkstra(g, start)
	#DijkstraQueue(g, start)
	print(g)
