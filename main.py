from data_loader import DataLoader
from graph import Graph
from menu import select_cities, run_search, ask_for_new_cities

def main():
    # File paths
    coordinates_file = 'coordinates.csv'
    adjacency_file = 'adjacencies.txt'

    # Load the data
    data_loader = DataLoader(coordinates_file, adjacency_file)
    city_coords = data_loader.load_coordinates()
    adjacency_list = data_loader.load_adjacency_list()

    # Set up the graph
    graph = Graph()
    for city1 in adjacency_list:
        for city2 in adjacency_list[city1]:
            graph.add_edge(city1, city2)
    graph.set_city_coords(city_coords)

    while True:
        # Select start and goal cities with error handling
        start_city, goal_city = select_cities(graph)

        # Run search algorithm with option to try different algorithms
        run_search(graph, start_city, goal_city)

        # Ask if they want to choose different cities
        if not ask_for_new_cities():
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
