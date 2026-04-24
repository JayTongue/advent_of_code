import tqdm

def main():
    infile = open('data/11.txt', 'r')
    stones = infile.read().split(' ')
    stones = [int(stone) for stone in stones]
    print(stones)

    

    for _ in tqdm.tqdm(range(75)):
        stones = blink(stones)
    
    print(f'Length of stone line: {len(stones)}')

    
def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            half = int(len(str(stone)) / 2)

            first_stone = list(str(stone))[:half]
            second_stone = list(str(stone))[half:]

            first_stone = int(''.join(map(str, first_stone)))
            second_stone = int(''.join(map(str, second_stone)))

            new_stones.append(first_stone)
            new_stones.append(second_stone)
        else:
            new_stones.append(stone * 2024)
    # print(new_stones)
    return new_stones

if __name__ == '__main__':
    main()