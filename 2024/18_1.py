import heapq
import math


def main():
    infile = open('data/18.txt', 'r')
    data = [line.strip().split(',') for line in infile]
    data = [[int(x), int(y)] for x, y in data]

    map_size = (70, 70)
    data = data[:1024]

    data_map = populate_map(data, map_size)

    solution = solve_maze(data_map, (0, 0), map_size)
    print(solution)


def solve_maze(maze, start, end):
    
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    rows, cols = len(maze), len(maze[0])
    pq = [(0 + heuristic(start, end), 0, start[0], start[1])]  

    g_score = [[float('inf')] * cols for _ in range(rows)]
    g_score[start[0]][start[1]] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        f, g, x, y = heapq.heappop(pq)
        if (x, y) == end:
            return g

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
                tentative_g = g + 1
                if tentative_g < g_score[nx][ny]:
                    g_score[nx][ny] = tentative_g
                    f_score = tentative_g + heuristic((nx, ny), end)
                    heapq.heappush(pq, (f_score, tentative_g, nx, ny))
    return -1


def populate_map(data, map_size):
    map_x, map_y = map_size
    data_map = [['.'] * (map_x+1) for _ in range(map_y+1)]
    for falling_byte in data:
        x, y = falling_byte
        data_map[y][x] = '#'
    return data_map


if __name__ == '__main__':
    main()