from helpers.timer_func import timer

@timer
def main():
	data = [list(map(int, line.split(' '))) for line in open('data/9.txt', 'r').read().splitlines()]

	def find_differences(diff_list):
		if not any(diff_list[-1]):
			return diff_list
		else:
			new_diffs = [diff_list[-1][i + 1] - diff_list[-1][i] for i in range(len(diff_list[-1]) - 1)]
			return find_differences(diff_list + [new_diffs])

	history_sum = 0
	for line in data:
		diffs = find_differences([line])
		history_sum += sum([line[-1] for line in diffs])
	print(f'History Sum: {history_sum}')


if __name__ == '__main__':
	main()