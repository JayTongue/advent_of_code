from pprint import pprint
from collections import defaultdict
import ast

with open('2018/data/16.txt', 'r') as infile:
    caps, sequence = infile.read().split('\n\n\n\n')
caps = [c.split('\n') for c in caps.split('\n\n')]
caps = [(list(ast.literal_eval(c[0][8:])), 
         list(map(int, c[1].split(' '))), 
         list(ast.literal_eval(c[2][8:]))) for c in caps]

def addr(before, A, B):
    return before[A] + before[B]
def addi(before, A, B):
    return before[A] + B
def mulr(before, A, B):
    return before[A] * before[B]
def muli(before, A, B):
    return before[A] * B
def banr(before, A, B):
    return before[A] & before[B]
def bani(before, A, B):
    return before[A] & B
def borr(before, A, B):
    return before[A] | before[B]
def bori(before, A, B):
    return before[A] | B
def setr(before, A, B):
    return before[A]
def seti(before, A, B):
    return A
def gtir(before, A, B):
    if A > before[B]:
        return 1
    return 0 
def gtri(before, A, B):
    if before[A] > B:
        return 1
    return 0
def gtrr(before, A, B):
    if before[A] > before[B]:
        return 1
    return 0
def eqir(before, A, B):
    if A == before[B]:
        return 1
    return 0
def eqri(before, A, B):
    if before[A] == B:
        return 1
    return 0
def eqrr(before, A, B):
    if before[A] == before[B]:
        return 1
    return 0

decode = defaultdict(list)
for cap in caps:
    before, op, after = cap
    op_code, A, B, C = op
    could_be = []
    for oper in [addr, addi, mulr, muli, 
                banr, bani, borr, bori, 
                setr, seti, gtir, gtri, 
                gtrr, eqir, eqri, eqrr]:
        if oper(before, A, B) == after[C]:
            could_be.append(oper)
    if op_code in decode:
        decode[op_code] = [c for c in decode[op_code] if c in could_be]
    else:
        decode[op_code] = could_be

discovered = {}
while True:
    if len(decode) == 0:
        break
    else:
        for op_code, possibles in decode.items():
            if len(possibles) == 1:
                locked = possibles[0]
                discovered[op_code] = locked
                new_decode = {}
                for k, v in decode.items():
                    if k != op_code:
                        if locked in v:
                            new_decode[k] = [x for x in v if x != locked]
                        else:
                            new_decode[k] = v
                break
        decode = new_decode
pprint(discovered)

registers = [0, 0, 0, 0]
sequence = [list(map(int, s.split(' '))) for s in sequence.split('\n')]
for operation in sequence:
    op_code, A, B, C = operation
    registers[C] = discovered[op_code](registers, A, B)
print(registers)