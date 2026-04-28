with open('2016/data/16.txt','r') as infile:
    data = infile.read()
finish_length = 272

def copy(a):
    a = str(a)
    b = ''.join(['1' if i == '0' else '0' for i in reversed(a)])
    return f'{a}0{b}'

while True:
    if len(data) >= finish_length:
        break
    data = copy(data)
data = data[:finish_length]

def make_checksum(data):
    checksum = []
    for i in range(0, len(data), 2):
        pair = data[i:i+2]
        if len(set(pair)) == 1:
            checksum.append('1')
        else:
            checksum.append('0')
    return ''.join(checksum)

while True:
    checksum = make_checksum(data)
    if len(checksum) % 2 == 1:
        print(checksum)
        break
    else:
        data = checksum

