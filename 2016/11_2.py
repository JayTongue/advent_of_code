from collections import deque
from itertools import combinations, product
import json
from copy import deepcopy

with open('2016/data/11.json', 'r') as infile:
    state_dict = json.load(infile)

state_dict = state_dict | {'elg': 1, 'elm': 1, 'dig': 1, 'dim': 1}
hash_order = ['elv', 'com', 'cum', 'rum', 'plm', 'prm', 'elm', 'dim', 'cog', 'cug', 'rug', 'plg', 'prg', 'elg', 'dig']
start_hash = tuple((state_dict[d] for d in hash_order))
end = tuple([4 for _ in hash_order])
seen_states = {start_hash}


def next_states(state_dict, seen_states):
    e_floor = state_dict['elv']
    moveable = [k for k, v in state_dict.items() if v == e_floor and k != 'elv']
    moveable = list(map(list, list(combinations(moveable, 1)) + list(combinations(moveable, 2))))
    floors = (e_floor + 1, e_floor - 1)
    moves = list(product(moveable, floors))
    new_states = []
    for move in moves:
        valid, state_hash = check_valid(move, state_dict, seen_states)
        if valid: 
            new_states.append(state_hash) 
    return new_states

def check_valid(move, state_dict, seen_states):
    if not 1 <= move[1] <= 4:
        return False, ()
    test_state = deepcopy(state_dict)
    test_state = {k: move[1] if k in move[0]+['elv'] else v for k, v in test_state.items()}
    state_hash = tuple((test_state[d] for d in hash_order))
    for checker_position in range(1, 8):
        if state_hash[checker_position] != state_hash[checker_position + 7]:
            if state_hash[checker_position] in state_hash[-7:]:
                return False, ()
    if state_hash in seen_states:
        return False, ()

    return True, state_hash

queue = deque([(start_hash, 0)])
seen_states = {start_hash}
step_counter = 0
while queue:
    state, steps = queue.popleft()
    if steps > step_counter:
        print(steps)
        step_counter = steps

    if state == end:
        print(steps)
        break
    else:
        state_dict = {i:j for i, j in zip(hash_order, state)}
        for next_state in next_states(state_dict, seen_states):
            if next_state not in seen_states:
                seen_states.add(next_state)
                queue.append((next_state, steps +1))
