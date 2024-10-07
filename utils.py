# Utility file for calculating distances and printing paths

import math

# Used code from https://gist.github.com/rochacbruno/2883505?permalink_comment_id=2615334
def create_euclidean_distance(city_coords): #Added due to distance calculation errors in menu.py: run_search
    def euclidean_distance(city1, city2):
        lat1, lon1 = city_coords[city1]
        lat2, lon2 = city_coords[city2]
        return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
    return euclidean_distance

def print_path(path):
    print(" -> ".join(path))
