import json

with open('2015/data/12.txt', 'r') as infile:
    data = json.load(infile)

def recur_searching(in_obj, ints=[]):
    if isinstance(in_obj, dict):
        if 'red' not in in_obj.keys() and 'red' not in in_obj.values():
            for val in in_obj.values():
                recur_searching(val, ints)
    elif isinstance(in_obj, list):
        for item in in_obj:
            recur_searching(item, ints)
    elif isinstance(in_obj, int):
        ints.append(in_obj)
    return ints

print(sum(recur_searching(data)))