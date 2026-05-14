import re

with open('2017/data/9.txt', 'r') as infile:
    line = infile.read()

line = re.sub(r'\!.', '', line)
line = re.sub(r'<.*?>', '', line)
indent = 0 ; score = 0
opens = [i for i in range(len(line)) if line[i] == '{']
closes = [i for i in range(len(line)) if line[i] == '}']
brack_count = {}
for i in range(len(line)):
    if line[i] == '{':
        brack_count[i] = True
    elif line[i] == '}':
        corresponding_open = max([k for k, v in brack_count.items() if v == True])
        score += sum([v for k, v in brack_count.items() if k < i])
        brack_count[corresponding_open] = False
print(score)
