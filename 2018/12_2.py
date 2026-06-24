from cffi import FFI
import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
cffi_dir = os.path.join(script_dir, 'cffi')
sys.path.insert(0, cffi_dir)

c_mod = '_12_1'
ffi = FFI()
ffi.cdef('''
int run_puz(int offset, int generations, int *start_seed, int start_len, int **to_one, int len_one);''')
ffi.set_source(c_mod, '''   
#include <stdbool.h>
#include <stdio.h>

bool is_in(int *match_arr, int **arr, int len) {
    for (int match_case_idx = 0; match_case_idx < len ; match_case_idx++) {
        int *match_case = arr[match_case_idx];
        bool little_match = true;
        for (int comp_idx = 0; comp_idx < 5; comp_idx++){
            if (match_arr[comp_idx] != match_case[comp_idx]) {
                little_match = false;   
            }
        }
        if (little_match == true) {
            return true;       
        }        
    }
    return false;               
}               

void copy_arr(int *a, int a_len, int *b) {
    for (int elem=0; elem < a_len; elem++) {
        b[elem] = a[elem]; 
    }    
}               

int run_puz(int offset, int generations, int *start_seed, int start_len, int **to_one, int len_one) {
    for (int g = 0; g < generations; g++ ) {
        int *new_seed = calloc((size_t)start_len, sizeof(*new_seed));
        for (int idx = 2; idx < start_len - 2; idx++) {
            if (is_in(&start_seed[idx - 2], to_one, len_one)) {
                new_seed[idx] = 1;    
            } else {
                new_seed[idx] = 0;
            }
        }
        copy_arr(new_seed, start_len, start_seed);
        free(new_seed);
    }
    int total = 0;
    for (int i=0; i<start_len; i++) {
        if (start_seed[i] == 1) total += i-offset;   
    }
    return total;
}
''', extra_compile_args=["-Wall", "-Wextra", "-Wconversion"])

ffi.compile(tmpdir=cffi_dir, verbose=True)

from _12_1 import lib
from pprint import pprint
# puz = '''initial state: #..#.#..##......###...###

# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #'''

with open('2018/data/12.txt', 'r') as infile:
    puz = infile.read()

puz = puz.replace('.', '0').replace('#', '1').splitlines()
initial = list(map(int, list(puz[0].split(' ')[-1])))
generations = 20
buffer_len = generations * 2
buffer = [0 for _ in range(buffer_len)]
initial = buffer + initial + buffer
changes = {tuple(map(int, list(k))):int(v) for k, v in map(lambda x: x.split(' => '), puz[2:])}
# print(initial)
# pprint(changes)

to_zero = [k for k, v in changes.items() if v == 0]
to_one = [k for k, v in changes.items() if v == 1]

# print(to_zero, to_one)

c_to_one_rows = [ffi.new("int[]", list(row)) for row in to_one]
c_to_one = ffi.new("int *[]", c_to_one_rows)
c_initial = ffi.new('int[]', initial)

result = lib.run_puz(
    buffer_len,
    generations,
    c_initial,
    len(initial),
    c_to_one,
    len(to_one),
)

print(result)