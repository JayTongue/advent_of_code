import hashlib
from functools import lru_cache

with open('2016/data/14.txt', 'r') as infile:
    salt = infile.read()

@lru_cache(maxsize=None)
def return_hash(x: str):
    return hashlib.md5(f'{salt}{x}'.encode()).hexdigest()

def check_window(st: str, wind_length: int):
    for idx in range(len(st)-wind_length):
        window = st[idx:idx+wind_length]
        if len(set(list(window))) == 1:
            return set(list(window))
    return False

rolling_int = 0 ; keys = []
while True:
    triple = False
    res = return_hash(rolling_int)
    triple = check_window(res, 3)
    if triple:
        thou_window = [return_hash(rolling_int+i) for i in range(1, 1001)]
        for tho in thou_window:
            if check_window(tho, 5) == triple:
                keys.append(rolling_int)
                break
    rolling_int += 1
    if len(keys) == 63: # why 63??
        break
print(keys[-1])

