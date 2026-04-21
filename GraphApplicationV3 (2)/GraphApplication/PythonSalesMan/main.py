import graph
import subprocess
import sys
import time
import dijkstra
import greedy
import backtracking
import branchAndBound

# ==============================================================================
# IDENTIFICACIO DELS ALUMNES ===================================================
# ==============================================================================

graph.NomAlumne1 = "Diogo"
graph.CognomsAlumne1 = "da Costa Lã Cabrita Teixeira"
graph.NIUAlumne1 = "1751533"

# No modificar si nomes grup d'un alumne

graph.NomAlumne2 = "Adriel"
graph.CognomsAlumne2 = "Orteu Portocarrero"
graph.NIUAlumne2 = "1750927"

# VERIFICAR ALUMNES =============================================================

graph.TestNIU(graph.NIUAlumne1)
if graph.NIUAlumne2!="": graph.TestNIU(graph.NIUAlumne2)


# EXECUCIO EN PROCESS DE CORRECCIO ==============================================

isCorrection = graph.CorrectionProcess()
if isCorrection == False:

	# ==============================================================================
	# PROVES =======================================================================
	# ==============================================================================

	g=graph.Graph()                     					# crear un graf
	g.Load("TestDijkstra/Desconectat.GR")     					# llegir el graf
	g.SetDistancesToEdgeLength()        					# Posar les longituts de les arestes a la distancia entre vertexs
	start=g.GetVertex("Start");         					# Obtenir el vertex origien de les distancies (distancia 0)
	t0 = time.time()                    					# temps inicial
	dijkstra.Dijkstra(g,start)          					# Calcular les distancies
	t1 = time.time()                    					# Temps final
	print("temps: ",t1-t0)              					# imprimir el temps d'execució
	g.DisplayDistances()                					# Visualitza el graf i les distancies

	g=graph.Graph()                     					# crear un graf
	g.Load("TestSalesMan/Graf10_20_3.GR")  				# llegir el graf
	g.SetDistancesToEdgeLength()        					# Posar les longituts de les arestes a la distancia entre vertexs
	vis=graph.Visits(g);									# Crear visites
	vis.Load("TestSalesMan/Graf10_20_3.VIS")				# Llegir les vistes
	t0 = time.time()                    					# temps inicial

	#Cerca cami que pasi per les visites
	#trk=greedy.SalesmanTrackGreedy(g,vis)                       #test greedy   
	trk=backtracking.SalesmanTrackBacktracking(g,vis)          #test backtracking
	#trk=backtracking.SalesmanTrackBacktrackingGreedy(g,vis)    #test backtracking-greedy
	#trk=branchAndBound.SalesmanTrackBranchAndBound2(g,vis)     #test branch&bound

	t1 = time.time()                    					# Temps final
	print("temps: ",t1-t0)              					# imprimir el temps d'execució
	trk.Display(vis)                    					# Visualitza el track i les visites sobre el graf el graf