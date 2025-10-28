import re
from helpers.timer_func import timer

@timer
def main():
	data = open('data/4.txt', 'r').read().split('\n')
	cards = [((j for j in i.split(' ') if j) for i in re.split(r':|\|', line)) for line in data]
	total_score = 0
	for card in cards:
		_, winning, have = card
		have, winning, = set(have), set(winning)
		hits = int(2 ** (len(have & winning) - 1))
		total_score += hits
	print(f'Total Points: {total_score}')

if __name__ == '__main__':
	main()