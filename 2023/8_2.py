import re
from math import lcm
from helpers.timer_func import timer

@timer
def main():
	instr, maps = open('data/8.txt', 'r').read().split('\n\n')
	maps = {source: (left, right) for submap in maps.split('\n') for source, left, right in [re.findall(r'[A-Z0-9]{3}', submap)]}
	instr = [1 if i == 'R' else 0 for i in list(instr)]

	all_starts = set([j for j in maps if re.findall(r'\w\wA', j)])
	all_ends = set([h for h in maps if re.findall(r'\w\wZ', h)])

	def walk_instructions(instr, maps, element):
		count = 0
		instr_len = len(instr)
		while element not in all_ends:
			step = instr[count % instr_len]
			element = maps[element][step]
			count += 1
		return count

	starts = []
	for start in all_starts:
		count = walk_instructions(instr, maps, start)
		starts.append(count)
	
	print(f'Convergence: {lcm(*starts)}')

		
if __name__ == '__main__':
	main()