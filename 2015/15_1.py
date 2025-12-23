import numpy as np
from scipy.optimize import minimize

with open('./2015/data/15.txt', 'r') as infile:
    data = {i.split(':')[0]:i.split(':')[1][1:].split(', ') for i in infile.read().split('\n')}
    matrix = []
    for d in data:
        data[d] = [int(i.split(' ')[1]) for i in data[d][:-1]]
        matrix.append(data[d])
    matrix = np.array(matrix).T


def optimize_weights(matrix, total=100):
    n_cols = matrix.shape[1]
    def objective(w):
        row_sums = np.sum(matrix * w, axis=1)
        if np.any(row_sums <= 0):
            return 1e10
        return -np.sum(np.log(row_sums))
    
    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - total}
    bounds = [(0, None)] * n_cols
    w0 = np.ones(n_cols) * (total / n_cols)
    result = minimize(objective, w0, method='SLSQP', bounds=bounds, constraints=constraints)
    continuous_weights = result.x
    rounded_weights = smart_round(continuous_weights, total)
    final_weights = local_search(matrix, rounded_weights, total)
    row_sums = np.sum(matrix * final_weights, axis=1)
    product = np.prod(row_sums)
    
    return final_weights, product


def smart_round(weights, total):
    rounded = np.round(weights).astype(int)
    diff = total - np.sum(rounded)
    fractional_parts = weights - np.floor(weights)
    
    if diff > 0:
        indices = np.argsort(fractional_parts)[::-1]
        for i in range(diff):
            rounded[indices[i]] += 1
    elif diff < 0:
        indices = np.argsort(fractional_parts)
        for i in range(-diff):
            if rounded[indices[i]] > 0:
                rounded[indices[i]] -= 1
    
    return rounded


def local_search(matrix, weights, total, max_iterations=1000):
    best_weights = weights.copy()
    row_sums = np.sum(matrix * best_weights, axis=1)
    best_product = np.prod(row_sums)
    improved = True ; iteration = 0
    
    while improved and iteration < max_iterations:
        improved = False
        iteration += 1
        for i in range(len(best_weights)):
            if best_weights[i] == 0:
                continue
            for j in range(len(best_weights)):
                if i == j:
                    continue
                test_weights = best_weights.copy()
                test_weights[i] -= 1 ; test_weights[j] += 1
                
                row_sums = np.sum(matrix * test_weights, axis=1)
                product = np.prod(row_sums)
                
                if product > best_product:
                    best_product = product
                    best_weights = test_weights
                    improved = True
                    break
            
            if improved:
                break
    
    return best_weights

weights, product = optimize_weights(matrix, total=100)
print(product)