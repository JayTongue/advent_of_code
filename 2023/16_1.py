from collections import deque
from helpers.timer_func import timer

@timer
def main():
	with open('data/16.txt', 'r') as data:
		data = [list(line) for line in data.read().split('\n')]

	walked = walk(data, (0, -1, 0, 1))
	print(walked)

def walk(data, start):
    queue, seen = deque([start]), set()
    while queue:
        row, col, row_change, col_change = queue.popleft()
        new_row = row + row_change
        new_col = col + col_change

        if not (0 <= new_row < len(data) and 0 <= new_col < len(data[0])):
            continue  # Skip if out of bounds
        new_position = data[new_row][new_col]
        if (
            new_position == "."
            or (new_position == "-" and row_change == 0)
            or (new_position == "|" and col_change == 0)
        ):
            if (new_row, new_col, row_change, col_change) not in seen:
                queue.append((new_row, new_col, row_change, col_change))
                seen.add((new_row, new_col, row_change, col_change))
        elif new_position == "\\":
            row_change, col_change = col_change, row_change
            if (new_row, new_col, row_change, col_change) not in seen:
                queue.append((new_row, new_col, row_change, col_change))
                seen.add((new_row, new_col, row_change, col_change))
        elif new_position == "/":
            row_change, col_change = -col_change, -row_change
            if (new_row, new_col, row_change, col_change) not in seen:
                queue.append((new_row, new_col, row_change, col_change))
                seen.add((new_row, new_col, row_change, col_change))
        else:
            if new_position == "|":
                for dr, dc in [(1, 0), (-1, 0)]:
                    if (new_row, new_col, dr, dc) not in seen:
                        queue.append((new_row, new_col, dr, dc))
                        seen.add((new_row, new_col, dr, dc))
            elif new_position == "-":
                for dr, dc in [(0, 1), (0, -1)]:
                    if (new_row, new_col, dr, dc) not in seen:
                        queue.append((new_row, new_col, dr, dc))
                        seen.add((new_row, new_col, dr, dc))

    visited = {(coords[0], coords[1]) for coords in seen} 
    return len(visited)

		
if __name__ == '__main__':
	main()