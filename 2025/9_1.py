from itertools import combinations

with open('2025/data/9.txt', 'r') as infile:
    data = [tuple(map(int, (i.split(',')[0], i.split(',')[1]))) 
            for i in infile.read().split('\n')]

max_area = 0
for combo in combinations(data, 2):
    p1, p2 = combo
    p1x, p1y = p1 ; p2x, p2y = p2
    area = (abs(p1x - p2x) + 1) * (abs(p1y - p2y) + 1)
    if area > max_area:
        max_area = area
print(max_area)