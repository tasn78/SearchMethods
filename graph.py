import matplotlib.pyplot as plt
import networkx as nx

from collections import defaultdict

# Creates graphs based on dictionary of cities and connections
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.city_coords = {}

    # Connects cities
    def add_edge(self, city1, city2):
        self.graph[city1].append(city2)
        self.graph[city2].append(city1)  # Symmetrical connection

    def set_city_coords(self, coords):
        self.city_coords = coords

    def get_neighbors(self, city):
        return self.graph[city]

    def get_city_coordinates(self, city):
        return self.city_coords.get(city, None)

    # Creates visual representation of cities and connections, draws based on the algorithm chosen
    def plot_graph(self, path=None):
        G = nx.Graph()

        # Add cities (nodes) to the graph
        for city in self.city_coords:
            G.add_node(city, pos=(self.city_coords[city][1], self.city_coords[city][0]))  # (longitude, latitude)

        # Add edges (adjacencies)
        for city1 in self.graph:
            for city2 in self.get_neighbors(city1):
                G.add_edge(city1, city2)

        # Get the positions of the cities (for NetworkX)
        pos = nx.get_node_attributes(G, 'pos')

        # Create a plot
        plt.figure(figsize=(12, 10))  # Increased figure size for better readability

        # Plot all the cities (nodes)
        nx.draw_networkx_nodes(G, pos, node_size=100, node_color='blue', label='Cities')

        # Plot all the connections between cities (edges)
        nx.draw_networkx_edges(G, pos, edge_color='gray', width=1)

        # Plot the city names (labels) with increased font size
        nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', verticalalignment='bottom')

        # If a path is provided, highlight the path
        if path:
            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.5, label='Path')

        # Set the title and show the plot
        plt.title("City Map and Routes")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()  # Adjust layout to prevent label cut-off
        plt.show()

'''
    # Created to show all algorithms on the same graph, but was too difficult to read due to overlapping
    def plot_graph(self, paths_by_algorithm=None):
        G = nx.Graph()

        # Add cities (nodes) to the graph
        for city in self.city_coords:
            G.add_node(city, pos=(self.city_coords[city][1], self.city_coords[city][0]))  # (longitude, latitude)

        # Add edges (adjacencies)
        for city1 in self.graph:
            for city2 in self.get_neighbors(city1):
                G.add_edge(city1, city2)

        # Get the positions of the cities (for NetworkX)
        pos = nx.get_node_attributes(G, 'pos')

        # Create a plot
        plt.figure(figsize=(12, 10))  # Increased figure size for better readability

        # Plot all the cities (nodes)
        nx.draw_networkx_nodes(G, pos, node_size=100, node_color='blue', label='Cities')

        # Plot all the connections between cities (edges)
        nx.draw_networkx_edges(G, pos, edge_color='gray', width=1)

        # Plot the city names (labels) with increased font size
        nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', verticalalignment='bottom')

        # If multiple paths are provided, plot each path with a different color
        if paths_by_algorithm:
            colors = ['red', 'green', 'orange', 'purple', 'brown']  # Assign distinct colors
            for i, (algorithm, path) in enumerate(paths_by_algorithm.items()):
                color = colors[i % len(colors)]  # Cycle through colors if more than 5 algorithms
                path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
                nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color=color, width=2.5, label=algorithm)

        # Set the title and show the plot
        plt.title("City Map and Routes")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()  # Adjust layout to prevent label cut-off
        plt.show()
'''