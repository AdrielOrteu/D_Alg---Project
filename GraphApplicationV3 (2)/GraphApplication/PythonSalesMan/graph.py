# Classes per la representació de grafs i altres estructures per la pràctica

import math
import sys
import subprocess
import time
import dijkstra
import greedy
import backtracking
import branchAndBound
import convexhull
import spanningtree


# VERTEX =======================================================================

class Vertex:
    def __init__(self, name, x, y):
        self.Name = name
        self.x = x
        self.y = y
        self.Edges = []
        self.DijkstraDistance = sys.float_info.max
        self.is_in_MSP = False
        self.DijktraVisit = False

    def __lt__(self, other):
        return self.x < other.x

# EDGE =========================================================================

class Edge:
    def __init__(self,name,length,origin,destination):
        self.Name = name
        self.Length = length
        self.Origin = origin
        self.Destination = destination
        self.ReverseEdge = []
        self.Saved=False
    def __lt__(self, other):
        return self.Length < other.Length



# GRAPH =======================================================================

class Graph:
    def __init__(self):
        self.Vertices = []
        self.Edges = []
        self.Edge_dict = {}

    def set_Edge_dict(self):
        for edge in self.Edges:
            if edge.Origin not in self.Edge_dict:
                self.Edge_dict[edge.Origin] = {}
            self.Edge_dict[edge.Origin][edge.Destination] = edge

    def set_Dijkstra_Distance(self, start):
        for node in self.Vertices:
            if node == start:
                node.DijkstraDistance = 0
            else:
                node.DijkstraDistance = sys.float_info.max

    def set_Dijkstra_Visit(self):
        for node in self.Vertices:
            node.DijktraVisit = False

    def get_Edges(self, node):
        return self.Edge_dict[node].items()

    def NewVertex(self, name, x, y):
        v=Vertex(name, x, y)
        self.Vertices.append(v)
        return v

    def GetVertexIndex(self,index):
        return self.Vertices[index]
    
    def GetVertex(self,name):
        for v in self.Vertices:
            if v.Name==name: return v
        else: raise Exception('el vertex ', name,' no existeix')

    def FindVertex(self,name,notFound):
        for v in self.Vertices:
            if v.Name==name: return v
        return notFound

    def NewEdge(self,name,value,origin,destination):
        e=Edge(name,value,origin,destination)
        r=Edge(name+"$Reverse",value,destination,origin)
        e.ReverseEdge=r
        r.ReverseEdge=e
        self.Edges.append(e)
        origin.Edges.append(e)
        self.Edges.append(r)
        destination.Edges.append(r)
        return e

    def GetEdge(self,name):
        for e in self.Edges:
            if e.Name==name: return e
        else: raise Exception('l\'aresta ', name,' no existeix')

    def SetDistancesToEdgeLength(self):
        for e in self.Edges:
            dx=e.Destination.x-e.Origin.x
            dy=e.Destination.y-e.Origin.y
            e.Length=math.sqrt(dx*dx+dy*dy)

    def Load(self,filename):
        f=open(filename,'r')
        l=f.readline()
        if l!='GRAPH 1.0\n': raise Exception(filename, 'no es un fitxer de graph')
        l = f.readline()
        if l[0:11]=='BACKGROUND ' : l=f.readline()
        if l!='UNDIRECTED\n': raise Exception('nomes es poden llegir grafs no dirigits')
        l = f.readline()
        if l != 'VERTICES\n': raise Exception('no es troba la llista de vertexs')
        self.Vertices=[]
        self.Edges=[]
        l=f.readline()
        while l!='EDGES\n':
            l=l.split()
            v=self.NewVertex(l[0],float(l[1]),float(l[2]))
            l = f.readline()
        l = f.readline()
        while l!='':
            l = l.split()
            v1=self.GetVertex(l[2])
            v2=self.GetVertex(l[3])
            e = self.NewEdge(l[0], float(l[1]), v1, v2)
            l = f.readline()
        f.close()

    def Save(self,filename):
        f=open(filename,'w')
        f.write('GRAPH 1.0\n')
        f.write('UNDIRECTED\n')
        f.write('VERTICES\n')
        for v in self.Vertices:
            f.write(str(v.Name)+' '+str(v.x)+' '+str(v.y)+'\n')
        f.write('EDGES\n')
        for e in self.Edges: e.Saved=False
        for e in self.Edges:
            if not e.Saved:
                f.write(str(e.Name)+' '+str(e.Length)+' '+str(e.Origin.Name)+' '+str(e.Destination.Name)+'\n')
                e.ReverseEdge.Saved=True
        f.close()

    def Display(self):
        self.Save("Display.gr")
        subprocess.Popen(["GraphApplicationProf.exe", "display", "Display.GR"])

    def LoadDistances(self,filename):
        f=open(filename,'r')
        l=f.readline()
        if l!='DISTANCES 1.0\n': raise Exception(filename, 'no es un fitxer de distancies')
        l = f.readline()
        while l:
            l=l.split()
            self.GetVertex(l[0]).DijkstraDistance=float(l[1])
            l = f.readline()
        f.close()

    def SaveDistances(self,filename):
        f=open(filename,'w')
        f.write('DISTANCES 1.0\n')
        for v in self.Vertices:
            f.write(str(v.Name)+' '+str(v.DijkstraDistance)+'\n')
        f.close()

    def DisplayDistances(self):
        self.Save("Display.gr")
        self.SaveDistances("Display.dis")
        subprocess.Popen(["GraphApplicationProf.exe", "display", "Display.GR", "Display.dis"])

