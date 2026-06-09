with open('2018/data/2.txt', 'r') as infile:
    boxes = [list(i) for i in infile.read().split('\n')]

found = False
for box1 in boxes:
    for box2 in boxes:
        similarity = 0
        for idx in range(len(box1)):
            if box1[idx] == box2[idx]:
                similarity += 1
        if similarity == len(box1)-1:
            found = True
            break
    if found:
        break

print(''.join([b1 for b1 in box1 if b1 in box2]))