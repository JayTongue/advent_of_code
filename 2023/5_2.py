import re
from helpers.timer_func import timer
from tqdm import tqdm
from functools import reduce

@timer
def main():
	seeds, *maps = open('data/5.txt', 'r').read().split('\n\n')
	seeds = tuple(map(int, seeds.split(' ')[1:]))
	seeds = tuple(zip(seeds[::2], seeds[1::2]))
	maps = [[list(map(int, number.split(' '))) for number in submap.split('\n')[1:]] for submap in maps]
	
	print(f'Minimum Location: {min(reduce(map_seed_io, maps, seeds))[0]}')


def map_seed_io(seeds, submap):
	results = []
	for seed_start, seed_length in seeds:
		while seed_length > 0:
			for map_chunk in submap:
				destination, source, span = map_chunk
				difference = seed_start - source
				if difference in range(span):
					span = min(span-difference, seed_length)
					results.append((destination + difference, span))
					seed_start += span
					seed_length -= span
					break
			else:
				results.append((seed_start, seed_length))
				break
	return results

if __name__ == '__main__':
	main()