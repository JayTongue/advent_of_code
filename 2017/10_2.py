from functools import reduce
from operator import xor

string = list(range(256))
with open('2017/data/10.txt', 'r') as infile:
    lengths = [ord(l) for l in infile.read()] + [17, 31, 73, 47, 23]

skip = 0 ; pointer = 0
for _ in range(64):
    for length in lengths:
        window_idxs = [i % len(string) for i in range(pointer, pointer + length)]
        rev_window_vals = list(reversed([string[i] for i in window_idxs]))
        for flip, val in zip(window_idxs, rev_window_vals):
            string[flip] = val
        pointer = (pointer + length + skip) % len(string)
        skip += 1
blocks = []
for i in range(16):
    blocks.append(reduce(xor, [string[i * 16 + j] for j in range(16)]))

dense_hash = ''.join(format(b, '02x') for b in blocks)
print(dense_hash)