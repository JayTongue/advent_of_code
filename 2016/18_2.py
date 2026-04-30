with open('2016/data/18.txt', 'r') as infile:
    old_row = [False if i == '.' else True for i in list(infile.read())]

def next_row(old_row):
    # new_row = [is_trap(i, old_row) for i in range(len(old_row))]
    new_row = list(map(lambda x: is_trap(x, old_row), range(len(old_row))))
    return new_row

def is_trap(i, row):
    aboves = [row[j] if 0<=j<=len(row)-1 else False for j in range(i-1, i+2) ]
    if aboves in [[True, True, False], 
                  [False, True, True], 
                  [True, False, False], 
                  [False, False, True]]:
        return True
    return False

ticker = 1
safes = len(old_row) - sum(old_row)

while ticker < int(4e5):
    new_row = next_row(old_row)
    safes += len(new_row) - sum(new_row)
    old_row = new_row
    ticker += 1

print(safes)