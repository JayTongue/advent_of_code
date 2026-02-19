import hashlib

with open('2016/data/5.txt', 'r') as infile:
    door_id = infile.read()

lim = 8
sol = [None for _ in range(lim)] ; numbers = 0

while not all(sol):
    trying = door_id + str(numbers)
    hashed = hashlib.md5((door_id + str(numbers)).encode()).hexdigest()
    if hashed[:5] == '00000' and (hashed[5] in [str(i) for i in range(lim)]) and not sol[int(hashed[5])]:
        sol[int(hashed[5])] = hashed[6]
    numbers += 1
print(''.join(sol))