import math
import sys
import queue
import heapq

# Dijkstra =====================================================================

def min_dist(dist, visitat):
	m = math.inf
	r = None
	for n, d in dist.items():
		if n not in visitat:
			if d < m:
				m = d
				r = n
	return r

def Dijkstra(g,start):
	if g.Vertices == [] or start == None:
		return None
	
	g.set_Dijkstra_Distance(start)
	dist = {node:math.inf for node in g.Vertices}
	visitat = {}
	anterior = {}
	
	dist[start] = 0
	
	for _ in range(len(g.Vertices)-1):
		neighbour_act = min_dist(dist, visitat)
		visitat[neighbour_act] = True
		for node2, edge in g.get_Edges(neighbour_act):
			if node2 not in visitat:
				if dist[neighbour_act] + edge.Length < dist[node2]:
					dist[node2] = dist[neighbour_act] + edge.Length
					node2.DijkstraDistance = dist[neighbour_act] + edge.Length
					anterior[node2] = neighbour_act
	return None
# DijkstraQueue ================================================================

def DijkstraQueue(g ,start ):
	if g.Vertices == [] or start == None:
		return None
	g.set_Dijkstra_Visit()
	g.set_Dijkstra_Distance(start)
	cua_distancias = queue.PriorityQueue()
	cua_distancias.put((0.0, start))
	acumulada = 0.0
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
	#edges = [
	#	("E0001", 0, "Start", "V0004"),
	#	("E0003", 0, "V0004", "V0002"),
	#	("E0005", 0, "Start", "V0003"),
	#	("E0007", 0, "V0002", "V0003"),
	#	("E0009", 0, "Start", "V0002")
	#]
	
	from graph import Graph
	g = Graph()
	for v in vertices:
		g.NewVertex(v[0], v[1], v[2])
	#for e in edges:
	#	g.NewEdge(e[0], e[1],
	#	          list(filter(lambda x: x.Name == e[2], g.Vertices))[0],
	#	          list(filter(lambda x: x.Name == e[3], g.Vertices))[0])
	g.SetDistancesToEdgeLength()
	start = g.FindVertex("Start", g.Vertices[0])
	g.Edge_dict = {v1:{e.Destination:e for e in g.Edges if e.Origin == v1} for v1 in g.Vertices}
	
	Dijkstra(g, start)
	#DijkstraQueue(g, start)
	print(g)
