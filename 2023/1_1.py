import re
from helpers.timer_func import timer

@timer
def main():
	data = open('data/1.txt', 'r')
	calibration_val = 0
	for line in data:
		digits = re.findall(r'\d', line)
		number = int(''.join(map(str, [digits[0], digits[-1]])))
		calibration_val += number
	print(f'Total Calibration Value: {calibration_val}')

	
	
if __name__ == '__main__':
	main()