from tqdm import tqdm

a_fac = 16807 ; b_fac = 48271 ; c_fac = 2147483647
a_res = 4 ; b_res = 8
a = 634 ; b = 301
mask = (1 << 16) - 1

def next_iteration(i, fac, res):
    while True:
        val = (i*fac)%c_fac
        if val % res == 0:
            return val
        i = val

sol = 0
for _ in tqdm(range(int(5e6))):    
    a, b = next_iteration(a, a_fac, a_res), next_iteration(b, b_fac, b_res)
    if (a & mask) == (b & mask):
            sol += 1
print(sol)
    
