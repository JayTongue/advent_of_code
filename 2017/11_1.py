with open('2017/data/11.txt', 'r') as infile:
    steps = infile.read().split(',')

counter = {i:0 for i in ['n', 'ne', 'se', 's', 'sw', 'nw']}
for s in steps:
    counter[s] += 1
for a, b in [{'n', 's'}, {'ne', 'sw'}, {'nw', 'se'}]:
    least = min((counter[a], counter[b]))
    counter[a] -= least ; counter[b] -= least

pairs = {('n', 'se'): 'ne', 
        ('ne','s'): 'se', 
        ('se','sw'): 's', 
        ('s','nw'): 'sw', 
        ('sw','n'): 'nw', 
        ('nw','ne'): 'n',}
while True:
    changed = False
    for c, d in pairs:
        if counter[c] and counter[d]:
            least = min((counter[c], counter[d]))
            counter[c] -= least ; counter[d] -= least
            counter[pairs[(c, d)]] += least
            changed = True
    if not changed:
        break

print(sum(counter.values()))
