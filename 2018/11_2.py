from cffi import FFI
import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
cffi_dir = os.path.join(script_dir, 'cffi')
sys.path.insert(0, cffi_dir)

c_mod = '_11_2'
ffi = FFI()
ffi.cdef('''
typedef struct {
    int best_x; 
    int best_y;
    int best_dim;
} coords;

int find_val(int x, int y, int seed);
coords iterate_grid(int x_len, int y_len, int seed);
''')
ffi.set_source(c_mod, '''
#include <math.h>
#include <stdlib.h>
               
typedef struct {
    int best_x; 
    int best_y;
    int best_dim;
} coords;
               
int find_val(int x, int y, int seed){
    int rack_id = x+10;
    int power_level = ((rack_id*y)+seed)*rack_id;
    power_level = (power_level/100) % 10;
    power_level -= 5;
    return power_level;
}
               
int find_min(int a, int b) {
    if (a < b) return a;
    return b;               
} 
               
coords iterate_grid(int x_len, int y_len, int seed) {
    int *memo = malloc(((size_t)x_len * (size_t)y_len) * sizeof(int));
    int best_x = 0;
    int best_y = 0;
    int best_dim = 0;
    int best_score = 0;
    
    for (int x=0; x<x_len; x++) {
        for (int y=0; y<y_len; y++) {
            memo[(x*x_len+y)] = find_val(x, y, seed);
        }
    }

    for (int x=0; x<x_len; x++) {
        for (int y=0; y<y_len; y++) {
            for (int trial_dim=1; trial_dim < find_min(x_len-x, y_len-y); trial_dim++) {
                int square_sum = 0;
               
                for (int tx=0; tx<trial_dim; tx++) {
                    for (int ty=0; ty<trial_dim; ty++) {
                        square_sum += memo[((tx+x)*x_len)+(ty+y)];
                    }
                }
                
                if (square_sum > best_score) {
                    best_x = x;
                    best_y = y;
                    best_dim = trial_dim;
                    best_score = square_sum;
            }
            }
        }           
    }
    free(memo);
    
    coords out;
    out.best_x = best_x;
    out.best_y = best_y;
    out.best_dim = best_dim;
    return out;        
}
''', extra_compile_args=["-Wall", "-Wextra", "-Wconversion"])

ffi.compile(tmpdir=cffi_dir, verbose=True)

from _11_2 import lib

seed = 1718
grid_dim = 300

coords = lib.iterate_grid(grid_dim, grid_dim, seed)
best_x, best_y, best_dim = coords.best_x, coords.best_y, coords.best_dim
print(f'{best_x},{best_y},{best_dim}')

