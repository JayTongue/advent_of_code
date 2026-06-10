from datetime import datetime
from collections import defaultdict

with open('2018/data/4.txt', 'r') as infile:
    shifts = infile.read().splitlines()
shifts.sort(key=lambda x: x[1:17])
shifts = [i.split(' ') for i in shifts]

guard_sleep = defaultdict(list)

for shift in shifts:
    date, time, activity = shift[0][1:], shift[1][:-1], shift[2:]
    year, month, day = date.split('-')
    hour, minute = time.split(':')
    dt = datetime.strptime(f'{year} {month} {day} {hour} {minute}', f'%Y %m %d %H %M')
    if activity[0] == "Guard":
        guard = int(activity[1][1:])
    elif activity[0] == 'falls':
        asleep = dt
    elif activity[0] == 'wakes':
        guard_sleep[guard].append((dt, asleep))

guard_maxes = {}
for guard in guard_sleep:
    times = [0 for _ in range(60)]
    for wake, sleep in guard_sleep[guard]:
        for i in range(sleep.minute, wake.minute):
            times[i] += 1
    guard_maxes[guard] = (max(times), times.index(max(times)))

g = 0 ; g_count = 0 ; g_min = 0
for guard in guard_maxes:
    count, minute = guard_maxes[guard]
    if count > g_count:
        g = guard ; g_min = minute ; g_count = count
print(g * g_min)




