with open('2017/data/12.txt', 'r') as infile:
    pipes = infile.read().split('\n')

pipes = [list(map(int, p.replace(',', '').replace(' <->', '').split(' '))) for p in pipes]
pipes = {p[0]: p[1:] for p in pipes}

to_zero = {0}
while True:
    changed = False
    for pipe in pipes:
        if not to_zero.isdisjoint(pipes[pipe]) and pipe not in to_zero:
            to_zero.add(pipe)
            changed = True
    if not changed:
        break
print(len(to_zero))