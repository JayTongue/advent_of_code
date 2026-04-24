from helpers.timer_func import timer

@timer
def main():
	with open('data/13.txt', 'r') as data:
		data = [[list(line) for line in board.split('\n')] for board in data.read().split('\n\n')]
	print(f'Total: {sum(map(find_verts, data)) + sum(map(find_horis, data))}')		
	
def find_verts(board):
	for i in range(1, len(board[0])):
		match = True
		for row in board:
			after, before = str(row[i:])[1:-1], str(list(reversed(row[:i])))[1:-1]
			if not (after.startswith(before) or before.startswith(after)):
				match = False
				break
		if match:
			return i
	return 0
	
def find_horis(board):
    for i in range(1, len(board)):
        match = True
        before, after = str(list(reversed(board[:i])))[1:-1], str(board[i:])[1:-1]
        if not (before.startswith(after) or after.startswith(before)):
            match = False
        if match:
            return 100 * i
    return 0

if __name__ == "__main__":
	main()