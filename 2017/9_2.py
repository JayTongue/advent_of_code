import re

with open('2017/data/9.txt', 'r') as infile:
    line = infile.read()

line = re.sub(r'\!.', '', rf'{line}')
garbage = re.findall(r'<.*?>', rf'{line}')
print(sum([len(g)-2 for g in garbage]))