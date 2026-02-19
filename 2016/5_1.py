import hashlib

with open('2016/data/5.txt', 'r') as infile:
    door_id = infile.read()

sol = [] ; numbers = 0 ; lim = 8

while len(sol) < lim:
    trying = door_id + str(numbers)
    hashed = hashlib.md5((door_id + str(numbers)).encode()).hexdigest()
    if hashed[:5] == '00000':
        sol.append(hashed[5])
    numbers += 1
print(''.join(sol))