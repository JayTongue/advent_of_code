with open('2025/data/2.txt', 'r') as infile:
    data = infile.read().split(',')
data = [(int(start), int(end)) for i in data for (start, end) in [i.split('-')]]

invalid_count = 0

for drange in data:
    start, end = drange
    for prod in range(start, end+1):
        str_prod = str(prod)
        begin, end = str_prod[:len(str_prod)//2], str_prod[len(str_prod)//2:]
        if begin == end:
            invalid_count += prod
print(invalid_count)
