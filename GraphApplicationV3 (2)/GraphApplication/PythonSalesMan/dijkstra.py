import math
import sys
import queue

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
	g.set_Edge_dict()
	g.set_Dijkstra_Distance(start)
	dist = {node:math.inf for node in g.Vertices}
	visitat = {}
	anterior = {}
	
	dist[start] = 0
	
	for _ in range(len(g.Vertices)-1):
		neighbour_act = min_dist(dist, visitat)
		visitat[neighbour_act] = True
		for node2, edge in g.Edge_dict[neighbour_act].items():
			if node2 not in visitat:
				if dist[neighbour_act] + edge.Length < dist[node2]:
					dist[node2] = dist[neighbour_act] + edge.Length
					node2.DijkstraDistance = dist[neighbour_act] + edge.Length
					anterior[node2] = neighbour_act
	return None
# DijkstraQueue ================================================================

def DijkstraQueue(g ,start ):
	g.set_Edge_dict()
	g.set_Dijkstra_Distance(start)
	g.set_Dijkstra_Visit()
	cua_distancias = queue.PriorityQueue()
	cua_distancias.put((start, 0))
	acumulada = 0
	while cua_distancias.empty() == False:
		actual = cua_distancias.get()
		if actual[0].DijktraVisit == True:
			continue
		actual[0].DijktraVisit = True
		acumulada += actual[1]
		for destination, edge in g.get_Edges(actual[0]):
				if destination.DijktraVisit == False:
					cua_distancias.put((destination, edge.Length))
					if acumulada + edge.Length < destination.DijkstraDistance:
						destination.DijkstraDistance = acumulada + edge.Length
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
	
	from graph import Graph
	g = Graph()
	for v in vertices:
		g.NewVertex(v[0], v[1], v[2])
	for e in edges:
		g.NewEdge(e[0], e[1],
		          list(filter(lambda x: x.Name == e[2], g.Vertices))[0],
		          list(filter(lambda x: x.Name == e[3], g.Vertices))[0])
	g.SetDistancesToEdgeLength()
	start = g.FindVertex("Start", g.Vertices[0])
	
	Dijkstra(g, start)
	DijkstraQueue(g, start)
	print(g)
