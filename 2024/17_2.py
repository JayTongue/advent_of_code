import re
import tqdm
import copy


def main():
    infile = open('data/17.txt', 'r').read()
    registers, program = infile.split('\n\n')
    reg_a, reg_b, reg_c = re.findall(r'\d+', registers)
    reg_a, reg_b, reg_c = int(reg_a), int(reg_b), int(reg_c)
    program = program.split()[1].split(',')
    program = [int(numb) for numb in program]

    for test_reg_a in tqdm.tqdm(range(1000000000)):
        reg_a = copy.deepcopy(test_reg_a)
        outputs = []
        pointer = 0
        while pointer < len(program):
            opcode, in_val = program[pointer], program[pointer + 1]
            if opcode == 0:
                reg_a, reg_b, reg_c = opcode_0(in_val, reg_a, reg_b, reg_c)
            elif opcode == 1:
                reg_a, reg_b = opcode_1(in_val, reg_a, reg_b)
            elif opcode == 2:
                reg_a, reg_b, reg_c = opcode_2(in_val, reg_a, reg_b, reg_c)
            elif opcode == 3:
                reg_a, pointer = opcode_3(in_val, reg_a, pointer)
            elif opcode == 4:
                reg_a, reg_b, reg_c = opcode_4(in_val, reg_a, reg_b, reg_c)
            elif opcode == 5:
                out_val, reg_a, reg_b, reg_c = opcode_5(in_val, reg_a, reg_b, reg_c)
                outputs.append(out_val)
            elif opcode == 6:
                reg_a, reg_b, reg_c = opcode_6(in_val, reg_a, reg_b, reg_c)
            elif opcode == 7:
                reg_a, reg_b, reg_c = opcode_7(in_val, reg_a, reg_b, reg_c)

            if opcode != 3:
                pointer += 2

        outputs = [int(i) for i in outputs]
        if outputs == program:
            print(f'Solution Found: {test_reg_a}')
            break
        


def combo_picker(in_val, reg_a, reg_b, reg_c):
    if 0 <= in_val <= 3:
        return in_val
    if in_val == 4:
        return reg_a
    if in_val == 5:
        return reg_b
    if in_val == 6:
        return reg_c
    if in_val == 7:
        raise ValueError("Invalid program input.")


def opcode_0(in_val, reg_a, reg_b, reg_c):
    combo = combo_picker(in_val, reg_a, reg_b, reg_c)
    reg_a = int(reg_a / (2 ** combo))
    return reg_a, reg_b, reg_c

    
def opcode_1(in_val, reg_a, reg_b):
    reg_b = in_val ^ reg_b
    return reg_a, reg_b


def opcode_2(in_val, reg_a, reg_b, reg_c):
    combo = combo_picker(in_val, reg_a, reg_b, reg_c)
    reg_b = combo % 8
    return reg_a, reg_b, reg_c


def opcode_3(in_val, reg_a, pointer):
    if reg_a == 0:
        pointer += 2
        return reg_a, pointer
    else:
        pointer = in_val
        return reg_a, pointer

def opcode_4(in_val, reg_a, reg_b, reg_c):
    reg_b = reg_b ^ reg_c
    return reg_a, reg_b, reg_c


def opcode_5(in_val, reg_a, reg_b, reg_c):
    combo = combo_picker(in_val, reg_a, reg_b, reg_c)
    out_val = str(combo % 8)
    return out_val, reg_a, reg_b, reg_c


def opcode_6(in_val, reg_a, reg_b, reg_c):
    combo = combo_picker(in_val, reg_a, reg_b, reg_c)
    reg_b = int(reg_a / (2 ** combo))
    return reg_a, reg_b, reg_c

def opcode_7(in_val, reg_a, reg_b, reg_c):
    combo = combo_picker(in_val, reg_a, reg_b, reg_c)
    reg_c = int(reg_a / (2 ** combo))
    return reg_a, reg_b, reg_c


if __name__ == '__main__':
    main()

