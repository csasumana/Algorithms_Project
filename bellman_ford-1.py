# Python3 program for Bellman-Ford's single source

# Class to represent a graph
class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = []
		self.location = []
	def addLoc(self,l):
		self.location.append(l)
	# function to add an edge to graph
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# utility function used to print the solution
	def printArr(self, dist):
		print("Cost from start point:")
		for i in range(self.V):
			print(i,self.location[i],": ", dist[i])


	def BellmanFord(self, src):

		# Initialize distances from src as INFINITE
		dist = [float("Inf")] * self.V
		dist[src] = 0

		for _ in range(self.V - 1):

			for u, v, w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
					dist[v] = dist[u] + w

		t=[]
		for i in dist:
			t.append(i)

		n_cycle = False
		for _ in range(self.V - 1):
			for u, v, w in self.graph:
			
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
					dist[v] = dist[u] + w
					n_cycle = True

		if n_cycle:
			for i in range(self.V ):
				if (t[i] > dist[i]):
					print(self.location[i],"is part of a profitable loop")
			return

		# print all distance
		self.printArr(t)


# Driver's code
if __name__ == '__main__':
	verteces = input("Enter the number of locations : ")
	edges = input("Enter the total no of unidirectional Paths : ")
	try:
		v = int(verteces)
		e = int(edges)
		g = Graph(v)
	except:
		print("Please Enter a valid number of locations and Paths")

	print("Enter all the Locations")
	for i in range(v):
		location = input("location:")
		g.addLoc(location)

	print("Enter all the unidirectional paths & their costs [-ve for profit]")
	for i in range(e):
		start = input("Start point:")
		end = input("End point:")
		cost = input("Path Cost:")

		c = int(cost)

		list_L = g.location

		u = list_L.index(start)
		v = list_L.index(end)

		g.addEdge(u, v, c)


	# function call
	starting_point = input("Enter the starting Point :")
	s = g.location.index(starting_point)
	g.BellmanFord(int(s))
