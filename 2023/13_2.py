import copy
from helpers.timer_func import timer

@timer
def main():
	with open('data/13.txt', 'r') as data:
		data = [[list(line) for line in board.split('\n')] for board in data.read().split('\n\n')]

	total = 0

	for board in data:
		old_vert, old_horiz = find_verts(board), find_horis(board)
		found = False
		for row_count, row in enumerate(board):
			for item_count, _ in enumerate(row):
				bizaro_board = copy.deepcopy(board)
				bizaro_board[row_count][item_count] = '#' if bizaro_board[row_count][item_count] == '.' else '.'
				horiz, vert = find_horis(bizaro_board), find_verts(bizaro_board)

				for choice, old_choice in zip([horiz, vert], [old_horiz, old_vert]):
					for value in choice:
						if value and value != next(iter(old_choice), 0):
							total += value
							found = True
							break
					if found:
						break
				if found:
					break
			if found:
				break

	print(f'Total: {total}')		

def find_verts(board):
    verts = set()
    row_len = len(board[0]) 
    for i in range(1, row_len):
        match = True
        for row in board:
            before, after = row[:i][::-1], row[i:]
            if not (before[:len(after)] == after or after[:len(before)] == before):
                match = False
                break
        if match:
            verts.add(i)
    return verts


def find_horis(board):
	horizs = set()
	for i in range(1, len(board)):
		match = True
		before, after = board[:i][::-1], board[i:]
		if not (before[:len(after)] == after or after[:len(before)] == before):
			match = False
		if match:
			horizs.add(i * 100)
	return horizs

if __name__ == "__main__":
	main()