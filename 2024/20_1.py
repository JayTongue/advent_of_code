from pprint import pprint
import networkx as nx
from collections import defaultdict

with open('2024/data/20.txt', 'r') as infile:
    data = [list(str(line).replace('\n', '')) for line in infile.readlines()]

for row_count, row in enumerate(data):
    if 'S' in row:
        start_point = (row_count, row.index('S'))
    if 'E' in row:
        end_point = (row_count, row.index('E'))
print(start_point, end_point)

def get_neighbors(node):
    x, y = node
    return (x+1, y), (x-1, y), (x, y+1), (x, y-1)

def make_graph(data):
    G = nx.Graph()
    for row_count, row in enumerate(data):  # make nx graph
        for col_count, col in enumerate(row):
            if data[row_count][col_count] != '#':
                G.add_node((row_count, col_count))
    return G

def draw_edges(G, data):
    rows = len(data)
    cols = len(data[0])
    for node in G.nodes():
        for neighbor in get_neighbors(node):
            n_x, n_y = neighbor
            if 0 <= n_x < rows and 0 <= n_y < cols:
                if data[n_x][n_y] != '#':
                    if neighbor in G:  # neighbor is also a node
                        G.add_edge(node, neighbor)
    return G


pure_graph = draw_edges(make_graph(data), data)
path = nx.shortest_path(pure_graph, source=start_point, target=end_point)
baseline = len(path) - 1   # number of steps from S to E
print("Baseline steps:", baseline)

times = {}
for t, coord in enumerate(path):
    times[coord] = baseline - t 

rows = len(data)
cols = len(data[0])

CHEAT_RANGE = 2

scorekeeper = defaultdict(int)
count = 0

for t, (i, j) in enumerate(path):
    for dx in range(-CHEAT_RANGE, CHEAT_RANGE + 1):
        for dy in range(-CHEAT_RANGE, CHEAT_RANGE + 1):
            d = abs(dx) + abs(dy)
            if d == 0 or d > CHEAT_RANGE:
                continue
            ii, jj = i + dx, j + dy
            if not (0 <= ii < rows and 0 <= jj < cols):
                continue
            if data[ii][jj] == '#':
                continue
            rem_t = times.get((ii, jj))
            if rem_t is None:
                continue
            cheated_len = t + d + rem_t
            saved = baseline - cheated_len

            if saved > 0:
                scorekeeper[saved] += 1
            if saved >= 100:
                count += 1

# pprint(dict(scorekeeper))
print(count)
