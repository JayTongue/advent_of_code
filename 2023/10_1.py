from helpers.timer_func import timer

@timer
def main():
	data = [list(i) for i in open('data/10.txt', 'r').read().splitlines()]
	start = [(count, row.index('S')) for count, row in enumerate(data) if 'S'in row][0]
	up, down, left, right = ((start[0]-1, start[1]), (start[0]+1, start[1]), (start[0], start[1]-1), (start[0], start[1]+1))
	directions = {up: {'|', '7', 'F'}, down: {'J', 'L', '|'}, right: {'-', '7', 'J'}, left: {'-', 'L', 'F'}}
	starts = [direction for direction, valid_chars in directions.items() if data[direction[0]][direction[1]] in valid_chars]
	starts = [d for d, v in directions.items() if data[d[0]][d[1]] in v]
	run_map(data, starts[0], {start, starts[0]})

def run_map(data, start, walked):
    while (new_step := find_next_step(data, start) - walked):
        start = new_step.pop()
        walked.add(start)
    print(f'loop length: {len(walked) // 2}')

def find_next_step(data, current_coord):
	current_symb = data[current_coord[0]][current_coord[1]]
	walk_dict = {'|': ((-1, 0), (1, 0)), '-': ((0, -1), (0, 1)), 'L': ((-1, 0), (0, 1)), 'J': ((-1, 0), (0, -1)), '7': ((0, -1), (1, 0)), 'F': ((0, 1), (1, 0))}
	new_candidates = {(current_coord[0] + walk_dict[current_symb][0][0], current_coord[1] + walk_dict[current_symb][0][1]), 
				   (current_coord[0] + walk_dict[current_symb][1][0], current_coord[1] + walk_dict[current_symb][1][1])}
	return new_candidates

if __name__ == '__main__':
	main()