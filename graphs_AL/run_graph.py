import json
from graphs_AL import GraphAL

# Load the graph data from JSON
with open('graph.json') as f:
    data = json.load(f)

nvertices = data['nvertices']
directed = data['directed']

# Create the graph object
g = GraphAL(nvertices, directed)

# Add all edges from the JSON
for edge in data['edges']:
    g.add_edge(edge['x'], edge['y'], edge['weight'])

# Display the graph (optional, can comment out)
g.display()

# Run Dijkstra's algorithm from vertex 1
start_vertex = 1
distance, parent = g.dijkstra(start_vertex)

# Print shortest distance from start_vertex to all vertices
print("\nShortest distances from vertex", start_vertex)
for v in range(1, nvertices+1):
    print(f"To vertex {v}: {distance[v]}")
