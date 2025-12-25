import numpy as np
from tqdm import tqdm

with open('./2015/data/15.txt', 'r') as infile:
    data = {i.split(':')[0]:i.split(':')[1][1:].split(', ') for i in infile.read().split('\n')}
    matrix = []
    for d in data:
        data[d] = [int(i.split(' ')[1]) for i in data[d]]
        matrix.append(data[d])
    matrix = np.array(matrix).T

search_space = 100 ; sol = 0
for i in tqdm(range(0, search_space)):
    for j in range(0, search_space-i):
        for k in range(0, search_space -i-j):
            for l in range(0, search_space-i-j-k):
                x_vec = np.array([i, j, l, k]).T
                y_vec = np.sum(matrix[:-1] * x_vec, axis=1)
                if sum(x_vec) == search_space and np.prod(y_vec) > sol:
                    sol = np.prod(y_vec)
print(sol)