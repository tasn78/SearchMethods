import networkx as nx
import csv

# ChatGPT - "How can I compare my program to other implementations to compare for correctness?"
# provided csv and txt data to be used

# Create a graph
G = nx.Graph()

# Load edges from adjacencies.txt
with open('adjacencies.txt', 'r') as adj_file:
    for line in adj_file:
        city1, city2 = line.strip().split()
        G.add_edge(city1, city2)

# Load coordinates from coordinates.csv
city_coords = {}
with open('coordinates.csv', 'r') as coord_file:
    reader = csv.reader(coord_file)
    for row in reader:
        city, lat, lon = row
        city_coords[city] = (float(lat), float(lon))

# Check the graph structure
print(G.nodes())
print(G.edges())

# You can now use NetworkX's built-in BFS, DFS, or A* algorithms to compare with your results
path = nx.shortest_path(G, source='Abilene', target='Manhattan', method='bfs')
print("BFS Path: ", path)


# You can also implement your own heuristic-based A* algorithm
def euclidean_distance(city1, city2):
    lat1, lon1 = city_coords[city1]
    lat2, lon2 = city_coords[city2]
    return ((lat2 - lat1)**2 + (lon2 - lon1)**2) ** 0.5


path_astar = nx.astar_path(G, source='Abilene', target='Manhattan', heuristic=euclidean_distance)
print("A* Path: ", path_astar)
