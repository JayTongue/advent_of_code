from functools import cache
from helpers.timer_func import timer

@timer
def main():
	with open('data/12.txt', 'r') as f:
		data = []
		for line in f.readlines():
			row, nums = line.split()
			nums = tuple(int(num) for num in nums.split(','))
			data.append((row, nums))
	print('Total: ', sum(springs_finder(r + '.', n) for r, n in data))

@cache
def springs_finder(row, nums):
	next_part = nums[1:]
	springs = (f"{'.'*spr}{'#'*nums[0]}." for spr in range(len(row) - sum(nums) - len(next_part)))
	valid = (len(spr) for spr in springs if all(r in (c, '?') for r, c in zip(row, spr)))
	
	return sum(springs_finder(row[v:], next_part) for v in valid) if next_part else sum('#' not in row[v:] for v in valid)

if __name__ == '__main__':
	main()