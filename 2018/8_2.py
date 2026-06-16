# puz = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')
with open('2018/data/8.txt', 'r') as infile:
    puz = infile.read().split(' ')
puz = [int(i) for i in puz]

md_sum = 0

def find_chunk(start_idx, puz):
    ch_count, md_count = puz[start_idx], puz[start_idx+1]
    start_idx += 2
    children = []
    for _ in range(ch_count):
        start_idx, child_val = find_chunk(start_idx, puz)
        children.append(child_val)

    metadata = puz[start_idx:start_idx+md_count]
    if ch_count == 0:
        val = sum(metadata)
    else:
        val = 0
        for idx in metadata:
            if 1 <= idx <= len(children):
                val += children[idx-1]
    start_idx += md_count

    return start_idx, val


start_idx, md_sum = find_chunk(0, puz)
print(md_sum)