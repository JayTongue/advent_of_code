import numpy as np


def main(infile):
    infile = open(f'data/{infile}', 'r')
    infile = [list(line.strip()) for line in infile]
    data = np.array(infile, dtype=int)
    print(data)

    zero_coords = find_start_coordinates(data)
    walk_from_zeros(data, zero_coords)


def find_start_coordinates(data):
    zero_coords = np.where(data == 0)
    return zip(zero_coords[0], zero_coords[1])
 

def walk_from_zeros(data, zero_coords):
    total_sum = 0
    for coord in zero_coords: # for all starting zeros
        working_coords = [coord]
        for matcher in range(1, 10): #are there any _ next to this coord?
            needed = np.where(data == matcher)
            needed = list(zip(needed[0], needed[1]))
            # print('all of the', matcher, ':', [need for need in needed])
            possible_neighbors = []
            for working_coord in working_coords:
                cardinals = get_cardinals(working_coord, data)
                possible_neighbors += cardinals
            # print('possible_neighbors: ', possible_neighbors)
            valid_neighbors = list(set(possible_neighbors).intersection(set(needed)))
            # print('valid neighbors:', valid_neighbors)
            working_coords = valid_neighbors

        total_sum += len(valid_neighbors)
    print(total_sum)


def get_cardinals(coord, data):
    cardinals = []
    shape = data.shape
    up = (coord[0] - 1, coord[1])
    if up[0] >= 0:
        cardinals.append(up)
    down = (coord[0] + 1, coord[1])
    if down[0] <= shape[0] - 1:
        cardinals.append(down)
    left = (coord[0], coord[1] - 1)
    if left[1] >= 0:
        cardinals.append(left)
    right = (coord[0], coord[1] + 1)
    if right[1] <= data.shape[1] - 1:
        cardinals.append(right)
    # print(cardinals)
    return cardinals


if __name__ == '__main__':
    main('10.txt')