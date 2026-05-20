from tqdm import tqdm

a_fac = 16807 ; b_fac = 48271 ; c_fac = 2147483647
a = 65 ; b = 8921
mask = (1 << 16) - 1

def next_iteration(i, fac):
    return (i*fac)%c_fac

sol = 0
for _ in tqdm(range(int(40e6))):    
    a, b = next_iteration(a, a_fac), next_iteration(b, b_fac)
    if (a & mask) == (b & mask):
            sol += 1
print(sol)
    