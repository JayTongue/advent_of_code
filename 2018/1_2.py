with open('2018/data/1.txt', 'r') as infile:
    changes = infile.read().replace('+', '').split('\n')
changes = list(map(int, changes))

seen = set()
val = 0
pointer = 0
while True:
    change = changes[pointer % len(changes)]
    if val in seen:
        print(val)
        break
    else:
        seen.add(val)
        val += change
    pointer += 1