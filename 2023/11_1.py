import itertools
from helpers.timer_func import timer

@timer
def main():
	data = [list(line) for line in open('data/11.txt', 'r').read().split('\n')]
	data = expand_galaxy(data)
	galaxies = [(row_count, col_count) for row_count, row in enumerate(data) for col_count, _ in enumerate(row) if data[row_count][col_count] == '#']
	galaxy_pairs = list(itertools.combinations(galaxies, 2))
	print(f'total: {sum(abs(one[0] - two[0]) + abs(one[1] - two[1]) for one, two in galaxy_pairs)}')

def expand_galaxy(data):
	spaces = [length for length in range(len(data[0])) if all([row[length] == '.' for row in data])]
	for count, space in enumerate(spaces):
		for row in data:
			row.insert(space + count, '.')
	data = [row for row in data for _ in (0, 1) if _ == 0 or all(char == '.' for char in row)]
	return data

if __name__ == '__main__':
	main()