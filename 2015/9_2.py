import networkx as nx
from itertools import permutations

with open('2015/data/9.txt', 'r') as infile:
    data = [i.split(' ') for i in infile.read().split('\n')]

G = nx.Graph()
for line in data:
    G.add_node(line[0]) ; G.add_node(line[2])
    G.add_edge(line[0], line[2], weight=int(line[4]))

sol = 0
for perm in permutations(list(G.nodes()), len(G.nodes())):
    dist = 0
    for p in range(len(perm[:-1])):
        dist += G[perm[p]][perm[p+1]]['weight']
    sol = max((dist, sol))
print(sol)