from collections import Counter

with open('2018/data/2.txt', 'r') as infile:
    boxes = [list(i) for i in infile.read().split('\n')]

twos, threes = 0, 0
for box in boxes:
    box = Counter(box)
    if 2 in box.values():
        twos += 1
    if 3 in box.values():
        threes += 1
print(twos * threes)