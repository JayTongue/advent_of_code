import re

with open('2016/data/9.txt', 'r') as infile:
    line = infile.read()

def line_walk(line):
    i = 0
    result = []
    while i < len(line):
        if line[i] == '(':
            end = line.index(')', i) # (find, start, stop)
            length, times = map(int, line[i+1:end].split('x'))
            chunk = line[end+1 : end+1+length]
            result.append(chunk * times)
            i = end + 1 + length
        else:
            result.append(line[i])
            i += 1
    return ''.join(result)

print(len(line_walk(line)))