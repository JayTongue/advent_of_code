def main():
    with open('data/17.txt', 'r') as data:
        data = [[int(num) for num in row] for row in data.read().splitlines()]
    print(data)
    visited_coords = set((0,0))
    start_coord = (0,0)
    

if __name__ == '__main__':
    main()