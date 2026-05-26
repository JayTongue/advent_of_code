steps = 377
buffer = [0]

add_val = 1 ; idx = 0
while add_val <= 2017:
    new_idx = (idx + steps) % len(buffer) + 1
    buffer.insert(new_idx, add_val)
    idx = new_idx ; add_val += 1
print(buffer[buffer.index(2017)+1])
