import json
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = {}
        self.adj = defaultdict(list)

    def add_node(self, node_id, node_type):
        self.nodes[node_id] = {"type": node_type}
    
    def add_edge(self, u, v, energy, capacity, bidirection = True,restriction = False):
        self.adj[u].append({
            "to": v,
            "energy": energy,
            "capacity":capacity,
            "restriction": restriction
        })
        if bidirection:
            self.adj[v].append({
                "to": u, 
                "energy": energy,
                "capacity": capacity,
                "restricted": restriction
                })

# B1: load graph from json file
    @staticmethod
    def from_json(path):
        g = Graph()
        with open(path) as f:
            data = json.load(f)
        
        for n in data["nodes"]:
            g.add_node(n["id"], n["type"])
        
        for e in data["edges"]:
            g.add_edge(
                e["from"], e["to"],
                e.get("energy", 1),
                e.get("capacity", 1),
                e.get("bidirectional", True),
                e.get("restricted", False),
            )
        return g
    
    # B2: restrict a corridor
    def restrict(self, u, v, status):
        for edge in self.adj[u]:
            if edge["to"] == v:
                edge["restricted"] = status
        
        for edge in self.adj[v]:
            if edge["to"] == u:
                edge["restricted"] = status
    
    # B3: modify network
    def modify_energy(self, u, v, new_energy):
        for edge in self.adj[u]:
            if edge["to"] == v:
                edge["energy"] = new_energy