import networkx as nx
from math import prod

with open('2025/data/11.txt', 'r') as infile:
    data = infile.read().split('\n')
    data_dict = {line.split(':')[0]: line.split(':')[1].strip().split(' ') for line in data if line}

G = nx.DiGraph()
for k, v in data_dict.items():
    G.add_edges_from([(k, sub_v) for sub_v in v])

def count_paths_dag(G: nx.DiGraph, src, dst) -> int:
    order = list(nx.topological_sort(G))
    pos = {node: i for i, node in enumerate(order)} ; dp = {node: 0 for node in order}
    dp[src] = 1
    for u in order[pos[src]:pos[dst] + 1]:
        if dp[u] == 0:
            continue
        for v in G.successors(u):
            dp[v] += dp[u]
    return dp[dst]

pairs = (('svr', 'dac'), 
         ('dac', 'fft'), 
         ('fft', 'out'), 
         ('svr', 'fft'), 
         ('fft', 'dac'), 
         ('dac', 'out'))

chunks = []
for u, v in pairs:
    chunks.append(count_paths_dag(G, u, v))
answer = prod(chunks[:3]) + prod(chunks[3:])
print(answer)