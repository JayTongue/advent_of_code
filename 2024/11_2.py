from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import tqdm
import os


def main():
    with open('data/11.txt', 'r') as infile:
        stones = list(map(int, infile.read().split()))

    num_processes = os.cpu_count()
    print(f'Number of cores: {num_processes}')

    for _ in tqdm.tqdm(range(75)):
        stones = blink_parallel(stones, num_processes)

    print(stones)
    print(f'Length of Final Stone Line: {len(stones)}')
    


def blink_parallel(stones, num_processes):
    chunk_size = len(stones) // num_processes
    chunks = [stones[i:i + chunk_size] for i in range(0, len(stones), chunk_size)]
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = executor.map(process_chunk, chunks)
    new_stones = [stone for result in results for stone in result]
    return new_stones

# def blink_parallel(stones, num_threads):
#     chunk_size = len(stones) // num_threads
#     chunks = [stones[i:i + chunk_size] for i in range(0, len(stones), chunk_size)]

#     with ThreadPoolExecutor(max_workers=num_threads) as executor:
#         results = executor.map(process_chunk, chunks)

#     return [stone for result in results for stone in result]


def process_chunk(chunk):
    new_stones = []
    for stone in chunk:
        if stone == 0:
            new_stones.append(1)
        else:
            num_digits = len(str(stone))
            if num_digits % 2 == 0:
                half = 10 ** (num_digits // 2)
                new_stones.append(stone // half)
                new_stones.append(stone % half)
            else:
                new_stones.append(stone * 2024)
    return new_stones


if __name__ == '__main__':
    main()
