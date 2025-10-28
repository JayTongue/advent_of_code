import re


def main():
	with open('data/5.txt', 'r') as data:
		orders, edits = parse_data(data)
		# print(orders)
		# print(edits)
		verify_instructions(orders, edits)
	

def parse_data(data):
	orders = []
	edits = []
	
	for count, line in enumerate(data):
		line = line.strip()
		if re.findall(r'\|', line):
			before = re.findall(r'\d+\|', line)[0][:-1]
			after = re.findall(r'\|\d+', line)[0][1:]
			orders.append([before, after])
				
		if re.findall(r',', line):
			line = line.split(',')
			edits.append(line)

	return orders, edits
	

def verify_instructions(orders, edits):
	
	good_edit_sums = 0
	
	for edit in edits:
		good_edit = True
		for before_page in edit:
			relevant_orders = [order for order in orders if ((order[0] == before_page) or (order[1] == before_page))]
			#print(relevant_orders)
			for relevant_order in relevant_orders:
				if (relevant_order[0] in edit) and (relevant_order[1] in edit):
					before_index = edit.index(relevant_order[0])
					after_index = edit.index(relevant_order[1])
					
					if not before_index < after_index:
						good_edit = False
		if good_edit:
			good_edit_sums += int(edit[int(len(edit)/2)])
	print(good_edit_sums)
		

if __name__ == '__main__':
	main()