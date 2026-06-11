from cffi import FFI
import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
cffi_dir = os.path.join(script_dir, 'cffi')
sys.path.insert(0, cffi_dir)

c_mod = '_6_1'
ffi = FFI()
ffi.cdef('int closest(int *pin, int **coords, int coord_count, int threshold);')
ffi.set_source(c_mod, '''
#include<stdio.h>
#include<stdlib.h>
               
int manhat(int x_pin, int y_pin, int x_coord, int y_coord){
    return abs(x_pin-x_coord) + abs(y_pin-y_coord);
}

int closest(int *pin, int **coords, int coord_count, int threshold) {
    int total_dist = 0;
    int x_pin = pin[0];
    int y_pin = pin[1];
               
    for (int i = 0; i < coord_count; i++) {
        int x_coord = coords[i][0]; 
        int y_coord = coords[i][1];
               
        total_dist += manhat(x_pin, y_pin, x_coord, y_coord);
    }
    if (total_dist < threshold) {return 1;}
    else {return 0;}
}
''')

ffi.compile(tmpdir=cffi_dir, verbose=True)

from _6_1 import lib

with open('2018/data/6.txt', 'r') as infile:
    coords = infile.read().splitlines()

coords = [tuple(map(int, i.split(', '))) for i in coords]
threshold = 10000
max_x, max_y = 0, 0
for x, y in coords:
    max_x = max((x, max_x)) ; max_y = max((y, max_y))
pad = 10

max_x, max_y = max_x + pad, max_y + pad
coords = [(c[0]+pad, c[1]+pad) for c in coords] #[(), (), ()]

grid = [['.' for _ in range(max_y + pad)] for _ in range(max_x + pad)]
safe = 0
c_coords = [ffi.new('int[]', [x, y]) for x, y in coords]
c_coords_array = ffi.new('int*[]', c_coords)
for x in range(len(grid)):
    for y in range(len(grid[0])):
        c_pin = ffi.new('int[]', [x, y])
        if lib.closest(c_pin, c_coords_array, len(coords), threshold):
            safe += 1

print(safe)
