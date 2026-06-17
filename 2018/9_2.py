from cffi import FFI
import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
cffi_dir = os.path.join(script_dir, 'cffi')
sys.path.insert(0, cffi_dir)

c_mod = '_9_1'
ffi = FFI()
ffi.cdef('''long long marbles(int player_count, int max_marble);''')
ffi.set_source(c_mod, '''
long long marbles(int player_count, int max_marble) {
    long long *scores = calloc(player_count, sizeof(long long));
    int *next = malloc((max_marble+1)*sizeof(int));
    int *prev = malloc((max_marble+1)*sizeof(int));
    int current = 0;
    
    prev[0] = 0;
    next[0] = 0;
    
    for (int marble=1; marble<=max_marble; marble++) {
        int player = (marble-1)%player_count;
               
        if (marble%23 == 0) {
            scores[player] += marble;
            
            int removing = current;
            for (int i=0; i<7; i++) {
                removing = prev[removing];
            }
            
            scores[player] += removing;
            int left = prev[removing];
            int right = next[removing];
            next[left] = right;
            prev[right] = left;
            
            current = removing[next];
        } else {
            int left = next[current];
            int right = next[left];

            next[left] = marble;
            next[marble] = right;
            prev[right] = marble;
            prev[marble] = left;

            current = marble;      
        }
    }
    free(next);
    free(prev);
    
    long long high_score = 0;
    for (int i=0; i<player_count; i++) {
        if (scores[i] > high_score) {high_score = scores[i];}    
    }
                       
    free(scores);
    return high_score;
}
               ''')
ffi.compile(tmpdir=cffi_dir, verbose=True)

from _9_1 import lib

with open('2018/data/9.txt', 'r') as infile:
    line = infile.read().split(' ')
    player_count, max_marble = int(line[0]), int(line[-2])

best = lib.marbles(player_count, max_marble*100)
print(best)
