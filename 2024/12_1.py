import numpy as np
import copy

def main():
    infile = open('data/12.txt', 'r')
    infile = [list(line.strip()) for line in infile]
    data = np.array(infile, dtype=str)
    print(data)

    unique_crops = np.unique(data)
    # print(unique_crops)

    find_crop_chunks(data, unique_crops)


def find_crop_chunks(data, unique_crops):
    all_fence = 0
    for unique_crop in unique_crops:
        locations = np.where(data == unique_crop)
        # print(locations)
        locations = zip(locations[0], locations[1])
        
        all_chunks = set()
        for location in locations: # for each possible starting chunk, look for neighbors
            chunk = grow_chunk(location, data, unique_crop)
            all_chunks.add(frozenset(chunk))
        # print(unique_crop, all_chunks)

        total_fence = 0
        for chunk in all_chunks:
            perimeter = find_perimeters(list(chunk), data, unique_crop)
            # print('perimeter: ', perimeter)
            fence = perimeter * len(chunk)
            total_fence += fence
        # print(total_fence)
        all_fence += total_fence
    print(f'Total fence cost: {all_fence}')

def find_perimeters(chunk: set, data, unique_crop):
    perimeter = 0
    # print(type(chunk))
    for point in chunk:
        # print('point:', point)
        neighbors = get_cardinals(point, data, boundaries=False)
        # print(neighbors)
        # peri_coords = []
        for neighbor in neighbors:
            try:
                if neighbor[0] < 0 or neighbor[1] < 0:
                    perimeter += 1
                    # peri_coords.append(neighbor)
                elif (data[neighbor] != unique_crop) and (neighbor not in chunk):
                    # print(data[neighbor], unique_crop)
                    perimeter += 1
                    # peri_coords.append(neighbor)
            except IndexError:
                perimeter += 1
                # peri_coords.append(neighbor)
        # print(peri_coords)
    return(perimeter)


def grow_chunk(location, data, unique_crop):
    neighbors = get_cardinals(location, data)

    chunk = set()
    chunk.add((location))
    # print(chunk, location)
    new = True
    while new:
        new = False
        chunk_set = chunk.copy() # I cannot articulate how many times copy() has kneecapped me 
        for location in chunk_set:
            neighbors = get_cardinals(location, data, boundaries=True)
            for neighbor in neighbors:
                # print(data[neighbor] == unique_crop, data[neighbor], unique_crop)
                if ((data[neighbor] == unique_crop) and (neighbor not in chunk)):
                    chunk.add(neighbor)
                    new = True
    return chunk



def get_cardinals(coord, data, boundaries = True):
    cardinals = []
    shape = data.shape
    up = (coord[0] - 1, coord[1])
    down = (coord[0] + 1, coord[1])
    left = (coord[0], coord[1] - 1)
    right = (coord[0], coord[1] + 1)

    if boundaries:
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
    else:
        cardinals.append(up)
        cardinals.append(down)
        cardinals.append(left)
        cardinals.append(right)
    # print(cardinals)
    return cardinals

if __name__ == '__main__':
    main()