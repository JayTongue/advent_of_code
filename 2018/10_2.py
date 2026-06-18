from cffi import FFI
import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
cffi_dir = os.path.join(script_dir, 'cffi')
sys.path.insert(0, cffi_dir)

c_mod = '_10_2'
ffi = FFI()
ffi.cdef('''
typedef struct {
    int *prev_x;
    int *prev_y;        
} results;

results move_step(int point_len, int *xs, int *ys, int *vel_x, int *vel_y);

void free_results(results r);
         ''')
ffi.set_source(c_mod, """
#include <stdlib.h>
#include <stdio.h>
               
typedef struct {
    int *prev_x;
    int *prev_y;
} results;
               
long long find_dim(int *ys, int *xs, int len) {
    int min_x = xs[0];
    int max_x = xs[0];
    int min_y = ys[0];
    int max_y = ys[0];

    for (int i=0; i< len; i++) {
        if (min_x > xs[i]) min_x = xs[i];
        if (max_x < xs[i]) max_x = xs[i];
        if (min_y > ys[i]) min_y = ys[i];
        if (max_y < ys[i]) max_y = ys[i];           
    }
               
    long long width = max_x - min_x;
    long long length = max_y - min_y;
    return width * length;               
}

void copy_arr(int *a, int *b, int len) {
    for (int i=0; i < len; i++) {
        b[i] = a[i]; 
    }              
}            

results move_step(int point_len, int *xs, int *ys, int *vel_x, int *vel_y) {
    long long old_dim = find_dim(ys, xs, point_len);
    int *prev_x = malloc(point_len * sizeof(*prev_x));
    int *prev_y = malloc(point_len * sizeof(*prev_y));
    int counter = 0;
    
    copy_arr(xs, prev_x, point_len);
    copy_arr(ys, prev_y, point_len);
               
    while (1){
        for (int idx = 0; idx < point_len; idx++) {
            xs[idx] += vel_x[idx];
            ys[idx] += vel_y[idx];
        }
        
        long long new_dim = find_dim(ys, xs, point_len);
        
        if (new_dim > old_dim) {
            printf("%d\\n", counter);
            results out;
            out.prev_x = prev_x;
            out.prev_y = prev_y;
            return out;
            
        } else {
            old_dim = new_dim;
            copy_arr(xs, prev_x, point_len);
            copy_arr(ys, prev_y, point_len);
            counter += 1;       
        }
    }           
}
               
void free_results(results r) {
    free(r.prev_x);
    free(r.prev_y);               
}
""", extra_compile_args=["-Wall", "-Wextra", "-Wconversion"])
ffi.compile(tmpdir=cffi_dir, verbose=True)

from _10_2 import lib
import re

with open('2018/data/10.txt', 'r') as infile:
    puz = infile.read().splitlines()

puz = [[tuple(map(lambda x: int(x.strip(' ')), (a, b))) for a, b, in re.findall(r'\<(.*?),(.*?)>', p)]
        for p in puz]

xs = [p[0][0]for p in puz]
ys = [p[0][1]for p in puz]
vel_x = [p[1][0]for p in puz]
vel_y = [p[1][1]for p in puz]

c_vel_x = ffi.new("int[]", vel_x)
c_vel_y = ffi.new("int[]", vel_y)
c_start_x = ffi.new("int[]", xs)
c_start_y = ffi.new("int[]", ys)

result = lib.move_step(len(puz), c_start_x, c_start_y, c_vel_x, c_vel_y)