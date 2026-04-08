class CConvexHull:
	def __init__(self,g):
		self.Graph=g
		self.Vertices=[]
	def GetNVertices(self):
		return len(self.Vertices)
	def Add(self, vertex):
		self.Vertices.append(vertex)
	def Save(self, filename):
		with open(filename, "w+") as f:
			f.write("CONVEX_HULL 1.0\n")
			for vert in self.Vertices:
				f.write(f"{vert.Name}\n")


# =============================================================================
# CONVEX HULL =================================================================
# =============================================================================

# left ========================================================================
# Recta de p1 a p2. i posició del punt p respecte la recta
# resultat>0: p a la esquerra.
# resultat==0: p sobre la recta.
# resultat<0: p a la dreta

def PosicioRespeteRecta(a, b, c):

	return (a.m_Y - b.m_Y) * (c.m_X - b.m_X) - (a.m_X - b.m_X) * (c.m_Y - b.m_Y)


# AreaTriangle ================================================================

def AreaTriangle(a, b, c):

	return abs((a.m_Y - b.m_Y) * (c.m_X - b.m_X) - (a.m_X - b.m_X) * (c.m_Y - b.m_Y)) / 2.0



# QuickHull ===================================================================

def QuickHull(g):

	return CConvexHull(g)
