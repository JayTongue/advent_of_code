known_sue = {'children': 3, 
             'cats': 7, 
             'samoyeds': 2, 
             'pomeranians': 3, 
             'akitas': 0, 
             'vizslas': 0, 
             'goldfish': 5, 
             'trees': 3, 
             'cars': 2, 
             'perfumes': 1}

sues = {}
with open('2015/data/16.txt', 'r') as infile:
    data = [i.replace(':', '').replace(',', '').split(' ') for i in infile.read().split('\n')]
    for sue in data:
        sues[sue[1]] = {sue[2]: int(sue[3]), 
                        sue[4]: int(sue[5]), 
                        sue[6]: int(sue[7])}
for idx, val in sues.items():
    right = True
    for qual in val:
        if qual in ('trees', 'cats'): #greater than
            if known_sue[qual] >= val[qual]:
                right = False
        elif qual in ('pomeranians', 'goldfish'): #lesser than
            if known_sue[qual] <= val[qual]:
                right = False
        else:
            if known_sue[qual] != val[qual]:
                right = False
    if right:
        break
print(idx)

