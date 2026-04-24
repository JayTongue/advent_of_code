import re

with open('2015/data/8.txt', 'r') as infile:
    data = infile.read()
    literal_length = sum([len(i) for i in data.split('\n')])

    def find_hex(m):
        return bytes.fromhex(m.group(1)).decode('latin-1')
    data = data.replace(r'\"', '"').replace(r'\\', '\\')
    data = re.sub(r'\\x([0-9a-fA-F]{2})', find_hex, data).split('\n')
mem_length = [len(i)-2 for i in data]
print(literal_length - sum(mem_length))