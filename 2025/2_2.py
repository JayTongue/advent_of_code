with open('2025/data/2.txt', 'r') as infile:
    data = infile.read().split(',')
data = [(int(start), int(end)) for i in data for (start, end) in [i.split('-')]]

invalid_count = 0

for drange in data:
    start, end = drange
    for prod in range(start, end+1):
        str_prod = str(prod)

        for chunk in range(1, len(str_prod)//2+1):
            if len(str_prod) % chunk == 0:
                check_bag = [str_prod[i:i+chunk] for i in range(0, len(str_prod), chunk)]
                check_bag = set(check_bag)
                if len(check_bag) == 1:
                    invalid_count += prod
                    break # avoids double counting e.g. 22,22,22 as 222,222
print(invalid_count)
