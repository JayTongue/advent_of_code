import networkx as nx

with open('2017/data/12.txt', 'r') as infile:
    pipes = infile.read().split('\n')

pipes = [list(map(int, p.replace(',', '').replace(' <->', '').split(' '))) for p in pipes]
pipes = {p[0]: p[1:] for p in pipes}

G = nx.Graph()
for pipe in pipes:
    G.add_node(pipe)
for pipe in pipes:
    for p in pipes[pipe]:
        G.add_edge(pipe, p)
print(len(list(nx.connected_components(G))))