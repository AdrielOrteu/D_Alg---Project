import graph
import math
import sys
import heapq
import queue
import dijkstra



def SalesmanTrackBacktracking(g,visits):
    track = graph.Track(g)
    start = visits.Vertices[0]
    final = visits.Vertices[-1]
    visitas = visits.Vertices[1:-1]
    visitats = set()
    visitats.add(start)


    cami , cost =backtracking(g, start, final, visitas, visitats, 0, [])
    
    for e in cami:
        track.AddLast(e)
    return track

def backtracking(g, node_actual, final, visitas, visitats, cost_actual, cami_actual):
    if node_actual == final and visitas == []:
        return cami_actual , cost_actual
    best_cami = None
    best_cost = math.inf
    for dest, edge in g.get_Edges(node_actual):
        if dest in visitats:
            continue
        path = cami_actual + [edge]
        new_cost = cost_actual + edge.Length
        if dest in visitas:
            visitats_new = set()
            visitats_new.add(dest)
            visitas.remove(dest)
            cami_res, cost_res = backtracking(g, dest, final, visitas, visitats, new_cost, path)
            visitas.append(dest)
        else:
            visitats.add(dest)
            cami_res, cost_res = backtracking(g, dest, final, visitas, visitats, new_cost, path)
            visitats.remove(dest)
        if cami_res is not None and cost_res < best_cost:
            best_cami = cami_res
            best_cost = cost_res
    return best_cami, best_cost

# ==============================================================================

def reconstrueix_cami(start, node):
    cami = []
    while node != start:
        edge = node.WhereFrom
        if edge.Origin == node:
            edge = edge.ReverseEdge
            node.WhereFrom = edge
        cami.append(edge)
        node = edge.Origin
    cami.reverse()
    return cami

def dijkstra (g, start):
        cua_prioritat = []
        g.set_Dijkstra_Distance(start)
        g.set_Dijkstra_Visit()
        heapq.heappush(cua_prioritat, (0.0, start))
        while cua_prioritat:
            dist_actual, actual = heapq.heappop(cua_prioritat)
            if actual.DijktraVisit:
                continue
            actual.DijktraVisit = True
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


def SalesmanTrackBacktrackingGreedy(g, visits):
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
    best_cami = []
    best_cost = [math.inf]

    start = 0
    visitas = list(range(1, len(visits.Vertices)-1))
    final = len(visits.Vertices)-1

    best_cami = backtrackingGreedy(start, final, visitas, where_from, dict_espai, 0, [], best_cost)
    for e in best_cami:
        track.AddLast(e)
    return track

def backtrackingGreedy(node_actual, final, visitas, where_from, dict_espai,  cost ,camino, best_cost):
    if cost > best_cost[0]:
        return []
    if visitas == []:
        cost = cost + dict_espai[node_actual][final]
        if cost < best_cost[0]:
            best_cost[0] = cost
            best_cami = camino + where_from[node_actual][final]
            return best_cami
        return []
    best_cami = []
    for node in visitas:
        nou_cost = cost + dict_espai[node_actual][node]
        if nou_cost >= best_cost[0]:
            continue
        nou_camino = camino + where_from[node_actual][node]
        nova_visitas = [v for v in visitas if v != node]
        cami_res = backtrackingGreedy(node, final, nova_visitas, where_from, dict_espai, nou_cost, nou_camino, best_cost)
        if cami_res != []:
            best_cami = cami_res
    
    return best_cami
