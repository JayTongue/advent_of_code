import os, sys
from cffi import FFI

pwd = os.path.dirname(os.path.abspath(__file__))
cffi_dir = os.path.join(pwd, 'cffi')
sys.path.insert(0, cffi_dir)

c_mod = '_2_1'
ffi = FFI()
ffi.cdef('''int twos_and_threes(char **boxes, int box_count);''')
ffi.set_source(c_mod, '''
int twos_and_threes(char **boxes, int box_count) {
    int total_twos = 0;
    int total_threes = 0;

    for (int i = 0; i < box_count; i++){
        int counts[26] = {0};
        for (int j = 0; boxes[i][j] != '\\0'; j++){
               char c = boxes[i][j];

               if (c >= 'a' && c <= 'z'){counts[c - 'a']++;}
               }
               
               int has_two = 0;
               int has_three = 0;
               
               for (int k = 0; k < 26; k++){
                    if (counts[k] == 2){has_two = 1;}
                    if (counts[k] == 3){has_three = 1;}
               }
               if (has_two){total_twos++;}
               if (has_three){total_threes++;}
               }
               return total_twos * total_threes;
               }
               ''')
# ffi.compile(tmpdir=cffi_dir, verbose=True)

from _2_1 import lib

with open('2018/data/2.txt', 'r') as infile:
    boxes = infile.read().split('\n')

c_boxes = [ffi.new('char[]', box.encode('ascii')) for box in boxes]
c_box_array = ffi.new('char *[]', c_boxes)
print(lib.twos_and_threes(c_box_array, len(c_box_array)))