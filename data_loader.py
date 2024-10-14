# Imports and loads data

import pandas as pd
from collections import defaultdict

class DataLoader:
    def __init__(self, coordinates_file, adjacency_file):
        self.coordinates_file = coordinates_file
        self.adjacency_file = adjacency_file

    # Dictionary of coordinates, tuple of two floats for latitude and longitude
    def load_coordinates(self):
        city_coords = {}
        data = pd.read_csv(self.coordinates_file, sep=",", header=None)
        #print(data.head())  # Print the first few rows of the data to confirm correct structure
        for _, row in data.iterrows():
            city, lat, lon = row[0], row[1], row[2]  # This unpacks the values
            city_coords[city] = (float(lat), float(lon))
        return city_coords

    # Dictionary of lists : city names map to lists of adjacent cities
    def load_adjacency_list(self):
        graph = defaultdict(list)
        with open(self.adjacency_file, 'r') as file:
            for line in file:
                city1, city2 = line.strip().split()
                graph[city1].append(city2)
                graph[city2].append(city1)  # Bidirectional connection
        return graph
