import re
from helpers.timer_func import timer

@timer
def main():
	data = open('data/3.txt', 'r').read().split('\n')
	special_indices = index_special_chars(data)
	# print(special_indices)

	total_sums = 0
	for row_count, line in enumerate(data):
		matches = [(m.group(), m.start(), m.end()) for m in re.finditer(r'\d+', line)]
		# print(row_count, matches)
		for match in matches:
			number, start_index, end_index = match
			for special in special_indices:
				special_row, special_col = special
				if (row_count + 1 >= special_row >= row_count - 1) and (start_index - 1 <= special_col <= end_index):
					total_sums += int(number)
					# print(f'matching {number} at {start_index}, {end_index} to {special}')
	print(f'Total Sums: {total_sums}')


def index_special_chars(data):
	special_chars = ['%', '*', '$', '+', '&', '=', '@', '-', '#', '/']
	special_indices = [(i, j) for i, row in enumerate(data) for j, val in enumerate(row) if val in special_chars]
	return special_indices



if __name__ == '__main__':
	main()