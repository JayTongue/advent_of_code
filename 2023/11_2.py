import itertools
from helpers.timer_func import timer

@timer
def main():
	data = [list(line) for line in open('data/11.txt', 'r').read().splitlines()]
	col_spaces, row_spaces = find_spaces(data)
	galaxies = [(row_count, col_count) for row_count, row in enumerate(data) for col_count, _ in enumerate(row) if data[row_count][col_count] == '#']
	total, spacing = 0, 999_999
	for one, two in list(itertools.combinations(galaxies, 2)):
		one_row, one_col = one
		two_row, two_col = two
		total += abs(one_row - two_row) + abs(one_col - two_col)
		total += sum([spacing for row_space in row_spaces if one_row > row_space > two_row or one_row < row_space < two_row])
		total += sum([spacing for col_space in col_spaces if one_col > col_space > two_col or one_col < col_space < two_col])
	print(f'Total: {total}')

def find_spaces(data):
	col_spaces = {col for col in range(len(data[0])) if all(row[col] == '.' for row in data)}
	row_spaces = {count for count, row in enumerate(data) if all(char == '.' for char in row)}
	return col_spaces, row_spaces

if __name__ == '__main__':
	main()