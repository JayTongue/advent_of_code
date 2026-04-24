with open('2025/data/12.txt', 'r') as infile:
    data = infile.read().split('\n\n')
    shapes, index = data[:-1], data[-1].split('\n')
    shapes = {i.split(':')[0]: i.split(':')[1][1:].split('\n') for i in shapes}
    shapes = {int(k): list(map(list, v)) for k, v in shapes.items()}
    for shape in shapes:
        shapes[shape] = [list(map(lambda x: 1 if x == '#' else 0, i))for i in shapes[shape]]
    index_list = []
    for i in index:
        size, needed = i.split(': ')
        size = tuple(map(int, size.split('x'))) ; needed = list(map(int, needed.split(' ')))
        index_list.append((size, needed))

sol = 0
for size, pieces in index_list:
    sanity = 0 ; size = size[0]*size[1]
    for c, p in enumerate(pieces):
        sanity += p * sum([i for sub in shapes[c] for i in sub])
    if size > sanity:
        sol += 1
print(sol)