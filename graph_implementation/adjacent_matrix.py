class GraphAdjMatrix:
    def __init__(self, num_nodes):
        self.n = num_nodes
        self.matrix = [[0] * num_nodes for _ in range(num_nodes)]
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        # for undirected graph: self.matrix[v][u] = 1
    def display(self):
        for row in self.matrix:
            print(row)


gm = GraphAdjMatrix(3)
gm.add_edge(0, 1)
gm.add_edge(0, 2)
gm.add_edge(1, 2)

gm.display()