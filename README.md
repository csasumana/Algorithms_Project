# Algorithms_Project
The provided code implements the Bellman-Ford algorithm for solving the single-source shortest path problem in a graph. It is written in Python and includes a Graph class that represents the graph and performs the necessary computations.

The Graph class has the following key features:

•Initialization: The class takes the number of vertices in the graph as input and initializes an empty graph and a list to store the locations.
•addLoc(): This method allows adding locations to the graph. It takes a location as input and appends it to the location list.
•addEdge(): This method adds an edge to the graph. It takes the start point, end point, and path cost as input and appends them to the graph list.
•printArr(): This method prints the cost from the starting point to each location in the graph.
•BellmanFord(): This method performs the Bellman-Ford algorithm to calculate the shortest paths from the given source location. It handles both positive and negative edge weights.
•The code takes user input to define the number of locations and unidirectional paths in the graph. It then prompts the user to enter the locations and the paths along with their costs. Finally, it asks for the starting point and uses the BellmanFord() method to calculate the shortest paths or detect profitable loops in the graph.
