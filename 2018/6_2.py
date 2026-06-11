from cffi import FFI
import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
cffi_dir = os.path.join(script_dir, 'cffi')
sys.path.insert(0, cffi_dir)

c_mod = '_6_2'
ffi = FFI()
ffi.cdef('int count_safe(int max_x, int max_y, int **coords, int coord_count, int threshold);')
ffi.set_source(c_mod, '''
#include<stdio.h>
#include<stdlib.h>
               
int manhat(int x_pin, int y_pin, int x_coord, int y_coord){
    return abs(x_pin-x_coord) + abs(y_pin-y_coord);
}

int count_safe(int max_x, int max_y, int **coords, int coord_count, int threshold) {
    int safe_count = 0;

    for (int x_pin = 0; x_pin < max_x; x_pin++) {
        for (int y_pin = 0; y_pin < max_y; y_pin++) {
            int pin_dists = 0;
            for (int coord = 0; coord < coord_count; coord++) {
                int x_coord = coords[coord][0];
                int y_coord = coords[coord][1];
                pin_dists += manhat(x_pin, y_pin, x_coord, y_coord);
            }
            if (pin_dists < threshold) {
                safe_count += 1;
            }
        }               
    }
    return safe_count;    
}
''')

ffi.compile(tmpdir=cffi_dir, verbose=True)

from _6_2 import lib

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
c_coords_array = ffi.new('int*[]', [ffi.new('int[]', [x, y]) for x, y in coords])

grid_dims = (max_x + pad, max_y + pad)
print(lib.count_safe(grid_dims[0], grid_dims[1], c_coords_array, len(coords), threshold))
