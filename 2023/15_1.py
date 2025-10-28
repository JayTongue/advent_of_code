from helpers.timer_func	import timer
from functools import reduce

@timer
def main():
	with open('data/15.txt', 'r') as data:
		data = data.read().split(',')

	def hash_datum(datum):
		return reduce(lambda total, char: ((total + ord(char)) * 17) % 256, datum, 0)

	print(sum(map(hash_datum, data)))

if __name__ == '__main__':
	main()