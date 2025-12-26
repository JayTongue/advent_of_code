import numpy as np
from tqdm import tqdm

with open('./2015/data/15.txt', 'r') as infile:
    data = {i.split(':')[0]:i.split(':')[1][1:].split(', ') for i in infile.read().split('\n')}
    matrix = []
    for d in data:
        data[d] = [int(i.split(' ')[1]) for i in data[d]]
        matrix.append(data[d])
    matrix = np.array(matrix).T
print(matrix)

search_space = 100 ; sol = 0
for i in tqdm(range(0, search_space+1)):
    for j in range(0, search_space-i+1):
        for k in range(0, search_space -i-j+1):
            for l in range(0, search_space-i-j-k+1):
                x_vec = np.array([i, j, k, l]).T
                y_vec = np.sum(matrix[:-1] * x_vec, axis=1)
                y_vec = np.maximum(y_vec, 0)
                calories = np.sum(matrix[-1] * x_vec)
                if sum(x_vec) == search_space and np.prod(y_vec) > sol and calories == 500:
                    sol = np.prod(y_vec)          

print(sol)
