import re
from functools import reduce
from operator import mul
from helpers.timer_func import timer

@timer
def main():
	data = open('data/3.txt', 'r').read().split('\n')
	special_indices = [(i, j) for i, row in enumerate(data) for j, val in enumerate(row) if val == '*']
	# print(special_indices)

	total_gear = 0
	for gear in special_indices:
		gear_row, gear_col = gear
		considered_rows = [r for r in (gear_row - 1, gear_row, gear_row + 1) if 0 <= r < len(data)]
		proximal = []
		for row in considered_rows:
			numbers = [(m.group(), m.start(), m.end()) for m in re.finditer(r'\d+', data[row])]
			for number in numbers:
				val, start, end = number
				end = end - 1
				if gear_col in set(range(start - 1, end + 2)):
					proximal.append(int(val))
		# print(f'{gear}, considering rows {considered_rows}, finding {proximal}')
		if len(proximal) >= 2:		
			total_gear += reduce(mul, proximal)
	print(f'Total Sums: {total_gear}')


if __name__ == '__main__':
	main()