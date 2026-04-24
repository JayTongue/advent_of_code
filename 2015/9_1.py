import networkx as nx
from itertools import permutations

with open('2015/data/9.txt', 'r') as infile:
    data = [i.split(' ') for i in infile.read().split('\n')]

G = nx.Graph()
for line in data:
    G.add_node(line[0]) ; G.add_node(line[2])
    G.add_edge(line[0], line[2], weight=int(line[4]))

sol = float('inf')
for combo in permutations(list(G.nodes()), len(G.nodes())):
    dist = 0
    for p in range(len(combo[:-1])):
        dist += nx.shortest_path_length(G, source=combo[p], target=combo[p+1], weight='weight')
    sol = min((dist, sol))
print(sol)