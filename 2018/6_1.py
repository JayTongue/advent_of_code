from cffi import FFI
import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
cffi_dir = os.path.join(script_dir, 'cffi')
sys.path.insert(0, cffi_dir)

c_mod = '_6_1'
ffi = FFI()
ffi.cdef('int closest(int *pin, int **coords, int coord_count);')
ffi.set_source(c_mod, '''
#include<stdio.h>
#include<stdlib.h>
               
int manhat(int x_pin, int y_pin, int x_coord, int y_coord){
    return abs(x_pin-x_coord) + abs(y_pin-y_coord);
}

int closest(int *pin, int **coords, int coord_count) {
    int closest = 0;
    int so_far = 2147483647;
    int x_pin = pin[0];
    int y_pin = pin[1];
    int tie = 0;
               
    for (int i = 0; i < coord_count; i++) {
        int dist = 0;
        int x_coord = coords[i][0]; 
        int y_coord = coords[i][1];
               
        dist = manhat(x_pin, y_pin, x_coord, y_coord);
        if (dist < so_far) {
            so_far = dist;
            closest = i;
            tie = 0;   
        }
        else if (dist == so_far) {tie = 1;}
        
    }
    if (tie == 0) {return closest;}
    else {return -1;}
}
''')

ffi.compile(tmpdir=cffi_dir, verbose=True)

from _6_1 import lib

with open('2018/data/6.txt', 'r') as infile:
    coords = infile.read().splitlines()

coords = [tuple(map(int, i.split(', '))) for i in coords]
max_x, max_y = 0, 0
for x, y in coords:
    max_x = max((x, max_x)) ; max_y = max((y, max_y))


pad = 10 ; pad_dict = {}

for pad_offset in range(2):
    pad += pad_offset
    max_x, max_y = max_x + pad, max_y + pad
    coords = [(c[0]+pad, c[1]+pad) for c in coords] #[(), (), ()]

    grid = [['.' for _ in range(max_y + pad)] for _ in range(max_x + pad)]
    counts = {i: 0 for i in range(len(coords))}
    c_coords = [ffi.new('int[]', [x, y]) for x, y in coords]
    c_coords_array = ffi.new('int*[]', c_coords)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            c_pin = ffi.new('int[]', [x, y])
            closest = lib.closest(c_pin, c_coords_array, len(coords))
            if closest >= 0:
                counts[closest] += 1
    pad_dict[pad_offset] = counts

unchanged = {k: v for k, v in pad_dict[0].items() if v == pad_dict[1][k]}
print(max(unchanged.values()))
