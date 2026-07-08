from cffi import FFI
import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
cffi_dir = os.path.join(script_dir, 'cffi')
sys.path.insert(0, cffi_dir)

c_mod = '_14_1'
ffi = FFI()
ffi.cdef('int run_puz(int *puz, int puz_len, int filled, int iterations, int elf_1, int elf_2, int *out);')
ffi.set_source(c_mod, '''
               
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

void copy_arr(int *a, int len_a, int *b) {
    for (int i = 0; i < len_a; i++){
        b[i] = a[i];
    }  
}


void print_arr(int *a, int len_a) {
    for (int i = 0; i < len_a; i++) {
        printf("%d ", a[i]);           
    }
    printf("\\n");
}

int run_puz(int *puz, int puz_len, int filled, int iterations, int elf_1, int elf_2, int *out) {
    int *puz_arr = malloc((size_t)puz_len * sizeof(int));
    copy_arr(puz, filled, puz_arr);
    
    for (int iter = 0; iter < iterations; iter++) {
        int elf_1_val = puz_arr[elf_1];
        int elf_2_val = puz_arr[elf_2];
        int new_sum = elf_1_val + elf_2_val;
                      
        if (new_sum >= 10) {
            puz_arr[filled] = 1;
            filled++;
            puz_arr[filled] = new_sum-10;
            filled++;
        } else {
            puz_arr[filled] = new_sum;
            filled++;        
        }
               
        elf_1 = (elf_1 + 1 + elf_1_val) % filled;
        elf_2 = (elf_2 + 1 + elf_2_val) % filled;
               
    }
    copy_arr(puz_arr, filled, out);
    free(puz_arr);
    return filled;
}
''', extra_compile_args=["-Wall", "-Wextra", "-Wconversion"])

ffi.compile(tmpdir=cffi_dir, verbose=True)

from _14_1 import lib

puz = [3, 7]
elf_1 = 0 ; elf_2 = 1

it = 768071
size = 1000000 ; iterations = it+10

c_puz = ffi.new("int[]", puz)
out = ffi.new("int[]", size)

filled = lib.run_puz(c_puz, size, len(puz), iterations, elf_1, elf_2, out)
py_arr = [out[i] for i in range(filled)]

print(''.join(map(str, py_arr[it:iterations])))