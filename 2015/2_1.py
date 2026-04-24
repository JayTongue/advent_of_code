with open('2015/data/2.txt', 'r') as infile:
    data = infile.read().split('\n')
    data = [list(map(int, i.split('x'))) for i in data]
    
print(sum([2*l*w + 2*w*h + 2*h*l + min((l*w, w*h, h*l)) for l, w, h in data]))