import re
from helpers.timer_func import timer

@timer
def main():
	instr, maps = open('data/8.txt', 'r').read().split('\n\n')
	maps = {source: (left, right) for submap in maps.split('\n') for source, left, right in [re.findall(r'[A-Z]{3}', submap)]}
	instr = [1 if i == 'R' else 0 for i in list(instr)]

	def walk_instructions(instr, maps, element):
		count = 0
		instr_len = len(instr)
		while element != 'ZZZ':
			step = instr[count % instr_len]
			element = maps[element][step]
			count += 1
		return count

	count = walk_instructions(instr, maps, 'AAA')
	print(f'Final Count: {count}')

		
if __name__ == '__main__':
	main()