# Search algorithms the user can choose from
import heapq

import networkx as nx


class SearchAlgorithms:
    @staticmethod
    def bfs(graph, start, goal):
        visited = set()  # Keeps track of visited nodes
        queue = [[start]]  # Queue of paths to explore

        # If the start and goal are the same, return the path immediately
        if start == goal:  # Updated after unit test test_no_path
            return [start]

        while queue:
            path = queue.pop(0)  # Dequeue the first path
            node = path[-1]  # Get the last node in the path

            if node == goal:  # If the goal is reached, return the path
                return path

            if node not in visited:
                visited.add(node)
                # Check if the graph is an instance of your custom Graph class or a networkx.Graph
                # Updated using ChatGPT when implementing networkx_comparison.py
                if isinstance(graph, nx.Graph):
                    neighbors = graph.neighbors(node)  # Use networkx neighbors method
                else:
                    neighbors = graph.get_neighbors(node)  # Use custom Graph get_neighbors method

                for neighbor in neighbors:
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append(new_path)

        return None  # Return None if no path is found after the queue is exhausted

    @staticmethod
    def dfs(graph, start, goal):
        visited = set()
        stack = [[start]]

        while stack:
            path = stack.pop()
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)
                # Added from ChatGPT during implementation of networkx_comparison.py
                # Check if the graph is an instance of networkx.Graph or your custom Graph class
                if isinstance(graph, nx.Graph):
                    neighbors = graph.neighbors(node)  # Use networkx method
                else:
                    neighbors = graph.get_neighbors(node)  # Use custom Graph method

                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)
        return None

    @staticmethod
    def iddfs(graph, start, goal, max_depth=100):
        def dls(node, goal, depth, visited):
            if node == goal:
                return [node]
            if depth == 0:
                return None
            visited.add(node)
            for neighbor in graph.get_neighbors(node):
                if neighbor not in visited:
                    result = dls(neighbor, goal, depth - 1, visited)
                    if result:
                        return [node] + result
            return None

        for depth in range(max_depth):
            visited = set()  # Reset visited nodes for each depth
            result = dls(start, goal, depth, visited)
            if result:
                return result

        return None  # Return None if no path is found

    @staticmethod
    def best_first_search(graph, start, goal, heuristic):
        visited = set()
        priority_queue = [(heuristic(start, goal), [start])]
        while priority_queue:
            _, path = heapq.heappop(priority_queue)
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)
                for neighbor in graph.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(neighbor)
                    heapq.heappush(priority_queue, (heuristic(neighbor, goal), new_path))
        return None

    @staticmethod
    def a_star(graph, start, goal, heuristic):
        visited = set()
        g_score = {start: 0} # Cost to reach each node
        f_score = {start: heuristic(start, goal)} # Estimated cost of the cheapest solution
        priority_queue = [(f_score[start], [start])]

        while priority_queue:
            _, path = heapq.heappop(priority_queue)  # Extract the path, ignore the priority
            node = path[-1]  # The last node in the path

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)
                # Used ChatGPT - added when implementing networkx.comparison
                # Check if the graph is an instance of networkx.Graph or your custom Graph class
                if isinstance(graph, nx.Graph):
                    neighbors = graph.neighbors(node)  # Use networkx method
                else:
                    neighbors = graph.get_neighbors(node)  # Use custom Graph method

                for neighbor in neighbors:
                    tentative_g_score = g_score[node] + 1  # Assuming equal edge cost
                    if tentative_g_score < g_score.get(neighbor, float('inf')):
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                        new_path = list(path)
                        new_path.append(neighbor)
                        heapq.heappush(priority_queue, (f_score[neighbor], new_path))

        return None # No path found
