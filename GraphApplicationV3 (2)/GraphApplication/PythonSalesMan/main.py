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

graph.NomAlumne1 = "nombre del alumno 1"
graph.CognomsAlumne1 = "apellidos del alumno 1"
graph.NIUAlumne1 = ""

# No modificar si nomes grup d'un alumne

graph.NomAlumne2 = "nombre del alumno 2"
graph.CognomsAlumne2 = "apellidos del alumno 2"
graph.NIUAlumne2 = ""

# VERIFICAR ALUMNES =============================================================

graph.TestNIU(graph.NIUAlumne1)
if graph.NIUAlumne2!="": graph.TestNIU(graph.NIUAlumne2)


# EXECUCIO EN PROCESS DE CORRECCIO ==============================================

isCorrection = graph.CorrectionProcess()
if isCorrection == False:

	# ==============================================================================
	# PROVES =======================================================================
	# ==============================================================================

	#g=graph.Graph()                     					# crear un graf
	#g.Load("TestDijkstra/Graf4.GR")     					# llegir el graf
	#g.SetDistancesToEdgeLength()        					# Posar les longituts de les arestes a la distancia entre vertexs
	#start=g.GetVertex("Start");         					# Obtenir el vertex origien de les distancies (distancia 0)
	#t0 = time.time()                    					# temps inicial
	#dijkstra.Dijkstra(g,start)          					# Calcular les distancies
	#t1 = time.time()                    					# Temps final
	#print("temps: ",t1-t0)              					# imprimir el temps d'execució
	#g.DisplayDistances()                					# Visualitza el graf i les distancies

	g=graph.Graph()                     					# crear un graf
	g.Load("TestSalesMan/RepeatVertex.GR")  				# llegir el graf
	g.SetDistancesToEdgeLength()        					# Posar les longituts de les arestes a la distancia entre vertexs
	vis=graph.Visits(g);									# Crear visites
	vis.Load("TestSalesMan/RepeatVertex.VIS")				# Llegir les vistes
	t0 = time.time()                    					# temps inicial

	#Cerca cami que pasi per les visites
	trk=greedy.SalesmanTrackGreedy(g,vis)                       #test greedy   
	#trk=backtracking.SalesmanTrackBacktracking(g,vis)          #test backtracking
	#trk=backtracking.SalesmanTrackBacktrackingGreedy(g,vis)    #test backtracking-greedy
	#trk=branchAndBound.SalesmanTrackBranchAndBound2(g,vis)     #test branch&bound

	t1 = time.time()                    					# Temps final
	print("temps: ",t1-t0)              					# imprimir el temps d'execució
	trk.Display(vis)                    					# Visualitza el track i les visites sobre el graf el graf