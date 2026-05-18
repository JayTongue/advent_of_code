with open('2017/data/13.txt', 'r') as infile:
    orig_layers = infile.read().split('\n')
orig_layers = {h[0]:h[1]-1 for h in [list(map(int, l.split(': '))) for l in orig_layers]}

offset = 0
while True:
    found = False
    for layer in range(0, max(orig_layers.keys())+1):
        time_there = offset + layer
        if layer in orig_layers.keys():
            if time_there % (orig_layers[layer]*2) == 0:
                found = True
                break
    if not found:
        print(offset)
        break
    offset += 1            