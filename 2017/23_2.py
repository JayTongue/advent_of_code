from math import isqrt


registers = {i: 0 for i in list('abcdefgh')}
registers['a'] = 1

with open('2017/data/23.txt', 'r') as infile:
    commands = [i.split(' ') for i in infile.read().strip().split('\n')]

b = int(commands[0][2])
c = b
if registers['a'] != 0:
    b = b * 100 + 100000
    c = b + 17000

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

h = 0

for x in range(b, c + 1, 17):
    if not is_prime(x):
        h += 1

print(h)