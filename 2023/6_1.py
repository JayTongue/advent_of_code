from helpers.timer_func import timer

@timer
def main():
	times, distances = ([int(i) for i in line.split(' ')[1:] if i] for line in open('data/6.txt', 'r').read().split('\n'))
	records = dict(zip(times, distances))

	total_breakers = 1
	for time in records:
		record_breakers = 0
		for hold_time in range(time):
			run_time = time - hold_time
			dist = hold_time * run_time
			if dist > records[time]:
				record_breakers += 1
		total_breakers *= record_breakers
	
	print(f'Total Record Breakers: {total_breakers}')

if __name__ == '__main__':
	main()