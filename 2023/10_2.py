from helpers.timer_func import timer
import re

@timer
def main():
	data = [list(i) for i in open('data/10.txt', 'r').read().splitlines()]
	start = [(count, row.index('S')) for count, row in enumerate(data) if 'S'in row][0]
	up, down, left, right = ((start[0]-1, start[1]), (start[0]+1, start[1]), (start[0], start[1]-1), (start[0], start[1]+1))
	directions = {up: {'|', '7', 'F'}, down: {'J', 'L', '|'}, right: {'-', '7', 'J'}, left: {'-', 'L', 'F'}}
	starts = [direction for direction, valid_chars in directions.items() if data[direction[0]][direction[1]] in valid_chars]
	starts = [d for d, v in directions.items() if data[d[0]][d[1]] in v]
	walked = run_map(data, starts[0], {start, starts[0]})
	make_new_map(data, walked, start)

def make_new_map(data, walked, start):
	new_map = [['.' if (r, c) not in walked else char for c, char in enumerate(row)] for r, row in enumerate(data)]
	new_map[start[0]][start[1]] = '-' # this is ideosyncratic depending on what makes a completed loop for your map
	count = 0
	for row in new_map:
		new_row = ''.join([char for char in row if char != '-'])
		new_row = re.sub(r'FJ|L7', r'|', new_row)
		new_row = re.sub(r'F|J|L|7', r'', new_row)
		inside = False
		for i in new_row:
			if i == '|':
				inside = not inside
			elif inside and i == '.':
				count += 1
	print(f'Enclosed:{count}')

def run_map(data, start, walked):
	while (new_step := [s for s in find_next_step(data, start) if s not in walked]):
		start = new_step[0]
		walked.add(start)
	return walked

def find_next_step(data, current_coord):
	current_symb = data[current_coord[0]][current_coord[1]]
	walk_dict = {'|': ((-1, 0), (1, 0)), '-': ((0, -1), (0, 1)), 'L': ((-1, 0), (0, 1)), 'J': ((-1, 0), (0, -1)), '7': ((0, -1), (1, 0)), 'F': ((0, 1), (1, 0))}
	new_candidates = {(current_coord[0] + walk_dict[current_symb][0][0], current_coord[1] + walk_dict[current_symb][0][1]), 
				   (current_coord[0] + walk_dict[current_symb][1][0], current_coord[1] + walk_dict[current_symb][1][1])}
	return new_candidates

if __name__ == '__main__':
	main()