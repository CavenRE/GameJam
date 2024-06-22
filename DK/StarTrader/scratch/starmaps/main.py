import json
import random
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, Delaunay
import networkx as nx
import numpy as np

NUM_STARS = 500
MAX_DISTANCE = 100
MAX_CONNECTIONS = 6

# Generate random star positions
def generate_stars(num_stars):
    return [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(num_stars)]

# Save star map to a JSON file
def save_star_map(filename, stars, connections):
    data = {
        'stars': stars,
        'connections': [[int(star1), int(star2)] for star1, star2 in connections]
    }
    with open(filename, 'w') as f:
        json.dump(data, f)

# Visualize the star map and save as an image
def visualize_star_map(stars, connections, method_name):
    plt.figure(figsize=(10, 10))
    for connection in connections:
        star1, star2 = connection
        plt.plot([stars[star1][0], stars[star2][0]], [stars[star1][1], stars[star2][1]], 'b-')
    for star in stars:
        plt.plot(star[0], star[1], 'ro')
    plt.savefig(f"{method_name}.png")
    plt.close()

# Read and visualize the star map from a JSON file
def read_and_visualize_star_map(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        stars = data['stars']
        connections = data['connections']
        plt.figure(figsize=(10, 10))
        for connection in connections:
            star1, star2 = connection
            plt.plot([stars[star1][0], stars[star2][0]], [stars[star1][1], stars[star2][1]], 'b-')
        for star in stars:
            plt.plot(star[0], star[1], 'ro')
        plt.savefig(f"{filename.split('.')[0]}.png")
        plt.show()

# Voronoi Diagram-Based Connections
def voronoi_method(stars):
    vor = Voronoi(stars)
    connections = set()
    for vertex_pair in vor.ridge_points:
        star1, star2 = vertex_pair
        if distance(stars[star1], stars[star2]) <= MAX_DISTANCE:
            connections.add((star1, star2))
    save_star_map('voronoi.json', stars, list(connections))
    visualize_star_map(stars, list(connections), 'voronoi')

# Delaunay Triangulation
def delaunay_method(stars):
    delaunay = Delaunay(stars)
    connections = set()
    for simplex in delaunay.simplices:
        for i in range(3):
            for j in range(i+1, 3):
                star1, star2 = simplex[i], simplex[j]
                if distance(stars[star1], stars[star2]) <= MAX_DISTANCE:
                    connections.add((star1, star2))
    save_star_map('delaunay.json', stars, list(connections))
    visualize_star_map(stars, list(connections), 'delaunay')

# Minimum Spanning Tree with Additional Constraints
def mst_method(stars):
    G = nx.Graph()
    for i, star1 in enumerate(stars):
        for j, star2 in enumerate(stars):
            if i != j:
                dist = distance(star1, star2)
                if dist <= MAX_DISTANCE:
                    G.add_edge(i, j, weight=dist)
    mst = nx.minimum_spanning_tree(G)
    connections = list(mst.edges)
    save_star_map('mst.json', stars, connections)
    visualize_star_map(stars, connections, 'mst')

# Proximity Graph with Constraints
def proximity_graph_method(stars):
    connections = set()
    for i, star1 in enumerate(stars):
        distances = sorted([(distance(star1, star2), j) for j, star2 in enumerate(stars) if i != j])
        for dist, j in distances[:MAX_CONNECTIONS]:
            if dist <= MAX_DISTANCE:
                connections.add((i, j))
    save_star_map('proximity_graph.json', stars, list(connections))
    visualize_star_map(stars, list(connections), 'proximity_graph')

# Custom Connection Algorithm with Heuristics
def custom_method(stars):
    connections = set()
    G = nx.Graph()
    for i, star1 in enumerate(stars):
        for j, star2 in enumerate(stars):
            if i != j:
                dist = distance(star1, star2)
                if dist <= MAX_DISTANCE:
                    G.add_edge(i, j, weight=dist)
    for i in range(len(stars)):
        if i in G:
            neighbors = sorted(G.neighbors(i), key=lambda x: G[i][x]['weight'])
            for j in neighbors[:MAX_CONNECTIONS]:
                connections.add((i, j))
    save_star_map('custom.json', stars, list(connections))
    visualize_star_map(stars, list(connections), 'custom')

# Helper function to calculate distance
def distance(star1, star2):
    return ((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2) ** 0.5

# Main menu
def main():
    stars = generate_stars(NUM_STARS)
    while True:
        print("Select a method to generate the star map:")
        print("1. Voronoi Diagram-Based Connections")
        print("2. Delaunay Triangulation")
        print("3. Minimum Spanning Tree with Additional Constraints")
        print("4. Proximity Graph with Constraints")
        print("5. Custom Connection Algorithm with Heuristics")
        print("6. Read and Visualize Star Map from JSON")
        print("7. Exit")
        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            voronoi_method(stars)
        elif choice == 2:
            delaunay_method(stars)
        elif choice == 3:
            mst_method(stars)
        elif choice == 4:
            proximity_graph_method(stars)
        elif choice == 5:
            custom_method(stars)
        elif choice == 6:
            filename = input("Enter the filename (e.g., voronoi.json): ")
            read_and_visualize_star_map(filename)
        elif choice == 7:
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()