# ChatGPT - "How can I compare my program to other implementations to compare for correctness?"
# provided csv and txt data to be used
# Wanted to test my implementation vs the networkx implementation

import networkx as nx
import csv
import time
from search_algorithms import SearchAlgorithms  # Import your custom search algorithms

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

# Define a heuristic for A* (Euclidean distance)
def euclidean_distance(city1, city2):
    lat1, lon1 = city_coords[city1]
    lat2, lon2 = city_coords[city2]
    return ((lat2 - lat1)**2 + (lon2 - lon1)**2) ** 0.5

# Compare BFS
start_time = time.time()
path_bfs = list(nx.shortest_path(G, source='Abilene', target='Manhattan', method='dijkstra'))
end_time = time.time()
print("NetworkX BFS Path:", path_bfs)
print(f"NetworkX BFS time: {end_time - start_time:.4f} seconds")

# Time your own BFS implementation
start_time = time.time()
your_bfs_path = SearchAlgorithms.bfs(G, 'Abilene', 'Manhattan')
end_time = time.time()
print("Your BFS Path:", your_bfs_path)
print(f"Your BFS time: {end_time - start_time:.4f} seconds")

# Networkx uses a different approach in neighbor processing and causes a different answer
# Compare DFS
# start_time = time.time()
# dfs_path = list(nx.dfs_preorder_nodes(G, source='Abilene'))
# end_time = time.time()
# print("NetworkX DFS Path:", dfs_path)
# print(f"NetworkX DFS time: {end_time - start_time:.4f} seconds")


# Time your own DFS implementation
# start_time = time.time()
# your_dfs_path = SearchAlgorithms.dfs(G, 'Abilene', 'Manhattan')  # Use your custom DFS
# end_time = time.time()
# print("Your DFS Path:", your_dfs_path)
# print(f"Your DFS time: {end_time - start_time:.4f} seconds")


# Compare A* search
start_time = time.time()
path_astar = nx.astar_path(G, source='Abilene', target='Manhattan', heuristic=euclidean_distance)
end_time = time.time()
print("NetworkX A* Path:", path_astar)
print(f"NetworkX A* time: {end_time - start_time:.4f} seconds")

# Time your own A* implementation
start_time = time.time()
your_astar_path = SearchAlgorithms.a_star(G, 'Abilene', 'Manhattan', heuristic=euclidean_distance)  # Use your custom A*
end_time = time.time()
print("Your A* Path:", your_astar_path)
print(f"Your A* time: {end_time - start_time:.4f} seconds")
