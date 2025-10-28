import itertools


def main():
	data = open('data/7.txt', 'r')
	all_data = parse_data(data)
	all_total = check_validity(all_data)
	print(f'\nFinal Sum: {all_total}')


def parse_data(data):
	all_data = []
	for line in data:
		line = line.strip()
		line = line.split(': ')
		line[1] = line[1].split(' ')
		all_data.append(line)
	return all_data
	
	
def check_validity(all_data):
	all_total = 0
	
	add = lambda x, y: x + y
	mult = lambda x, y: x * y
	conc = lambda x, y: int(str(x) + str(y))
	def operate(operator, x, y):
		return operator(x, y)
			
	for line in all_data:
		print(line)
		answer, problem = int(line[0]), line[1]
		num_count = len(problem) # It looks like this will always be at least 2
		
		correct = False
		
		operations = [add, mult, conc]
		operators_list = list(itertools.product(operations, repeat=len(problem)-1))
		
		for operator_combinations in operators_list:
			total = int(problem[0])
			for count, problem_num in enumerate(problem[1:]):
				operator = operator_combinations[count]
				total = operate(operator, total, int(problem_num))
			if total == answer:
				all_total += answer
				break
	return all_total		



if __name__ == '__main__':
	main()