with open('2016/data/18.txt', 'r') as infile:
    maze = [[False if i == '.' else True for i in list(infile.read())]]

def next_row(old_row):
    new_row = [is_trap(i, old_row) for i in range(len(old_row))]
    return new_row

def is_trap(i, row):
    aboves = [maze[-1][j] if 0<=j<=len(row)-1 else False for j in range(i-1, i+2) ]
    if aboves in [[True, True, False], 
                  [False, True, True], 
                  [True, False, False], 
                  [False, False, True]]:
        return True
    return False

while len(maze) < 40:
    new_row = next_row(maze[-1])
    maze.append(new_row)

print((len(maze[0]) * len(maze)) - sum([sum(i) for i in maze]))


