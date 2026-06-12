from collections import defaultdict
from pprint import pprint

steps = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
'''.splitlines()

with open('2018/data/7.txt', 'r') as infile:
    steps = infile.read().splitlines()

steps = [(i.split(' ')[1], i.split(' ')[-3]) for i in steps]

all_befores, all_afters = set(), set()
befores_dict = defaultdict(set) ; afters_dict = defaultdict(set)
for before, after in steps:
    all_befores.add(before) ; all_afters.add(after)
    befores_dict[after].add(before) ; afters_dict[before].add(after)

start = (all_befores - all_afters).pop() ; end = (all_afters - all_befores).pop() ; all_letters = all_befores | all_afters

def sort_alpha(nexts):
    alpha_order = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ordered = sorted({alpha_order.index(i): i for i in nexts}.items())
    return [i[1] for i in ordered]

def get_alpha_idx(char):
    alpha_order = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return alpha_order.index(char)

order = []

while len(order) < len(all_letters):
    possibles = []
    for x in all_letters:
        if x not in order and all(i in order for i in befores_dict[x]):
            possibles.append(x)
    possibles = sort_alpha(possibles)

    order.append(possibles[0])

print(sum([get_alpha_idx(o) + 60 for o in order]))

