import re
from helpers.timer_func import timer

@timer
def main():
	data = open('data/1.txt', 'r')

	replacement_dict = {'one': 'o1e',
					 'two': 't2o',
					 'three': 't3e', 
					 'four': 'f4r',
					 'five': 'f5e',
					 'six': 's6x',
					 'seven': 's7n',
					 'eight': 'e8t',
					 'nine': 'n9e'}
	
	calibration_value = 0
	for line in data:
		line = line.strip()
		for old, new in replacement_dict.items():
			line = line.replace(old, new)
		line = re.sub(r'[A-z]', '', line)
		calibration_value += int(''.join(map(str, (line[0], line[-1]))))
	print(f'Calibration Value: {calibration_value}')




if __name__ == '__main__':
	main()