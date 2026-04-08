class CSpanningTree:
	def __init__(self,g):
		self.Graph=g
		self.Edges=[]

	def Add(self, pEdge):
		self.Edges.insert(0,pEdge)
	
	def GetNEdges(self):
		return len(self.Edges)

	def Save(self, filename):
		with open(filename, "w+") as f:
			f.write("SPANNNING TREE 1.0\n")
			for edge in self.Edges:
				f.write(f"{edge.Name}\n")
def SpanningTreePrim(g):
	return CSpanningTree(g)
