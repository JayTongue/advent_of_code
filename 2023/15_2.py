from helpers.timer_func	import timer
from functools import reduce
import re

@timer
def main():
	with open('data/15.txt', 'r') as data:
		data = data.read().split(',')

	def hash_datum(datum):
		return reduce(lambda total, char: ((total + ord(char)) * 17) % 256, datum, 0)

	boxes = {key: [] for key in range(256)}
	for lens in data:
		if re.findall('-', lens):
			new_label = lens[:-1]
			boxes[hash_datum(new_label)] = [(l, p) for (l, p) in boxes[hash_datum(new_label)] if l != new_label]
		elif re.findall('=', lens):
			new_label, new_power = lens.split('=')
			correct_box = hash_datum(new_label)
			if any([l == new_label for l, p in boxes[correct_box]]):
				boxes[correct_box] = [(new_label, new_power) if l == new_label else (l, p) for (l, p) in boxes[correct_box]]
			else:
				boxes[correct_box].append((new_label, new_power))
	total = 0
	for box in boxes:
		total += sum([(box + 1) * int(lens[1][1]) * (lens[0] + 1) for lens in enumerate(boxes[box])])
	print(total)

if __name__ == '__main__':
	main()