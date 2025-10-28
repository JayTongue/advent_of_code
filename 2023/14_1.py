from helpers.timer_func import timer

@timer
def main():
	with open('data/14.txt', 'r') as data:
		data = [list(line) for line in data.read().splitlines()]
	roundies = sorted([(line_count, place_count) for line_count, line in enumerate(data) for place_count, place in enumerate(line) if place == 'O'])
	squaries = sorted([(line_count, place_count) for line_count, line in enumerate(data) for place_count, place in enumerate(line) if place == '#'])
	new_roundies = []

	for roll_row, roll_col in roundies:
		new_row = max((square_row + 1 for square_row, square_col in squaries if square_col == roll_col and square_row < roll_row), default=0)
		while (new_row, roll_col) in new_roundies or (new_row, roll_col) in squaries:
			new_row += 1
		new_roundies.append((new_row, roll_col))
		
	print(f'total: {sum(len(data) - row for row, _ in new_roundies)}')

if __name__ == "__main__":
	main()