with open('2016/data/9.txt', 'r') as infile:
    line = infile.read()

def line_walk(line, result=0):
    i = 0
    while i < len(line):
        if line[i] == '(':
            end = line.index(')', i) # (find, start, stop)
            length, times = map(int, line[i+1:end].split('x'))
            chunk = line[end+1 : end+1+length]
            if '(' in chunk:
                small_sum = line_walk(chunk)
                result += small_sum * times
            else:
                result += len(chunk) * times
            i = end + 1 + length
        else:
            result += 1
            i += 1
    return result

print(line_walk(line))
