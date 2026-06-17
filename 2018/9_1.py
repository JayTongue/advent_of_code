from itertools import cycle

with open('2018/data/9.txt', 'r') as infile:
    line = infile.read().split(' ')
    player_count, marble_max = int(line[0]), int(line[-2])

player_dict = {i: 0 for i in range(1, player_count+1)}
player_iter = cycle(player_dict.keys())

marbles = [0] #constant time for indexing, but O(n) for inserting.
idx = 1

for marble in range(1, marble_max+1):
    player = next(player_iter)
    if marble % 23 == 0:
        player_dict[player] += marble
        idx = (idx-7) % len(marbles)
        player_dict[player] += marbles.pop(idx)
    else:
        idx += 2
        if idx > len(marbles):
            idx %= len(marbles)
        marbles.insert(idx, marble)
print(max(player_dict.values()))