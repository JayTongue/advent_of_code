from collections import defaultdict

with open('2015/data/19.txt', 'r') as infile:
    replacements, starter = infile.read().split('\n\n')
    repl_dict = defaultdict(list)
    for i in replacements.split('\n'):
        k, v, = i.split(' => ')
        repl_dict[k].append(v)

uniques = set()
for key in repl_dict.keys():
    idxs = [i for i in range(len(starter) - len(key)+1) if ''.join(starter[i:i+len(key)]) == key]
    for idx in idxs:
        for sub in repl_dict[key]:
            uniques.add(starter[:idx] + sub + starter[idx+len(key):])

print(len(uniques))