from collections import deque

with open('2017/data/24.txt', 'r') as infile:
    pipes = infile.read().split('\n')

pipes = [list(map(int, i.split('/'))) for i in pipes]

results = []
dq = deque([[[0], pipes]])
while True:
    if len(dq) == 0:
        break
    progress, remaining = dq.popleft() 
    possibles = [p for p in remaining if progress[-1] in p]

    if not possibles:
        results.append(progress)
    else:
        for p in possibles:
            new_end = [p[i] for i in range(len(p)) if i != p.index(progress[-1])]
            new_remaining = [remaining[i] for i in range(len(remaining)) if i != remaining.index(p)]
            dq.append([[*progress, *new_end], new_remaining])

max_len = max([len(i) for i in results])
longests = [i for i in results if len(i) == max_len]
print(max(longest[0] + longest[-1] + (2*sum(longest[1:-1])) for longest in longests))
