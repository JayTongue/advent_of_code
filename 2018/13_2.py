with open('2018/data/13.txt', 'r') as infile:
    puz = infile.read().splitlines()

puz = [list(p) for p in puz]

carts = []
for row_idx in range(len(puz)):
    for symb in ['>', '<', 'v', '^']:
        if symb in puz[row_idx]:
            for col_idx in range(len(puz[row_idx])):
                if puz[row_idx][col_idx] == symb:
                    carts.append((symb, 'L', (row_idx, col_idx)))

for direc, turn, coords in carts:
    if direc in ['<', '>']:
        puz[coords[0]][coords[1]] ='-'
    elif direc in ['v', '^']:
        puz[coords[0]][coords[1]] = '|'

def move_cart(cart, puz):
    direc, turn, coords = cart
    current = puz[coords[0]][coords[1]]
    if direc == '>':
        if current == '\\':
            return ('v', turn, (coords[0]+1, coords[1]))
        elif current == '/':
            return ('^', turn, (coords[0]-1, coords[1]))
        elif current == '+':
            if turn == 'L':
                return ('^', 'S', (coords[0]-1, coords[1]))
            elif turn == 'S':
                return ('>', 'R', (coords[0], coords[1]+1))
            elif turn == 'R':
                return ('v', 'L', (coords[0]+1, coords[1]))
        return ('>', turn, (coords[0], coords[1]+1))
    elif direc == '<':
        if current == '\\':
            return ('^', turn, (coords[0]-1, coords[1]))
        elif current == '/':
            return ('v', turn, (coords[0]+1, coords[1]))
        elif current == '+':
            if turn == 'L':
                return ('v', 'S', (coords[0]+1, coords[1]))
            elif turn == 'S':
                return ('<', 'R', (coords[0], coords[1]-1))
            elif turn == 'R':
                return ('^', 'L', (coords[0]-1, coords[1]))
        return ('<', turn, (coords[0], coords[1]-1))
    elif direc == 'v':
        if current == '\\':
            return ('>', turn, (coords[0], coords[1]+1))
        elif current == '/':
            return ('<', turn, (coords[0], coords[1]-1))
        elif current == '+':
            if turn == 'L':
                return ('>', 'S', (coords[0], coords[1]+1))
            elif turn == 'S':
                return ('v', 'R', (coords[0]+1, coords[1]))
            elif turn == 'R':
                return ('<', 'L', (coords[0], coords[1]-1))
        return ('v', turn, (coords[0]+1, coords[1]))
    elif direc == '^':
        if current == '\\':
            return ('<', turn, (coords[0], coords[1]-1))
        elif current == '/':
            return ('>', turn, (coords[0], coords[1]+1))
        elif current == '+':
            if turn == 'L':
                return ('<', 'S', (coords[0], coords[1]-1))
            elif turn == 'S':
                return ('^', 'R', (coords[0]-1, coords[1]))
            elif turn == 'R':
                return ('>', 'L', (coords[0], coords[1]+1))
        return ('^', turn, (coords[0]-1, coords[1]))

while True:
    carts.sort(key=lambda cart: (cart[2][0], cart[2][1]))

    remaining = carts[:]
    moved = []

    for cart in carts:
        if cart not in remaining:
            continue

        remaining.remove(cart)

        new_cart = move_cart(cart, puz)
        new_coord = new_cart[2]
        hit_moved = [c for c in moved if c[2] == new_coord]
        hit_remaining = [c for c in remaining if c[2] == new_coord]

        if hit_moved:
            moved = [c for c in moved if c[2] != new_coord]
            continue

        if hit_remaining:
            remaining = [c for c in remaining if c[2] != new_coord]
            continue

        moved.append(new_cart)

    carts = moved + remaining

    if len(carts) == 1:
        sol = carts[0][2]
        print(f"{sol[1]},{sol[0]}")
        break
        