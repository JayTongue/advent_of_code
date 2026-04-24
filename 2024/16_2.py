from collections import deque
import heapq

def main():
    with open('data/16.txt', 'r') as infile:
        maze = [list(line.strip()) for line in infile]

    start_coord = find_coord(maze, 'S')
    end_coord = find_coord(maze, 'E')

    maze[start_coord[0]][start_coord[1]] = '.'
    maze[end_coord[0]][end_coord[1]] = '.'

    best_paths, best_score = astar_solve_maze(maze, start_coord, end_coord)

    if best_paths:
        for path in best_paths:
            if path[1][1] != start_coord[1] + 1:
                best_score += 1000

        best_seats = len({item for sublist in best_paths for item in sublist})
        # print(f'Best Paths: {best_paths}')
        print(f'Best Score: {best_score}')
        print(f'Best Seats: {best_seats}')
    else:
        print("No path found.")

def astar_solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    open_set = [(0, start, [start])]
    came_from = {}
    g_score = {start: 0}
    best_score = float('inf')
    best_paths = []

    def heuristic(node):
        x1, y1 = node
        x2, y2 = end
        return abs(x1 - x2) + abs(y1 - y2)

    while open_set:
        _, current, path = heapq.heappop(open_set)

        if current == end:
            if g_score[current] == best_score:
                best_paths.append(path)
            elif g_score[current] < best_score:
                best_score = g_score[current]
                best_paths = [path]
        else:
            for dx, dy in directions:
                neighbor = (current[0] + dx, current[1] + dy)
                tentative_g_score = g_score[current] + calculate_step_cost(path, neighbor)

                if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] == '.':
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score = g_score[neighbor] + heuristic(neighbor)
                        heapq.heappush(open_set, (f_score, neighbor, path + [neighbor]))

    return best_paths, best_score


def calculate_step_cost(path, next_pos):
    if not path:
        return 1

    prev_pos = path[-1]
    dx1, dy1 = next_pos[0] - prev_pos[0], next_pos[1] - prev_pos[1]

    if len(path) > 1:
        prev_prev_pos = path[-2]
        dx2, dy2 = prev_pos[0] - prev_prev_pos[0], prev_pos[1] - prev_prev_pos[1]

        if (dx1, dy1) != (dx2, dy2) and (dx1, dy1) != (-dx2, -dy2): 
            return 1001
    return 1


def find_coord(maze, symbol):
    for x, row in enumerate(maze):
        try:
            y = row.index(symbol)
            return x, y
        except ValueError:
            continue
    return None

if __name__ == '__main__':
    main()