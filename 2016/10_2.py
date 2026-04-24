from collections import defaultdict
from math import prod
import re

with open('2016/data/10.txt', 'r') as infile:
    data = infile.read().split('\n')

bots = defaultdict(set) ; out_dict = defaultdict(set)
starts = [i for i in data if re.search(r"value", i)]
outputs = [i for i in data if re.search(r'output', i)]
trades = [i for i in data if re.search(r'gives', i) and not re.search(r'output', i)]

for start in starts:
    val, bot = tuple(map(int, re.findall(r'\d+', start)))
    bots[bot].add(val)

def find_trades(trades, bots):
    while trades:
        for trade in trades:
            bot, low, high = tuple(map(int, re.findall(r'\d+', trade)))
            if len(bots[bot]) == 2:
                bots[low].add(min(bots[bot])) ; bots[high].add(max(bots[bot]))
                bots[bot] = set()
                trades.remove(trade)
        print('trade_pool:', len(trades))
    return bots


def find_outputs(outputs, bots):
    while outputs:
        for output in outputs:
            bot, out, high = tuple(map(int, re.findall(r'\d+', output)))
            if len(bots[bot]) == 2:
                out_dict[out].add(min(bots[bot])) ; bots[high].add(max(bots[bot]))
                bots[bot] = set()
                outputs.remove(output)
    return prod(map(sum, (out_dict[0], out_dict[1], out_dict[2])))
    
print(find_outputs(outputs, find_trades(trades, bots)))