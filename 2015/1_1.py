with open('2015/data/1.txt', 'r') as infile:
    print(sum([1 if i == '(' else -1 for i in list(infile.read())]))