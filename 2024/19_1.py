import re
from collections import deque
import tqdm
from multiprocessing import Pool, cpu_count


def main():
    infile = open('data/19.txt', 'r').read()
    towels, combos = infile.split('\n\n')
    towels = towels.split(', ')
    combos = combos.split('\n')

    num_workers = cpu_count()

    with Pool(num_workers) as pool:
        possible_count = sum(pool.map(check_combo, [(towels, combo) for combo in combos]))

    print(f'Out of {len(combos)}, {possible_count} are possible.')


def check_combo(args):
    towels, combo = args
    return find_possibles(towels, combo)


def find_possibles(towels, combo):
    queue = deque([("", [])])  # (string, words used)

    small_towels = [i for i in towels if re.findall(i, combo)]
    # print(len(small_towels))

    while queue:
        current_str, used_words = queue.popleft()

        if current_str == combo:
            return True  # If solution

        for towel in small_towels:
            new_str = current_str + towel
            if len(new_str) <= len(combo) and combo.startswith(new_str):
                queue.append((new_str, used_words + [combo]))

    return False  # If no solution


if __name__ == '__main__':
    main()
