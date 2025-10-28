import copy 
import itertools


def main():
	infile = open('data/8.txt', 'r')
	data_array = [list(line.strip()) for line in infile]
	#for line in data_array:
	#	print(line)
	x_lim = len(data_array[0]) - 1
	y_lim = len(data_array) - 1
	
	antenna_locations = build_antenna_locations(data_array)
	
	antinodes = find_antinodes(data_array, antenna_locations, x_lim, y_lim)
	
	
	for antinode in antinodes:
		data_array[antinode[0]][antinode[1]] = '#'
	
	for line in data_array:
		print(line)
	
	
def build_antenna_locations(data_array):
	antenna_locations = {}
	for row_count, row in enumerate(data_array):
		for column_count, char in enumerate(row):
			if char != '.':
				if char in antenna_locations:
					antenna_locations[char].append([row_count, column_count])
				else:
					antenna_locations[char] = [[row_count, column_count]]
	return antenna_locations


def find_antinodes(data_array, antenna_locations, x_lim, y_lim):
	antinodes = set()
	for antenna_type in antenna_locations:
		antenna_coords = antenna_locations[antenna_type]
		antenna_coord_combos = list(itertools.product(antenna_coords, repeat=2))
		
		antenna_coord_combos = [coord for coord in antenna_coord_combos if coord[0] != coord[1]]
		for combo in antenna_coord_combos:
			dist_x = combo[1][0] - combo[0][0]
			dist_y = combo[1][1] - combo[0][1]
			anti_x = combo[1][0] + dist_x
			anti_y = combo[1][1] + dist_y
			while 0 <= anti_x <= x_lim and 0 <= anti_y <= y_lim:
				antinode = (anti_x, anti_y)
				print(combo, '=', antinode)
				antinodes.add(antinode)
				anti_x = anti_x + dist_x
				anti_y = anti_y + dist_y
			antinodes.add(tuple(combo[0]))
			antinodes.add(tuple(combo[1]))

	print(f'Total antinodes: {len(antinodes)}')
	return antinodes


if __name__ == '__main__':
	main()