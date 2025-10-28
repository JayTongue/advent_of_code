import re
from helpers.timer_func import timer
from functools import reduce

@timer
def main():
	seeds, *maps = open('data/5.txt', 'r').read().split('\n\n')
	seeds = map(int, seeds.split(' ')[1:])
	maps = [[list(map(int, number.split(' '))) for number in submap.split('\n')[1:]] for submap in maps]
	s2s, s2f, f2w, w2l, l2t, t2h, h2l = maps

	def lookup_in_map(in_val, submap):
		for map_chunk in submap:
			destination, source, span = map_chunk
			out_val = in_val
			if source <= in_val <= (source + span):
				out_val = destination + (in_val - source)
				break
		return out_val
	
	lowest = min([reduce(lookup_in_map, maps, seed) for seed in seeds])
	print(f'Lowest Location: {lowest}')


if __name__ == '__main__':
	main()