# Visits ======================================================================

class Visits:
    def __init__(self,g):
        self.Graph=g
        self.Vertices=[]

    def Load(self,filename):
        f=open(filename,'r')
        l=f.readline()
        if l!='VISITS 1.0\n': raise Exception(filename, 'no es un fitxer de visites')
        l = f.readline()
        self.Vertices=[]
        while l:
            l=l.rstrip('\n')
            self.Vertices.append(self.Graph.GetVertex(l))
            l = f.readline()
        f.close()

    def Save(self,filename):
        f=open(filename,'w')
        f.write('VISITS 1.0\n')
        for v in self.Vertices: f.write(str(v.Name)+'\n')
        f.close()

    def Display(self):
        self.Graph.Save("Display.gr")
        self.Save("Display.vis")
        subprocess.Popen(["GraphApplicationProf.exe", "display", "Display.gr", "Display.vis"])

# Track ========================================================================

class Track:
    def __init__(self,g):
        self.Graph=g
        self.Edges=[]

    def AddFirst(self,edge):
        self.Edges.insert(0,edge)

    def AddLast(self,edge):
        self.Edges.append(edge)

    def Append(self,trk):
        self.Edges.extend(trk.Edges)

    def AppendBefore(self,trk):
        self.Edges[0:0]=trk.Edges

    def Load(self,filename):
        f=open(filename,'r')
        l=f.readline()
        if l!='TRACK 1.0\n': raise Exception(filename, 'no es un fitxer de track')
        l = f.readline()
        self.Edges=[]
        while l:
            l=l.rstrip('\n')
            self.Edges.append(self.Graph.GetEdge(l))
            l = f.readline()
        f.close()

    def Save(self,filename):
        f=open(filename,'w')
        f.write('TRACK 1.0\n')
        for e in self.Edges: f.write(str(e.Name)+'\n')
        f.close()

    def Display(self,visits=False):
        self.Graph.Save("Display.gr")
        self.Save("Display.trk")
        if visits:
            visits.Save("Display.vis")
            subprocess.Popen(["GraphApplicationProf.exe", "display", "Display.gr", "Display.trk", "Display.vis"])
        else: subprocess.Popen(["GraphApplicationProf.exe", "display", "Display.gr", "Display.trk"])

# TestNIU ======================================================================

def TestNIU(niu):
    f = open('NIUSAlumnes.csv', 'r')
    l = f.readline()
    while l:
        l=l.rstrip('\n')
        if l==niu:
            f.close()
            return
        l = f.readline()
    f.close()
    raise Exception('el NIU no correspon a un alumne', niu)

# CorrectionProcess ============================================================

