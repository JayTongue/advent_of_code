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
            spaced.append([int(digit), id_num])
            id_num += 1
            data_block = False
        else:
            if int(digit) > 0:
                spaced.append([int(digit), '.'])
            data_block = True
    return spaced


def move_files(spaced):
    print(spaced)
    sorted_spaced = copy.deepcopy(spaced)
    code_chunks = [count for count, chunk in enumerate(spaced) if isinstance(chunk[1], int)]
    # space_chunks = [count for count, chunk in enumerate(spaced) if chunk[1] == '.']
    
    # print(code_chunks)
    # print(space_chunks)

    for code_chunk in reversed(code_chunks): # code chunk is the index
        space_needed, value = spaced[code_chunk]
        eligible_chunks = [count for count, chunk in enumerate(sorted_spaced) if ((chunk[1] == '.') and (chunk[0] >= space_needed))]
        # print(f'needed: {space_needed}, eligible: {eligible_chunks}')

        if eligible_chunks:
            eligible_chunk = eligible_chunks[0]
            # print(sorted_spaced[eligible_chunk])
            free_space, dot = sorted_spaced[eligible_chunk]
            if free_space == space_needed:
                sorted_spaced[eligible_chunk] = [space_needed, value]
                sorted_spaced[code_chunk] = [space_needed, dot]
            else:
                sorted_spaced[eligible_chunk] = [space_needed, value]
                sorted_spaced[eligible_chunk + 1] = [free_space - space_needed, dot]
                sorted_spaced[code_chunk] = [space_needed, dot]
        sorted_spaced = consolidate(sorted_spaced)
        print(sorted_spaced)
    return sorted_spaced


def consolidate(sorted_spaced):
    # print("Initial list:     ", sorted_spaced)
    
    count = 0
    while count < len(sorted_spaced) - 1:  # Loop until the second-to-last element
        blob = sorted_spaced[count]
        counter = 1
        
        # Check the next item (adjacent)
        if blob[1] == sorted_spaced[count + counter][1]:
            # Merge the adjacent elements
            sorted_spaced[count][0] += sorted_spaced[count + counter][0]
            # Remove the next item
            sorted_spaced.pop(count + counter)
        else:
            count += 1  # Only increment count if no merge occurs
    
    # print("Consolidated list:", sorted_spaced)
    return sorted_spaced


def generate_checksum(sorted_spaced):
    sorted_list = []

    for cluster in sorted_spaced:
        for _ in range(cluster[0]):
            sorted_list.append(cluster[1])

    total_checksum = 0
    for count, block in enumerate(sorted_list):
        if isinstance(block, int):
            total_checksum += (block * count)
        else:
            break
    print(f'Total Checksum: {total_checksum}')


if __name__ == '__main__':
    main()