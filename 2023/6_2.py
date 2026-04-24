import re
from math import sqrt
from helpers.timer_func import timer

@timer
def main():
	time, record = (int(re.sub(' ', '', line.split(':')[1])) for line in open('data/6.txt', 'r').read().split('\n'))

	upper = int((-(time) + sqrt(time**2 - (4*record)))/2)
	lower = int((-(time) - sqrt(time**2 - (4*record)))/2)

	print(f'Total Record Breakers: {upper-lower}')

if __name__ == '__main__':
	main()