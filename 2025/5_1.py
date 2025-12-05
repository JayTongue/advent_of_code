with open('2025/data/5.txt', 'r') as infile:
    ranges, items = infile.read().split('\n\n')
ranges, items = [[int(i.split('-')[0]), int(i.split('-')[1])] for i in ranges.split('\n')], map(int, items.split('\n'))

ranges.sort(key=lambda x: x[0])
merged = []
cur_start, cur_end = ranges[0]

for trial_start, trial_end in ranges[1:]:
    if trial_start <= cur_end + 1:
        cur_end = max((trial_end, cur_end))
    else:
        merged.append([cur_start, cur_end])
        cur_start, cur_end = trial_start, trial_end
merged.append([cur_start, cur_end])

fresh = 0
for item in items:
    for s, e in merged:
        if s <= item <= e:
            fresh += 1
            break
print(fresh)