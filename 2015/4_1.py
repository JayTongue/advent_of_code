from hashlib import md5

with open('2015/data/4.txt', 'r') as infile:
    key = infile.read()

d = 0
while True:
    guess = f'{key}{d}'
    if str(md5(guess.encode()).hexdigest())[:5] == '00000':
        break
    d += 1
print(d)