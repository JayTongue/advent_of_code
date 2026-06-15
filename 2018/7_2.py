from collections import defaultdict

with open('2018/data/7.txt', 'r') as infile:
    steps = infile.read().splitlines()

steps = [(i.split(' ')[1], i.split(' ')[-3]) for i in steps]

all_befores, all_afters = set(), set()
befores_dict = defaultdict(set) ; afters_dict = defaultdict(set)

for before, after in steps:
    all_befores.add(before) ; all_afters.add(after)
    befores_dict[after].add(before) ; afters_dict[before].add(after)

all_letters = all_befores | all_afters


def sort_alpha(nexts):
    return sorted(set(nexts))


def get_wait_time(ltr):
    wait_window = 60
    alpha_order = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return alpha_order.index(ltr) + wait_window + 1


class Worker():
    def __init__(self):
        self.ltr = False
        self.cnt = 0


workers = [Worker(), Worker(), Worker(), Worker(), Worker()]

order = []
in_progress = set()
second_tick = 0

while len(order) < len(all_letters):
    for worker in workers:
        if worker.ltr and worker.cnt == 0:
            order.append(worker.ltr)
            in_progress.remove(worker.ltr)
            worker.ltr = False
    possibles = []
    for x in all_letters:
        if x not in order and x not in in_progress and all(i in order for i in befores_dict[x]):
            possibles.append(x)

    possibles = sort_alpha(possibles)

    for worker in workers:
        if not worker.ltr and possibles:
            worker.ltr = possibles.pop(0)
            worker.cnt = get_wait_time(worker.ltr)
            in_progress.add(worker.ltr)

    if len(order) == len(all_letters):
        break
    for worker in workers:
        if worker.ltr:
            worker.cnt -= 1

    second_tick += 1

print(second_tick)