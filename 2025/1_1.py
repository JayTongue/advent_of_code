with open('2025/data/1.txt', 'r') as infile:
    data = infile.read().split('\n')
data = [(turn[0], int(turn[1:])) for turn in data]

start_point = 50

def make_turn(start_point, turn):
    if turn[0] == 'R':
        start_point += turn[1]
    else:
        start_point -= turn[1]
    return abs(start_point % 100)

zero_count = 0
for turn in data:
    start_point = make_turn(start_point, turn)
    if start_point == 0:
        zero_count += 1

print(zero_count)
