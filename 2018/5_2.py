from cffi import FFI
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
cffi_dir = os.path.join(script_dir, 'cffi')
sys.path.insert(0, cffi_dir)

c_mod = '_5_1'
ffi = FFI()
ffi.cdef('''
         int react(char *poly, int length); 
         ''')
ffi.set_source(c_mod, '''
#include <stdlib.h>

char low_if_high(char c){
    if (c >= 'A' && c <= 'Z') {return c+32;}
    return c; 
}

int reacts(char a, char b) {
    return a != b && low_if_high(a) == low_if_high(b);               
}

int react(char *poly, int length) {
    char *stack = malloc(length);
    int total_len = 0;
               
    for (int i = 0; i < length; i++) {
        char p = poly[i];
        if (total_len > 0 && reacts(p, stack[total_len-1])) {total_len--;}
        else {stack[total_len] = p;
               total_len++;}
    }
    free(stack);
    return total_len;
}
''')

ffi.compile(tmpdir=cffi_dir, verbose=True)

from _5_1 import lib

with open('2018/data/5.txt', 'r') as infile:
    perm = infile.read().strip()

lowest = float('inf')
for low, up in [(i, i.upper()) for i in list('abcdefghijklmnopqrstuvwxyz')]:
    poly = perm.replace(low, '') ; poly = poly.replace(up, '')
    data = poly.encode('ascii')
    c_poly = ffi.new('char[]', data)
    length = (lib.react(c_poly, len(poly)))
    if length < lowest:
        lowest = length
print(lowest)