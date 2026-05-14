string = [i for i in range(256)]

with open('2017/data/10.txt', 'r') as infile:
    lengths = list(map(int, infile.read().split(',')))

skip = 0 ; pointer = 0
for length in lengths:
    window_idxs = [i%len(string) for i in range(pointer, pointer+length)]
    rev_window_vals = reversed([string[i] for i in window_idxs])
    for flip, val in zip(window_idxs, rev_window_vals):
        string[flip] = val
    pointer = (pointer + length + skip)%len(string)
    skip += 1
print(string[0]*string[1])
