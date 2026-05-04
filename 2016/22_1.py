import re

with open('2016/data/22.txt', 'r') as infile:
    data = [list(map(int, re.findall(r'\d+', i))) for i in infile.read().split('\n')[2:]]
    data = {(d[0], d[1]): d[2:] for d in data} # 0Size  1Used  2Avail  3Use

pairs = set()
for node_1 in data:
    for node_2 in data:
        if data[node_1][1] != 0 and data[node_1][1] <= data[node_2][2]:
                pairs.add(frozenset((node_1, node_2)))
print(len(pairs))
