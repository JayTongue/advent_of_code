import os

""""
This solution technically works, but is VERY resource intensive.
For context, blink 51 was 83gb. 
TODO: A solution that uses memoization is better, and will be explored later.
"""

def main():
    infile = open('data/11/11.txt', 'r')
    stones = infile.read().split(' ')
    stones = [int(stone) for stone in stones]
    infile.close()

    read_file_name = 'data/11/11_read.txt'
    with open(read_file_name, 'w') as read_file:
        for stone in stones:
            read_file.write(f"{stone}\n")

    for blink_count in range(76):
        write_file_name = f'data/11/11_{blink_count}.txt'
        stone_count = 0
        with open(read_file_name, 'r') as read_file, open(write_file_name, 'w') as write_file:
            line = read_file.readline()
            while line:
                stone = int(line.strip())
                blink(stone, write_file)
                stone_count += 1
                line = read_file.readline()

        read_file_name = write_file_name

        filesize_mb = os.path.getsize(write_file_name) / (1024 ^ 3)
        print(f'Blink Number: {blink_count} | Stone Count: {stone_count} | Filesize: {filesize_mb:.2f} GB')

def blink(stone, write_file):
    if stone == 0:
        write_file.write('1\n')
    elif len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        first_stone = str(stone)[:half]
        second_stone = str(stone)[half:]
        write_file.write(f"{first_stone}\n{second_stone}\n")
    else:
        write_file.write(f"{stone * 2024}\n")

if __name__ == '__main__':
    main()
