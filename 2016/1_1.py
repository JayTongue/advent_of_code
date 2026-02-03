with open('2016/data/1.txt', 'r') as infile:
    data = [(a[0], int(a[1:])) for a in infile.read().split(', ')]

orientations = ['N', 'E', 'S', 'W']
coords = [0, 0] ; orientation = 'N'

for direction, distance in data:
    current_or = orientations.index(orientation)
    if direction == 'L':
        try:
            orientation = orientations[current_or - 1]
        except IndexError:
            orientation = orientations[-1]
    elif direction == 'R':
        try:
            orientation = orientations[current_or + 1]
        except IndexError:
            orientation = orientations[0]

    if orientation == 'N':
        coords = [coords[0], coords[1] + distance]
    elif orientation == 'S':
        coords = [coords[0], coords[1] - distance]
    elif orientation == 'E':
        coords = [coords[0] + distance, coords[1]]
    elif orientation == 'W':
        coords = [coords[0] - distance, coords[1]]

print(sum(map(abs, coords)))