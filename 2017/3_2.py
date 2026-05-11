import numpy as np
from itertools import product

def get_neighbor(arr, row, col):
    neighbor_total = 0
    prods = product([row + i for i in [-1, 0, 1]], [col + i for i in [-1, 0, 1]])
    for x, y in prods:
        if 0<=x<=arr.shape[0]-1 and 0<=y<=arr.shape[1]-1 and (x, y) != (row, col):
            neighbor_total += arr[x][y]
    return int(neighbor_total)

def make_arr(largest):
    arr = np.array([[1]])
    while True:
        arr = np.rot90(arr, 3, (0, 1))
        new_row = np.zeros(arr.shape[1])
        arr = np.r_[arr, [new_row]]
        row = arr.shape[0]-1
        for col in range(arr.shape[1]):
            arr[row][col] = get_neighbor(arr, row, col)
            
        if arr.max() >= largest:
            break
    return arr

target = 289326
arr = make_arr(target).astype(int)
next_largest = min(arr[arr>target])
print(next_largest)