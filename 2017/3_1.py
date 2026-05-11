import numpy as np

def make_arr(largest):
    arr = np.array([[1]])
    while True:
        arr = np.rot90(arr, 3, (0, 1))
        new_row = list(range(int(arr.max()+1), int(arr.max()+arr.shape[1])+1))
        arr = np.r_[arr, [new_row]]
        if arr.max() >= largest:
            break
    return arr

target = 289326
arr = make_arr(target)

def int_coords(arr, find):
    return tuple(map(int, np.where(arr==find)))

centx, centy = int_coords(arr, 1)
tarx, tary = int_coords(arr, target)
manhat_dist = (max([centx, tarx]) - min([centx, tarx])) + (max([centy, tary]) - min([centy, tary]))

print(manhat_dist)