with open('2015/data/14.txt', 'r') as infile:
    data = infile.read().split('\n')
    data = {d.split(' ')[0]: map(int, (d.split(' ')[3], d.split(' ')[6], d.split(' ')[13])) for d in data}

seconds = 2503 ; runs = {}
for deer in data:
    run = [0] ; speed, fast, rest = data[deer]
    while len(run) < seconds+1:
        floor = run[-1]
        for i in range(1, fast+1):
            run.append(i * speed + floor)
        for _ in range(rest):
            run.append(run[-1])
    runs[deer] = run
print(max([runs[r][seconds] for r in runs]))