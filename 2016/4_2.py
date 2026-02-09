import re
from collections import Counter

with open('2016/data/4.txt', 'r') as infile:
    data = [re.split(r'\-|\[', re.sub(r']', '', i)) for i in infile.read().split('\n')]

letters_list = 'abcdefghijklmnopqrstuvwxyz'* int(1e2)
for d in data:
    counts = Counter()
    for chunk in d[:-2]:
        for c in chunk:
            counts[c] += 1
    counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    checksum = []
    for i in range(counts[0][1], 0, -1):
        letters = [l[0] for l in counts if l[1] == i]
        checksum += sorted(letters)

    if d[-1] == ''.join(checksum[:5]):
        room_name = ' '.join(d[:-2]); new_name = ''
        for letter in room_name:
            if letter == ' ':
                new_name += ' '
            else:
                start_idx = letters_list.index(letter)
                new_name += letters_list[start_idx + int(d[-2])]
        if re.search(r'north', new_name):
            print(int(d[-2]))
            break




