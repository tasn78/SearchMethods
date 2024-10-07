# Main menu functions for user choices

from search_algorithms import SearchAlgorithms
import time
import tracemalloc  # For memory tracking
from utils import create_euclidean_distance, print_path


def choose_algorithm():
    while True:
        try:
            print("\nChoose a search algorithm: ")
            print("1. BFS (Breadth-First Search)")
            print("2. DFS (Depth-First Search)")
            print("3. ID-DFS (Iterative Deepening DFS)")
            print("4. Best-First Search")
            print("5. A* Search")
            print("6. Exit")
            choice = int(input("Enter your choice (1-6): "))

            if 1 <= choice <= 6:  # Ensure choice is within valid range
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")


def select_cities(graph):
    while True:
        start_city = input("Enter the starting city: ")
        goal_city = input("Enter the goal city: ")

        # Check if cities exist in the graph
        if start_city not in graph.graph:
            print(f"Error: '{start_city}' is not in the list of available cities.")
        elif goal_city not in graph.graph:
            print(f"Error: '{goal_city}' is not in the list of available cities.")
        else:
            return start_city, goal_city

# Runs search based on user choice
def run_search(graph, start_city, goal_city):
    # Uses euclidean distance to compute direct distance between the 2 cities
    euclidean_distance = create_euclidean_distance(graph.city_coords)

    while True:
        algorithm_choice = choose_algorithm()

        # Measure time taken
        start_time = time.time()

        # Start memory tracking
        tracemalloc.start()

        # Initialize path variable
        path = None

        if algorithm_choice == 1:
            print("\nRunning BFS...")
            path = SearchAlgorithms.bfs(graph, start_city, goal_city)
        elif algorithm_choice == 2:
            print("\nRunning DFS...")
            path = SearchAlgorithms.dfs(graph, start_city, goal_city)
        elif algorithm_choice == 3:
            print("\nRunning ID-DFS...")
            path = SearchAlgorithms.iddfs(graph, start_city, goal_city)
        elif algorithm_choice == 4:
            print("\nRunning Best-First Search...")
            path = SearchAlgorithms.best_first_search(graph, start_city, goal_city, euclidean_distance)
        elif algorithm_choice == 5:
            print("\nRunning A* Search...")
            path = SearchAlgorithms.a_star(graph, start_city, goal_city, euclidean_distance)
        elif algorithm_choice == 6:
            print("Exiting algorithm selection.")
            break

        # Stop memory tracking and get memory usage
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        end_time = time.time()

        # Display the path
        if path:
            print("\nPath found:")
            print_path(path)
            print(f"Time taken: {end_time - start_time:.4f} seconds")
            print(f"Memory used: {current / 1024:.2f} KB")
            print(f"Peak memory usage: {peak / 1024:.2f} KB")

            # Calculate the total distance
            total_distance = 0
            for i in range(len(path) - 1):
                total_distance += euclidean_distance(path[i], path[i + 1])
            print(f"Total distance: {total_distance:.2f} units")

            # Call the function to plot the cities and the path (only one path at a time)
            graph.plot_graph(path)
        else:
            print("No path found.")

        # Ask if they want to try another algorithm
        another_algo = input("\nDo you want to try another algorithm? (y/n): ").lower()
        if another_algo != 'y':
            break

    # After exiting the algorithm choice loop, ask if the user wants to select new cities
    if ask_for_new_cities():
        start_city, goal_city = select_cities(graph)
        run_search(graph, start_city, goal_city)  # Call run_search recursively to search for new cities

''' Implementation to view multiple algorithms on visual graph (too messy)
def run_search(graph, start_city, goal_city):
    # Uses euclidean distance to compute direct distance between the 2 cities
    euclidean_distance = create_euclidean_distance(graph.city_coords)
    
    # Dictionary to store paths from different algorithms
    paths_by_algorithm = {}
    
    while True:
        algorithm_choice = choose_algorithm()
        
        # Measure time taken
        start_time = time.time()
        
        # Start memory tracking
        tracemalloc.start()
        
        # Initialize path variable
        path = None
        algorithm_name = ""
        
        if algorithm_choice == 1:
            print("\nRunning BFS...")
            path = SearchAlgorithms.bfs(graph, start_city, goal_city)
            algorithm_name = "BFS"
        elif algorithm_choice == 2:
            print("\nRunning DFS...")
            path = SearchAlgorithms.dfs(graph, start_city, goal_city)
            algorithm_name = "DFS"
        elif algorithm_choice == 3:
            print("\nRunning ID-DFS...")
            path = SearchAlgorithms.iddfs(graph, start_city, goal_city)
            algorithm_name = "ID-DFS"
        elif algorithm_choice == 4:
            print("\nRunning Best-First Search...")
            path = SearchAlgorithms.best_first_search(graph, start_city, goal_city, euclidean_distance)
            algorithm_name = "Best-First"
        elif algorithm_choice == 5:
            print("\nRunning A* Search...")
            path = SearchAlgorithms.a_star(graph, start_city, goal_city, euclidean_distance)
            algorithm_name = "A*"
        elif algorithm_choice == 6:
            print("Exiting algorithm selection.")
            break
            
        # Stop memory tracking and get memory usage
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        end_time = time.time()
        
        # Display the path
        if path:
            print(f"\nPath found with {algorithm_name}:")
            print_path(path)
            print(f"Time taken: {end_time - start_time:.4f} seconds")
            print(f"Memory used: {current / 1024:.2f} KB")
            print(f"Peak memory usage: {peak / 1024:.2f} KB")
            
            # Calculate the total distance
            total_distance = 0
            for i in range(len(path) - 1):
                total_distance += euclidean_distance(path[i], path[i + 1])
            print(f"Total distance: {total_distance:.2f} units")
            
            # Store the path and algorithm name
            paths_by_algorithm[algorithm_name] = path
            
        else:
            print("No path found.")
            
        # Ask if they want to try another algorithm
        another_algo = input("\nDo you want to try another algorithm? (y/n): ").lower()
        if another_algo != 'y':
            break
            
    # After all algorithms are run, plot all the paths
    if paths_by_algorithm:
        graph.plot_graph(paths_by_algorithm)
        
    # Check if the user wants to choose new cities
    if ask_for_new_cities():
        # Clear previous paths if the user chooses new cities
        paths_by_algorithm.clear()  # Reset paths
        start_city, goal_city = select_cities(graph)
        run_search(graph, start_city, goal_city)  # Recursive call to start over with new cities
'''

# Allows user to attempt new cities
def ask_for_new_cities():
    while True:
        try_again = input("\nDo you want to choose different cities? (y/n): ").lower()
        if try_again == 'y':
            return True
        elif try_again == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")
