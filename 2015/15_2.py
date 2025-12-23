import numpy as np
from scipy.optimize import minimize

def optimize_weights_with_constraint(matrix, total=100, target_row=3, target_sum=500):
    """
    Find optimal weights that maximize product of row sums.
    
    Args:
        matrix: numpy array of shape (n_rows, n_cols)
        total: sum constraint for weights (default 100)
        target_row: which row must equal target_sum (0-indexed)
        target_sum: required sum for target_row (default 500)
    
    Returns:
        tuple: (optimal_weights, product_value, target_row_sum)
    """
    n_rows, n_cols = matrix.shape
    print(f"Matrix shape: {n_rows} rows x {n_cols} cols")
    
    # Better initial guess that tries to satisfy the target constraint
    # Solve: matrix[target_row, :] @ w = target_sum, sum(w) = total
    target_row_values = matrix[target_row, :]
    avg_contrib = target_sum / total  # average contribution per unit weight
    
    # Start with weights proportional to 1/target_row_values to hit target
    if np.all(target_row_values > 0):
        w0 = total / target_row_values
        w0 = w0 * (total / np.sum(w0))  # normalize to sum to total
        # Scale to hit target_sum
        current_target = np.sum(target_row_values * w0)
        if current_target > 0:
            w0 = w0 * (target_sum / current_target)
            w0 = w0 * (total / np.sum(w0))  # re-normalize
    else:
        w0 = np.ones(n_cols) * (total / n_cols)
    
    print(f"Initial guess: {w0}")
    print(f"Initial target row sum: {np.sum(matrix[target_row, :] * w0)}")
    print(f"Initial weight sum: {np.sum(w0)}")
    
    # Objective: minimize negative log-sum (to maximize product)
    # BUT exclude the target_row from the product calculation
    def objective(w):
        row_sums = np.sum(matrix * w, axis=1)
        # Exclude target_row from product
        mask = np.ones(len(row_sums), dtype=bool)
        mask[target_row] = False
        relevant_sums = row_sums[mask]
        # Handle edge cases
        if np.any(relevant_sums <= 0):
            return 1e10
        return -np.sum(np.log(relevant_sums))
    
    # Constraints:
    # 1. sum(w) = total
    # 2. row[target_row] sum = target_sum
    constraints = [
        {'type': 'eq', 'fun': lambda w: np.sum(w) - total},
        {'type': 'eq', 'fun': lambda w: np.sum(matrix[target_row, :] * w) - target_sum}
    ]
    
    # Bounds: w_j >= 0
    bounds = [(0, None)] * n_cols
    
    # Solve continuous optimization problem
    result = minimize(objective, w0, method='SLSQP', 
                     bounds=bounds, constraints=constraints,
                     options={'maxiter': 2000, 'ftol': 1e-9})
    
    if not result.success:
        print(f"Warning: optimization may not have converged. Message: {result.message}")
        print(f"Constraint violations: sum={np.sum(result.x) - total}, target={np.sum(matrix[target_row, :] * result.x) - target_sum}")
    
    continuous_weights = result.x
    
    # Round to integers while maintaining BOTH constraints
    rounded_weights = smart_round_dual_constraint(
        continuous_weights, matrix, total, target_row, target_sum
    )
    
    # Local search to improve integer solution
    final_weights = local_search_dual_constraint(
        matrix, rounded_weights, total, target_row, target_sum
    )
    
    # Calculate final product and check constraints
    row_sums = np.sum(matrix * final_weights, axis=1)
    # Product excludes target_row
    mask = np.ones(len(row_sums), dtype=bool)
    mask[target_row] = False
    product = np.prod(row_sums[mask])
    
    print(f"\nContinuous solution: {continuous_weights}")
    print(f"Rounded solution: {rounded_weights}")
    print(f"After local search: {final_weights}")
    print(f"\nRow sums: {row_sums}")
    print(f"Product (excluding row {target_row}): {product}")
    print(f"Target row (row {target_row}) sum: {row_sums[target_row]} (target: {target_sum})")
    print(f"Weight sum: {np.sum(final_weights)} (target: {total})")
    print(f"Product: {product}")
    
    return final_weights, product, row_sums[target_row]


