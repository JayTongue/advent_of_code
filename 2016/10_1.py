from collections import defaultdict
import re

with open('2016/data/10.txt', 'r') as infile:
    data = infile.read().split('\n')

bots = defaultdict(set)
starts = [i for i in data if re.search(r"value", i)]
trades = [i for i in data if re.search(r'gives', i)]

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
                if bots[low] == {17, 61}:
                    return low
                elif bots[high] == {17, 61}:
                    return high 
        print(f'Trade pool: {len(trades)}')
    
print(find_trades(trades, bots))
