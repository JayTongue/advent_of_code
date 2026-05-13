import networkx as nx

with open('2017/data/7.txt', 'r') as infile:
    nodes = [i.replace(',', '').split(' ') for i in infile.read().split('\n')]

G = nx.DiGraph()
for node in nodes:
    G.add_node(node[0])

for node in nodes:
    if len(node) > 2:
        for n in node[3:]:
            G.add_edge(node[0], n)
print([i for i, j in G.in_degree if j == 0][0])