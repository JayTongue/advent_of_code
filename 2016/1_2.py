with open('2016/data/1.txt', 'r') as infile:
    data = [(a[0], int(a[1:])) for a in infile.read().split(', ')]

orientations = ['N', 'E', 'S', 'W']
coords = (0, 0) ; orientation = 'N'
visited = [coords]

def solve(coords, orientation, orientations, visited):
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

        for _ in range(distance):
            if orientation == 'N':
                new_coord = (coords[0], coords[1]+1)
            elif orientation == 'S':
                new_coord = new_coord = (coords[0], coords[1]-1)
            elif orientation == 'E':
                new_coord = new_coord = (coords[0]+1, coords[1])
            elif orientation == 'W':
                new_coord = new_coord = (coords[0]-1, coords[1])

            if new_coord in visited:
                return sum(map(abs, new_coord))
            else:
                visited.append(new_coord)
                coords = new_coord

print(solve(coords, orientation, orientations, visited))