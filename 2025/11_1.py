import networkx as nx

with open('2025/data/11.txt', 'r') as infile:
    data = infile.read().split('\n')
    data_dict = {i.split(':')[0]: i.split(':')[1][1:].split(' ') for i in data}

G = nx.DiGraph()
for k, v in data_dict.items():
    G.add_edges_from([(k, sub_v) for sub_v in v])

print(len(list(nx.all_simple_paths(G, source='you', target='out'))))