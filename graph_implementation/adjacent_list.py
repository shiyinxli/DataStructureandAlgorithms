class GraphAdjList:
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)

        if v not in self.graph[u]:
            self.graph[u].append(v)
         # for undirected graph: self.graph[v].append(u)
    
    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")

g = GraphAdjList()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)

g.display()