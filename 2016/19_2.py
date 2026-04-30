with open('2016/data/19.txt', 'r') as infile:
    lim = int(infile.read())

ape_outcomes = [0]
powers = [] ; power = 0

while True:
    powers.append(3**power)
    if 3**power > lim:
        break
    power += 1

reset = True
for puz in range(2, lim+1):
    if reset:
        ape = 1
        reset = False
    else:
        if puz in powers:
            ape = puz
            reset = True
        elif ape_outcomes[-1]+1 <= puz/2:
            ape = ape_outcomes[-1]+1
        else:
            ape = ape_outcomes[-1]+2
    ape_outcomes.append(ape)
print(ape_outcomes[-1])