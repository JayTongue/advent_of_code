from math import sqrt, prod
import networkx as nx
from itertools import combinations

with open('2025/data/8.txt', 'r') as infile:
    data = [tuple(map(int, line.split(','))) for line in infile.read().split('\n')]

def euclidean_dist(abox, bbox):
    ax, ay, az = abox ; bx, by, bz = bbox
    return sqrt((ax-bx)**2 + (ay-by)**2 + (az-bz)**2)

G = nx.Graph()
for abox, bbox in combinations(data, 2):
    G.add_node(abox) ; G.add_node(bbox)
    G.add_edge(abox, bbox)
    G[abox][bbox]['weight'] = euclidean_dist(abox, bbox)

G2 = nx.Graph()
sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2].get('weight', 1))
connections = 10
for count, edge in zip(range(connections), sorted_edges):
    abox, bbox, weight = edge
    weight = weight['weight']
    G2.add_node(abox) ; G2.add_node(bbox)
    G2.add_edge(abox, bbox)

components = sorted(list(nx.connected_components(G2)), key=len, reverse=True)
print(prod(sorted([len(i) for i in components], reverse=True)[:3]))
