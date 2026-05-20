from functools import reduce
from operator import xor

def knot_hash(in_str):
    string = list(range(256))
    lengths = [ord(l) for l in in_str] + [17, 31, 73, 47, 23]
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
    return ''.join(format(b, '02x') for b in blocks)

def binify(start_string):
    return ''.join([str(bin(int(char, 16))[2:].zfill(4)) for char in list(start_string)])

start_str = 'ljoxqyyw'
starts = [f'{start_str}-{i}' for i in range(128)]
starts = [binify(b) for b in list(map(knot_hash, starts))]

print(sum([sum(list(map(int, list(s)))) for s in starts]))

