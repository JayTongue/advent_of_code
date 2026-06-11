import copy

with open('2018/data/5.txt', 'r') as infile:
    perm = list(infile.read())
case_match = {i: i.upper() for i in list('abcdefghijklmnopqrstuvwxyz')}

lowest = float('inf')
for key in case_match:
    poly = [i for i in copy.deepcopy(perm) if i not in (key, case_match[key])]

    stack = []
    for p in poly:
        if not len(stack):
            stack.append(p)
        else:
            if p in case_match.keys() and case_match[p] == stack[-1]:
                stack.pop()
            elif stack[-1] in case_match.keys() and case_match[stack[-1]] == p:
                stack.pop()
            else:
                stack.append(p)

    ans = len(stack)
    if ans < lowest:
        lowest = ans
print(lowest)
