from pprint import pprint
import ast

with open('2018/data/16.txt', 'r') as infile:
    caps, _ = infile.read().split('\n\n\n')
caps = [c.split('\n') for c in caps.split('\n\n')]
caps = [(list(ast.literal_eval(c[0][8:])), 
         list(map(int, c[1].split(' '))), 
         list(ast.literal_eval(c[2][8:]))) for c in caps]

def addr(before, A, B, C, after):
    return before[A] + before[B] == after[C]
def addi(before, A, B, C, after):
    return before[A] + B == after[C]
def mulr(before, A, B, C, after):
    return before[A] * before[B] == after[C]
def muli(before, A, B, C, after):
    return before[A] * B == after[C]
def banr(before, A, B, C, after):
    return before[A] & before[B] == after[C]
def bani(before, A, B, C, after):
    return before[A] & B == after[C]
def borr(before, A, B, C, after):
    return before[A] | before[B] == after[C]
def bori(before, A, B, C, after):
    return before[A] | B == after[C]
def setr(before, A, B, C, after):
    return before[A] == after[C]
def seti(before, A, B, C, after):
    return A == after[C]
def gtir(before, A, B, C, after):
    if A > before[B]:
        return after[C] == 1
    return after[C] == 0 
def gtri(before, A, B, C, after):
    if before[A] > B:
        return after[C] == 1
    return after[C] == 0
def gtrr(before, A, B, C, after):
    if before[A] > before[B]:
        return after[C] == 1
    return after[C] == 0
def eqir(before, A, B, C, after):
    if A == before[B]:
        return after[C] == 1
    return after[C] == 0
def eqri(before, A, B, C, after):
    if before[A] == B:
        return after[C] == 1
    return after[C] == 0
def eqrr(before, A, B, C, after):
    if before[A] == before[B]:
        return after[C] == 1
    return after[C] == 0

samp_count = 0
for cap in caps:
    before, op, after = cap
    op, A, B, C = op
    if sum(oper(before, A, B, C, after) for oper in [addr, addi, mulr, muli, 
                                                         banr, bani, borr, bori, 
                                                         setr, seti, gtir, gtri, 
                                                         gtrr, eqir, eqri, eqrr])>=3:
        samp_count += 1
print(samp_count)