import unittest
import networkx as nx
from graph import Graph  # Replace YourGraphClass with the actual name
from search_algorithms import SearchAlgorithms

class TestSearchAlgorithms(unittest.TestCase):

    def setUp(self):
        # Create a NetworkX graph with the same edges
        self.nx_graph = nx.Graph()
        self.nx_graph.add_edges_from([
            ("Abilene", "Manhattan"),
            ("Coldwater", "Pratt"),
            ("Andover", "Newton")
        ])

        # Create the same custom graph using your class
        self.custom_graph = Graph()  # Using the correct class
        self.custom_graph.add_edge("Abilene", "Manhattan")
        self.custom_graph.add_edge("Coldwater", "Pratt")
        self.custom_graph.add_edge("Andover", "Newton")

        # Add city coordinates to the custom graph for heuristic functions
        self.city_coords = {
            "Abilene": (38.9220277, -97.2666667),
            "Manhattan": (39.1682049, -96.6901159),
            "Coldwater": (37.2574937, -99.3549149),
            "Pratt": (37.6753423, -98.7769217),
            "Andover": (37.6868403, -97.1657752),
            "Newton": (38.0353742, -97.4239353)
        }

    # Helper function for Euclidean distance
    def euclidean_distance(self, city1, city2):
        x1, y1 = self.city_coords[city1]
        x2, y2 = self.city_coords[city2]
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def test_bfs(self):
        # Compare BFS paths using NetworkX's bfs_successors (a BFS-specific function)
        bfs_tree = nx.bfs_successors(self.nx_graph, source="Abilene")

        # Generate path from BFS tree
        nx_path = []
        current_node = "Abilene"
        while current_node != "Manhattan":
            nx_path.append(current_node)
            successors = dict(bfs_tree).get(current_node, [])
            current_node = successors[0] if successors else None
        nx_path.append("Manhattan")

        custom_path = SearchAlgorithms.bfs(self.custom_graph, "Abilene", "Manhattan")
        self.assertEqual(nx_path, custom_path)


    def test_astar(self):
        # Compare A* paths
        nx_path = nx.astar_path(self.nx_graph, source="Abilene", target="Manhattan", heuristic=self.euclidean_distance)
        custom_path = SearchAlgorithms.a_star(self.custom_graph, "Abilene", "Manhattan", self.euclidean_distance)
        self.assertEqual(nx_path, custom_path)

if __name__ == '__main__':
    unittest.main()
