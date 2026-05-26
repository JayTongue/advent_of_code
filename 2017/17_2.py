steps = 377
buffer = 1

add_val = 1; idx = 0 ; sol = 0
while add_val <= int(5e7):
    new_idx = (idx + steps) % buffer + 1
    if new_idx == 1:
        sol = add_val
    buffer += 1
    idx = new_idx ; add_val += 1
print(sol)