def smart_round_dual_constraint(weights, matrix, total, target_row, target_sum):
    """Round weights to integers while trying to maintain both constraints."""
    n_cols = len(weights)
    target_row_values = matrix[target_row, :]
    
    # Try to find integer solution that satisfies both constraints
    # Use a greedy approach based on fractional parts and constraint impact
    
    rounded = np.floor(weights).astype(int)
    units_to_add = total - np.sum(rounded)
    
    # Calculate how adding 1 unit to each column affects the target row
    target_contributions = target_row_values.copy()
    
    # Greedily add units to columns that help us reach target_sum
    current_target = np.sum(target_row_values * rounded)
    target_deficit = target_sum - current_target
    
    print(f"\nRounding phase:")
    print(f"Need to add {units_to_add} units")
    print(f"Target deficit: {target_deficit} (current: {current_target}, want: {target_sum})")
    
    # Sort columns by their fractional part (for tie-breaking)
    fractional_parts = weights - rounded
    
    for _ in range(units_to_add):
        current_target = np.sum(target_row_values * rounded)
        deficit = target_sum - current_target
        
        # Prefer columns whose contribution gets us closer to target_sum
        # But also consider fractional parts
        scores = np.abs(target_row_values - deficit/units_to_add) * -1 + fractional_parts * 0.1
        
        best_col = np.argmax(scores)
        rounded[best_col] += 1
    
    final_target = np.sum(matrix[target_row, :] * rounded)
    print(f"After rounding - target row sum: {final_target} (want {target_sum}), weight sum: {np.sum(rounded)} (want {total})")
    
    return rounded


def local_search_dual_constraint(matrix, weights, total, target_row, target_sum, 
                                  max_iterations=5000, tolerance=0):
    """
    Improve integer solution through local search while maintaining constraints.
    Product excludes target_row.
    tolerance: how far from target_sum we allow (since integers are discrete)
    """
    best_weights = weights.copy()
    row_sums = np.sum(matrix * best_weights, axis=1)
    # Product excludes target_row
    mask = np.ones(len(row_sums), dtype=bool)
    mask[target_row] = False
    best_product = np.prod(row_sums[mask])
    
    target_row_values = matrix[target_row, :]
    
    print(f"\nStarting local search...")
    print(f"Initial product: {best_product}")
    
    improved = True
    iteration = 0
    improvements = 0
    
    while improved and iteration < max_iterations:
        improved = False
        iteration += 1
        
        # Try all pairs (i, j) where we move 1 unit from i to j
        for i in range(len(best_weights)):
            if best_weights[i] == 0:
                continue
                
            for j in range(len(best_weights)):
                if i == j:
                    continue
                
                # Moving 1 from i to j changes target row by: -target_row_values[i] + target_row_values[j]
                delta = target_row_values[j] - target_row_values[i]
                current_target = np.sum(target_row_values * best_weights)
                new_target = current_target + delta
                
                if abs(new_target - target_sum) > tolerance:
                    continue
                
                # Try the move
                test_weights = best_weights.copy()
                test_weights[i] -= 1
                test_weights[j] += 1
                
                row_sums = np.sum(matrix * test_weights, axis=1)
                # Product excludes target_row
                mask = np.ones(len(row_sums), dtype=bool)
                mask[target_row] = False
                product = np.prod(row_sums[mask])
                
                if product > best_product:
                    best_product = product
                    best_weights = test_weights
                    improved = True
                    improvements += 1
                    break
            
            if improved:
                break
    
    print(f"Local search complete: {improvements} improvements found in {iteration} iterations")
    
    return best_weights


# Example usage with file reading
if __name__ == "__main__":
    # Read and parse the data
    with open('./2015/data/15.txt', 'r') as infile:
        data = {i.split(':')[0]: i.split(':')[1][1:].split(', ') for i in infile.read().strip().split('\n')}
        matrix = []
        ingredient_names = []
        for name in data:
            ingredient_names.append(name)
            data[name] = [int(i.split(' ')[1]) for i in data[name]]
            matrix.append(data[name])
        matrix = np.array(matrix).T  # Transpose so rows are properties, cols are ingredients
    
    print("Ingredients:", ingredient_names)
    print("Matrix (rows=properties, cols=ingredients):")
    print(matrix)
    print(f"Shape: {matrix.shape}")
    print("\n" + "="*60 + "\n")
    
    # Row 4 (index 3) should be calories
    weights, product, target_check = optimize_weights_with_constraint(
        matrix, total=100, target_row=4, target_sum=500  # calories are usually the last row
    )
    
    print("\n" + "="*60)
    print(f"\nFinal weights: {weights}")
    print(f"Ingredient distribution: {dict(zip(ingredient_names, weights))}")
    print(f"Sum check: {np.sum(weights)}")
    print(f"Calorie sum: {target_check} (wanted 500)")
    print(f"Maximum product: {product}")