def CorrectionProcess():
    args=sys.argv
    print(args, len(args))
    if len(args)<2: return False
    print("Nom Alumne 1.....:",NomAlumne1)
    print("Cognoms Alumne 1.:",CognomsAlumne1 )
    print("NIU Alumne 1.....:",NIUAlumne1)
    print()
    if NIUAlumne2 != "":
        print("Nom Alumne 2.....:",NomAlumne2)
        print("Cognoms Alumne 2.:",CognomsAlumne2)
        print("NIU Alumne 2.....:",NIUAlumne2)
        print()
    if len(args)==2 and args[-1]=="Authors":
        with open("Authors.txt", "w+") as txtfile:
            txtfile.write(NIUAlumne1+"\n"+NIUAlumne2+"\n")
        return True

        #['PythonSalesMan\\main.py', 'Outputs\\Graf10_Dijkstra_Out.txt', 'dijkstra', 'TestDijkstra\\Graf10.GR', 'Outputs\\Graf10_Dijkstra.DIS']
    if len(args)==5 and args[2]=="dijkstra":
        print("Algoritmo..:",args[2])
        print("Grafo......:",args[3])
        print("Distancias.:",args[4])
        g=Graph()
        g.Load(args[3])
        g.SetDistancesToEdgeLength()
        start=g.FindVertex("Start",g.Vertices[0])
        t0=time.time()
        dijkstra.Dijkstra(g,start)
        t1=time.time()
        print("TIEMPO DE EJECUCION:",t1-t0)
        g.SaveDistances(args[-1])
        return True
    elif len(args)==5 and args[2]=="dijkstraqueue":
        print("Algoritmo..:",args[2])
        print("Grafo......:",args[3])
        print("Distancias.:",args[4])
        g=Graph()
        g.Load(args[3])
        g.SetDistancesToEdgeLength()
        start=g.FindVertex("Start",g.Vertices[0])
        t0=time.time()
        dijkstra.DijkstraQueue(g,start)
        t1=time.time()
        print("TIEMPO DE EJECUCION:",t1-t0)
        g.SaveDistances(args[-1])
        return True
    elif len(args)==6 and args[2]=="greedy":
        print("Algoritmo..:",args[2])
        print("Grafo......:",args[3])
        print("Visitas....:",args[4])
        print("Track......:",args[5])
        g=Graph()
        g.Load(args[3])
        g.SetDistancesToEdgeLength()
        vis=Visits(g)
        vis.Load(args[4])
        t0=time.time()
        trk = greedy.SalesmanTrackGreedy(g, vis)
        t1=time.time()
        print("TIEMPO DE EJECUCION:",t1-t0)
        trk.Save(args[-1])
        return True
    elif len(args)==6 and args[2]=="backtracking":
        print("Algoritmo..:",args[2])
        print("Grafo......:",args[3])
        print("Visitas....:",args[4])
        print("Track......:",args[5])
        g=Graph()
        g.Load(args[3])
        g.SetDistancesToEdgeLength()
        vis=Visits(g)
        vis.Load(args[4])
        t0=time.time()
        trk = backtracking.SalesmanTrackBacktracking(g, vis)
        t1=time.time()
        print("TIEMPO DE EJECUCION:",t1-t0)
        trk.Save(args[-1])
        return True
    elif len(args)==6 and args[2]=="backtrackinggreedy":
        print("Algoritmo..:",args[2])
        print("Grafo......:",args[3])
        print("Visitas....:",args[4])
        print("Track......:",args[5])
        g=Graph()
        g.Load(args[3])
        g.SetDistancesToEdgeLength()
        vis=Visits(g)
        vis.Load(args[4])
        t0=time.time()
        trk = backtracking.SalesmanTrackBacktrackingGreedy(g, vis)
        t1=time.time()
        print("TIEMPO DE EJECUCION:",t1-t0)
        trk.Save(args[-1])
        return True
    elif len(args)==6 and args[2]=="branchandbound1":
        print("Algoritmo..:",args[2])
        print("Grafo......:",args[3])
        print("Visitas....:",args[4])
        print("Track......:",args[5])
        g=Graph()
        g.Load(args[3])
        g.SetDistancesToEdgeLength()
        vis=Visits(g)
        vis.Load(args[4])
        t0=time.time()
        trk = branchAndBound.SalesmanTrackBranchAndBound1(g, vis)
        t1=time.time()
        print("TIEMPO DE EJECUCION:",t1-t0)
        trk.Save(args[-1])
        return True
    elif len(args)==6 and args[2]=="branchandbound2":
        print("Algoritmo..:",args[2])
        print("Grafo......:",args[3])
        print("Visitas....:",args[4])
        print("Track......:",args[5])
        g=Graph()
        g.Load(args[3])
        g.SetDistancesToEdgeLength()
        vis=Visits(g)
        vis.Load(args[4])
        t0=time.time()
        trk = branchAndBound.SalesmanTrackBranchAndBound2(g, vis)
        t1=time.time()
        print("TIEMPO DE EJECUCION:",t1-t0)
        trk.Save(args[-1])
        return True
    elif len(args)==6 and args[2]=="branchandbound3":
        print("Algoritmo..:",args[2])
        print("Grafo......:",args[3])
        print("Visitas....:",args[4])
        print("Track......:",args[5])
        g=Graph()
        g.Load(args[3])
        g.SetDistancesToEdgeLength()
        vis=Visits(g)
        vis.Load(args[4])
        t0=time.time()
        trk = branchAndBound.SalesmanTrackBranchAndBound3(g, vis)
        t1=time.time()
        print("TIEMPO DE EJECUCION:",t1-t0)
        trk.Save(args[-1])
        return True
    elif len(args)==5 and args[2]=="convexhull":
        print("Algoritmo..:",args[2])
        print("Grafo......:",args[3])
        print("Hull.:",args[4])
        g=Graph()
        g.Load(args[3])
        t0=time.time()
        hull = convexhull.QuickHull(g)
        t1=time.time()
        print("TIEMPO DE EJECUCION:",t1-t0)
        hull.Save(args[-1])
        return True

    elif len(args)==5 and args[2]=="spanningtree":
        print("Algoritmo..:",args[2])
        print("Grafo......:",args[3])
        print("Arbol.:",args[4])
        g=Graph()
        g.Load(args[3])
        g.SetDistancesToEdgeLength()
        t0=time.time()
        tree = spanningtree.SpanningTreePrim(g)
        t1=time.time()
        print("TIEMPO DE EJECUCION:",t1-t0)
        tree.Save(args[-1])
        return True
    return False

# Display ======================================================================

def DisplayDistances(graf):
    graf.Save("Display.gr")
    graf.SaveDistances("Display.dis")
    subprocess.Popen(["GraphApplicationProf.exe", "display", "Display.GR", "Display.dis"])

