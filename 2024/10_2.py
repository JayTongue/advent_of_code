import networkx as nx


def main():
    infile = open('data/10.txt', 'r')
    data = [list(line.strip()) for line in infile]
    data = [[int(num) for num in sublist] for sublist in data]
    zero_coords = find_zeros(data)
    
    for zero in zero_coords:
        build_tree(zero, data)

class Node:
    def __init__(self, value, coord):
        self.value = value
        self.coord = coord
    def __repr__(self):
        return f"CustomNode(value = {self.value}, coord = {self.coord})"



def build_tree(zero: tuple[int, int], data):
    graph = nx.Graph()

    value = data[zero[0]][zero[1]]
    zero_node = Node(value, zero)
    graph.add_node(zero_node)

    print(graph)

    neighbors = get_cardinals(zero, data)

    for neighbor in neighbors:
        row, number = neighbor
        value = data[row][number]
        if value == 1:
            one_node = Node(value, (row, number))
            graph.add_node(one_node)


def find_zeros(data):
    zero_coords = []
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == 0:
                zero_coords.append(tuple([x, y]))
    return zero_coords


def get_cardinals(coord, data):
    cardinals = []
    up = (coord[0] - 1, coord[1])
    if up[0] >= 0:
        cardinals.append(up)
    down = (coord[0] + 1, coord[1])
    if down[0] <= len(data) - 1:
        cardinals.append(down)
    left = (coord[0], coord[1] - 1)
    if left[1] >= 0:
        cardinals.append(left)
    right = (coord[0], coord[1] + 1)
    if right[1] <= len(data[0]) - 1:
        cardinals.append(right)
    # print(cardinals)
    return cardinals


if __name__ == '__main__':
    main()