from cffi import FFI
import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
cffi_dir = os.path.join(script_dir, 'cffi')
sys.path.insert(0, cffi_dir)

c_mod = '_14_2'
ffi = FFI()
ffi.cdef('int run_puz(int *puz, int puz_len, int filled, int elf_1, int elf_2, int *check_list, int check_len);')
ffi.set_source(c_mod, '''
#include <stdlib.h>
#include <stdbool.h>

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

bool check_sum(int *check_list, int check_len, int *puz_arr, int filled) {
    bool check_bool = true;
    for (int k = 0; k < check_len; k++){
        if (puz_arr[(filled-check_len)+k] != check_list[k]) {
            check_bool = false;
            break;
        }
    }
    return check_bool;
}

int run_puz(int *puz, int puz_len, int filled, int elf_1, int elf_2, int *check_list, int check_len) {
    int *puz_arr = malloc((size_t)puz_len * sizeof(int));
    copy_arr(puz, filled, puz_arr);
    
    while (1) {
        int elf_1_val = puz_arr[elf_1];
        int elf_2_val = puz_arr[elf_2];
        int new_sum = elf_1_val + elf_2_val;
                      
        if (new_sum >= 10) {
            puz_arr[filled] = 1;
            filled++;
            
            bool check_bool = check_sum(check_list, check_len, puz_arr, filled);
            if (check_bool == true) {
               int answer = filled-check_len;
               free(puz_arr);
               return answer;
            } 
               
            puz_arr[filled] = new_sum-10;
            filled++;
            
            check_bool = check_sum(check_list, check_len, puz_arr, filled);
            if (check_bool == true) {
               int answer = filled-check_len;
               free(puz_arr);
               return answer;
            } 
        } else {
            puz_arr[filled] = new_sum;
            filled++;
               
            bool check_bool = check_sum(check_list, check_len, puz_arr, filled);
            if (check_bool == true) {
               int answer = filled-check_len;
               free(puz_arr);
               return answer;
            } 
        }
               
        elf_1 = (elf_1 + 1 + elf_1_val) % filled;
        elf_2 = (elf_2 + 1 + elf_2_val) % filled;
        
    }
}
''', extra_compile_args=["-Wall", "-Wextra", "-Wconversion"])

ffi.compile(tmpdir=cffi_dir, verbose=True)

from _14_2 import lib

puz = [3, 7]
elf_1 = 0 ; elf_2 = 1

it = '768071'
check_len = len(list(it))
size = 100000000

c_puz = ffi.new("int[]", puz)
out = ffi.new("int[]", size)
check_list = ffi.new("int[]", list(map(int, list(it))))

counter = lib.run_puz(c_puz, 
                      size, 
                      len(puz), 
                      elf_1, 
                      elf_2, 
                      check_list, 
                      check_len)
print(counter)
