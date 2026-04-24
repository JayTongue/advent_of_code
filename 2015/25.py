import re
from pprint import pprint

with open('2015/data/25.txt', 'r') as infile:
    row, col = map(int, re.findall(r'\d+', infile.read()))

# print(row, col)

def generate_numbers(starter):
    return (starter * 252533) % 33554393
# def generate_numbers(starter):
    # return starter + 1

list_of_lists = []
starter = 20151125
# starter = 1
# for _ in range(4):
while True:
    try:
        for idx in range(len(list_of_lists)):
            list_of_lists[idx].append(starter)
            starter = generate_numbers(starter)
    except:
        pass
    list_of_lists.append([starter])
    starter = generate_numbers(starter)
    # pprint(list_of_lists)
    
    if len(list_of_lists) > col:
        try: 
            if len(list_of_lists[col]) > row:
                break
        except IndexError:
            pass

print(list_of_lists[col-1][row-1])