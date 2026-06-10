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
    guard_maxes[guard] = times.index(max(times))

longest = 0 ; longest_window = 0
for guard in guard_sleep:
    total_sleep = (sum([int((stop-start).total_seconds()//60) for stop, start in guard_sleep[guard]]))
    if total_sleep > longest_window:
        longest = guard ; longest_window = total_sleep

print(longest * guard_maxes[longest])




