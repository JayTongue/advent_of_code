with open('2018/data/8.txt', 'r') as infile:
    puz = infile.read().split(' ')
puz = [int(i) for i in puz]

md_sum = 0

def find_chunk(start_idx, puz, md_sum):
    ch_count, md_count = puz[start_idx], puz[start_idx+1]
    start_idx += 2
    for _ in range(ch_count):
        start_idx, md_sum = find_chunk(start_idx, puz, md_sum)
    md_sum += sum(puz[start_idx:start_idx+md_count])
    start_idx += md_count

    return start_idx, md_sum

start_idx, md_sum = find_chunk(0, puz, md_sum)
print(md_sum)