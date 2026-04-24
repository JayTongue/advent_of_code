import copy
import time


def main():
    infile = get_infile('9.txt')
    spaced = process_data(infile)
    sorted_list = move_files(spaced)
    generate_checksum(sorted_list)

def get_infile(filename):
    return open(f'data/{filename}', 'r').read()


def process_data(infile):
    spaced = []
    data_block = True
    id_num = 0
    for digit in list(infile):
        if data_block:
            for _ in range(int(digit)):
                spaced.append(id_num)
            id_num += 1
            data_block = False
        else:
            for _ in range(int(digit)):
                spaced.append('.')
            data_block = True
    return spaced


def move_files(spaced):
    sorted_list = copy.deepcopy(spaced)
    blanks = [count for count, blank in enumerate(spaced) if blank == '.'] # list of indexes of blanks
    datum = [count for count, data in enumerate(spaced) if isinstance(data, int)] # list of indexes of data

    for count, data in enumerate(reversed(datum)):
        if data < blanks[count] : # compares the index of the data block to be moved to the corresponding blank space
            break 
        else:
            sorted_list[blanks[count]] = spaced[data] # starts with moving the LAST data into the FIRST space
            sorted_list[data] = '.' # replaces the LAST data with '.'
            # print(''.join([str(j) for j in sorted_list]))
    return sorted_list 


def generate_checksum(sorted_list):
    total_checksum = 0
    for count, block in enumerate(sorted_list):
        if isinstance(block, int):
            total_checksum += (block * count)
        else:
            break
    print(f'Total Checksum: {total_checksum}')


if __name__ == '__main__':
    main()