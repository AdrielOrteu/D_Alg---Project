import graph
import math
import sys
import heapq
import queue
import dijkstra



def SalesmanTrackBacktracking(g,visits):
    track = graph.Track(g)
    
    recc_backtracking_salesman(g=g,
                               track=track,
                               destinations=set(visits[1:-1]),
                               final_destination=visits[-1],
                               seen=set(),
                               best_len=math.inf,
                               position=visits[0])
    return track

def recc_backtracking_salesman(g, track, destinations: set, final_destination, seen: set, best_len: float, position=None):
    paths = []
    best_track = track
    if position is None: position = track.Edges[-1].Destination
    for v, e in g.Edge_dict[position].items():
        if v in seen: continue
        if track.Length + e.Length >= best_len: continue
        
        n_track = graph.Track(g)
        paths.append(n_track)
        n_track.AddLast(e)
        if v is final_destination and destinations == set():
            track.Append(n_track)
            return track.Length
        if v in destinations:
            destinations.remove(v)
            seen.clear()
        tmp_len = recc_backtracking_salesman(g, track, destinations, final_destination, seen) #TODO: recursion
        if tmp_len < best_len:
            best_len = tmp_len
            best_track = n_track
    
    track.Append(best_track)
    return best_len

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
