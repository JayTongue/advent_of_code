with open('2018/data/5.txt', 'r') as infile:
    poly = list(infile.read())
case_match = {i: i.upper() for i in list('abcdefghijklmnopqrstuvwxyz')}

stack = [poly[0]]
for p in poly[1:]:
    if not len(stack):
        stack.append(p)
    else:
        if p in case_match.keys() and case_match[p] == stack[-1]:
            stack.pop()
        elif stack[-1] in case_match.keys() and case_match[stack[-1]] == p:
            stack.pop()
        else:
            stack.append(p)
print(len(stack))