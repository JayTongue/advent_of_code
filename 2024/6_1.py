import numpy as np
import copy


def main():
	with open('data/6.txt', 'r') as file:
		data = [list(line.strip()) for line in file]
		data = np.array(data, dtype=str)
		data = data.squeeze()
		
		guard_movement = copy.deepcopy(data)
		path_marking = copy.deepcopy(data)
    
		path_marking, guard_movement = process_guard(guard_movement, path_marking)
		
		print(path_marking)
		#print(guard_movement)
		total_positions = get_coords(path_marking, 'X')
		print(f'Total Positions: {len(total_positions)}')
		
		
def process_guard(guard_movement, path_marking):
	guard_coord, guard_icon = find_guard(guard_movement)
	turn = False
	while True:
		try:
			path_marking[guard_coord] = 'X'
			guard_coord, guard_icon, turn = move_guard(guard_movement, guard_coord, guard_icon, turn)
		except IndexError:
			break
    
	return path_marking, guard_movement
    	
        
def move_guard(guard_movement, guard_coord, guard_icon, turn = False):
	# box_coordinates = get_coords(guard_movement, '#')
    
	if guard_icon == '^':
		next_coord = (guard_coord[0] - 1, guard_coord[1])
	elif guard_icon == 'v':
		next_coord = (guard_coord[0] + 1, guard_coord[1])
	elif guard_icon == '>':
		next_coord = (guard_coord[0], guard_coord[1] + 1)
	elif guard_icon == '<': 
		next_coord = (guard_coord[0], guard_coord[1] - 1)

	if next_coord[0] < 0 or next_coord[1] < 0:
		raise IndexError("Outside of Guard movements")
		
	next_coord_icon = guard_movement[next_coord[0], next_coord[1]]
	
	if next_coord_icon == '#':
		print(f'Blocked at {next_coord[0]}, {next_coord[1]}')
		return guard_coord, turn_guard(guard_icon), True
	else:
		return next_coord, guard_icon, False
	
		"""	

	if next_coord in box_coordinates: # rotates guard if it's against a box'
		new_icon = turn_guard(guard_icon)
		if turn:
			print('turn')
		return guard_coord, new_icon, turn
	else:
		turn = False
		return next_coord, guard_icon, turn
		"""
    	
    	
def turn_guard(guard_icon):
    guard_icons = ['^', '>', 'v', '<']
	try:
		guard_icon_index = guard_icons.index(guard_icon)
		new_guard_icon = guard_icons[guard_icon_index + 1]
	except IndexError:
		new_guard_icon = '^'
	return new_guard_icon

  
def find_guard(data):
	guard_icons = ['^', '>', 'v', '<'] # only one will exist
	for guard in guard_icons:
		finder = get_coords(data, guard)
		if finder != []:
			guard_coord = finder[0]
			guard_icon = guard		
	return guard_coord, guard_icon	
	

def get_coords(data, icon):
	finder = np.where(data == icon)
	finder = list(zip(finder[0], finder[1])) # -> list of tuples
	return finder

	

if __name__ == '__main__':
	main()