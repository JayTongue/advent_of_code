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
	bad_edit_sums = 0
	
	for edit in edits:
		good_edit = True
		good_edit = find_good_edits(good_edit, edit, orders)
		if good_edit:
			good_edit_sums += int(edit[int(len(edit)/2)])
		else:
			fix_bad_edits(edit, orders)
			
	print(f'Good Edits: {good_edit_sums}')


class Node:
	def __init__(self, page):
		self.page = page
		self.next = None
		self.befores = set()
		self.afters = set()
		
	def print_attr(self):
		print(f'''---- Page: {self.page} ----
	  Next: {self.next}
	  Befores: {self.befores}
	  Afters: {self.afters}\n''')
			
	def add_befores(self, before: int):
		self.befores.add(before)
			
	def add_afters(self, after: int):
		self.afters.add(after)
		
	def shuffle_up(self, pages: list):
		current_index = pages.index(self)
		pages.pop(current_index)
		pages.insert(current_index - 1, self)
		return pages
		
	def vibe_check(self, pages: list):
		vibe_check = True
		current_index = pages.index(self)
		
		for before in pages[:current_index]:
			if before.page in self.afters:
				vibe_check = False
		for after in pages[current_index:]:
			if after.page in self.befores:
				vibe_check = False

		print('Vibe Check: ', vibe_check)
		
		return vibe_check
		
		
def fix_bad_edits(edit, orders):
	pages = []
	for page in edit:
		page_obj = Node(page)
		pages.append(page_obj)
	
	for LL_page in pages:
		for order in orders:
			if order[0] == LL_page.page:
				LL_page.add_afters(order[1])
			if order[1] == LL_page.page:
				LL_page.add_befores(order[0])
		#LL_page.print_attr()
		#vibe_check = LL_page.vibe_check(pages)
	new_order = []
	for LL_page in pages:
		new_order.append(LL_page)
		for test_page in new_order:
			vibe_check = test_page.vibe_check(pages)
			while not vibe_check:
				new_order = new_order.shuffle_up(test_page)
				vibe_check = test_page.vibe_check(new_order)
	print(new_order)
				
	
			
def find_good_edits(good_edit, edit, orders):
	for before_page in edit:
		relevant_orders = [order for order in orders if ((order[0] == before_page) or (order[1] == before_page))]
		#print(relevant_orders)
		for relevant_order in relevant_orders:
			if (relevant_order[0] in edit) and (relevant_order[1] in edit):
				before_index = edit.index(relevant_order[0])
				after_index = edit.index(relevant_order[1])
					
				if not before_index < after_index:
					good_edit = False
		
	return good_edit
		

if __name__ == '__main__':
	main()