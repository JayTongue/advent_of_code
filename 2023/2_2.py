import re
from helpers.timer_func import timer

@timer
def main():
	data = open('data/2.txt', 'r').read()
	data = data.split('\n')
	data = [game.split(':') for game in data]

	total_power = 0
	for game_number, revealed in data:
		game_number = int(game_number.split(' ')[1])
		revealed = re.sub(r',', '', revealed)
		reveals = revealed.split(';')

		game_dict = {'red': 0, 'green': 0, 'blue': 0}
		for reveal in reveals: 
			reveal = reveal.split(' ')[1:]
			turn_dict = dict(zip(reveal[1::2], map(int, reveal[::2])))
			for color in turn_dict:
				if turn_dict[color] > game_dict[color]:
					game_dict[color] = turn_dict[color]
		# print(game_dict)

		power = 1	
		for color in game_dict:
			power *= game_dict[color]

		
		total_power += power
	
	print(f'total_power: {total_power}')
	

if __name__ == '__main__':
	main()