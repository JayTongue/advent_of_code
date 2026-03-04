'''
ADVENT contains no markers and decompresses to itself with no changes, resulting in a decompressed length of 6.
A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a decompressed length of 7.
(3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.
A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a decompressed length of 11.
(6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but because it's within a data section of another marker, it is not treated any differently from the A that comes after it. It has a decompressed length of 6.
X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18), because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped and not processed further.
'''

import re

data = '''ADVENT
A(1x5)BC
(3x3)XYZ
A(2x2)BCD(2x2)EFG
(6x1)(1x3)
X(8x2)(3x3)ABCY'''.split('\n')

for line in data:
    replacements = list(map(lambda x: tuple(map(int, x.split('x'))), 
                            re.findall(r'\((.*?)\)', line)))
    open_brack = [idx for idx in range(len(line)) if line[idx] == '(']
    close_brack = [idx for idx in range(len(line)) if line[idx] == ')']
    brack_delimiters = list(map(tuple, zip(open_brack, close_brack)))
    brack_delimiters = {k: v for k, v in zip(brack_delimiters, replacements)}
    print(line, brack_delimiters)
    for idx, character in enumerate(line):
        if idx in open_brack:
            window = idx + replacements[0][2]


