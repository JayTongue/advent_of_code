# with open('2018/data/1.txt', 'r') as infile:
#     changes = infile.read().replace('+', '').split('\n')
# changes = list(map(int, changes))

# print(sum(changes))

import os
import sys
from cffi import FFI

script_dir = os.path.dirname(os.path.abspath(__file__)) #pwd
cffi_dir = os.path.join(script_dir, "cffi") #points to cffi folder

sys.path.insert(0, cffi_dir) # adds a path, cffi_dir, at index 0 of paths

c_mod = "_1_1"
ffi = FFI()

ffi.cdef("""
    int sum_ints(int *values, int length);
""")

ffi.set_source(
    c_mod,
    """
    int sum_ints(int *values, int length) {
        int total = 0;
        for (int i = 0; i < length; i++) {
            total += values[i];
        }
        return total;
    }
    """
)

ffi.compile(tmpdir=cffi_dir, verbose=True)

from _1_1 import lib

with open('2018/data/1.txt', 'r') as infile:
    changes = infile.read().replace("+", "").splitlines()

changes = list(map(int, changes))

c_array = ffi.new("int[]", changes)

print(lib.sum_ints(c_array, len(changes)))