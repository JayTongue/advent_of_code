with open('2015/data/19.txt', 'r') as infile:
    replacements, starter = infile.read().split('\n\n')

    repl_dict = {}
    for i in replacements.split('\n'):
        k, v, = i.split(' => ')
        repl_dict[v] = k

counter = 0
while starter != 'e':
    for k in repl_dict.keys():
        if k in starter:
            starter = starter.replace(k, repl_dict[k], 1)
            counter += 1
            
print(counter)    
