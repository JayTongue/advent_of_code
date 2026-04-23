'''
ADVENT contains no markers and decompresses to itself with no changes, resulting in a decompressed length of 6.
A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a decompressed length of 7.
(3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.
A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a decompressed length of 11.
(6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but because it's within a data section of another marker, it is not treated any differently from the A that comes after it. It has a decompressed length of 6.
X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18), because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped and not processed further.
'''

import re

with open('2016/data/9.txt', 'r') as infile:
    line = infile.read()

# data = '''ADVENT
# A(1x5)BC
# (3x3)XYZ
# A(2x2)BCD(2x2)EFG
# (6x1)(1x3)A
# X(8x2)(3x3)ABCY'''.split('\n')


def line_walk(line):
    i = 0
    result = []
    while i < len(line):
        if line[i] == '(':
            end = line.index(')', i)
            length, times = map(int, line[i+1:end].split('x'))
            chunk = line[end+1 : end+1+length]
            result.append(chunk * times)
            i = end + 1 + length
        else:
            result.append(line[i])
            i += 1
    return ''.join(result)

print(len(line_walk(line)))