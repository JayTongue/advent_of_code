import networkx as nx
from collections import defaultdict
import copy

with open('2017/data/7.txt', 'r') as infile:
    nodes = [i.replace(',', '').split(' ') for i in infile.read().split('\n')]

G = nx.DiGraph()
for node in nodes:
    G.add_node(node[0], weight=int(node[1][1:-1]))

for node in nodes:
    if len(node) > 2:
        for n in node[3:]:
            G.add_edge(node[0], n)

def sum_children(G, target):
    return sum([G.nodes[target]['weight'], *[G.nodes[i]['weight'] for i in nx.descendants(G, target)]])

original_grid = copy.deepcopy(G)
ends = [i for i, j in G.out_degree if j == 0]
while True:
    imbalance = False
    balance = defaultdict(list)
    for end in ends:
        balance[list(G.predecessors(end))[0]].append(end)
    for k in balance:
        weights = {i: sum_children(G, i) for i in balance[k]}
        if len(set(weights.values())) != 1:
            odds = {i:[] for i in weights.values()}
            for key, val in weights.items():
                odds[val].append(key)
            many = [o for o in odds if len(odds[o]) > 1][0]
            few = [o for o in odds if len(odds[o]) == 1][0] 
            print(many - few + G.nodes[odds[few][0]]['weight'])
            imbalance = True
            break
        else:
            continue
    ends = balance.keys()
    if imbalance:
        break
