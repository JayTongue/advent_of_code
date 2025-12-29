with open('2015/data/20.txt', 'r') as infile:
    data = int(infile.read())

limit = int(1e6)
gift_counter = [0 for _ in range(limit)]

def calculate_gifts(data):
    for i in range(1, limit+1):
        j = 1
        while i*j < limit:
            gift_counter[i*j] += 10*i
            j += 1
    return gift_counter
        

gift_counter = calculate_gifts(data)
print([i for i in range(len(gift_counter)) if gift_counter[i] > data][0])