from itertools import permutations

with open('2015/data/22.txt', 'r') as infile:
    boss_hp, boss_dmg = [int(i.split(': ')[1]) for i in infile.read().split('\n')]

spells= {'magic_missile': {'mana_cost': 53,  'duration': 1, 'hp': 0, 'atk': 4,  'arm': 0, 'mana': 0},
         'drain':        {'mana_cost': 73,  'duration': 1, 'hp': 2, 'atk': 2,  'arm': 0, 'mana': 0},
         'shield':       {'mana_cost': 113, 'duration': 6, 'hp': 0, 'atk': 0,  'arm': 7, 'mana': 0},
         'poison':       {'mana_cost': 173, 'duration': 6, 'hp': 0, 'atk': 3,  'arm': 0, 'mana': 0},
         'recharge':     {'mana_cost': 229, 'duration': 5, 'hp': 0, 'atk': 0,  'arm': 0, 'mana': 101}}

# moveset = ('recharge', 'shield', 'drain', 'poison', 'magic_missile')
# player_stats = {'hp': 10, 'mana': 250, 'arm': 0, 'counters': {'shield': 0, 'poison': 0, 'recharge': 0}}
# boss_stats = {'hp': 14, 'dmg': 8}

def do_magic(move, player_stats, boss_stats):
    # print('doing: ', move)
    if move == 'magic_missile':
        boss_stats['hp'] -= 4
    elif move == 'drain':
        player_stats['hp'] += 2 ; boss_stats['hp'] -= 2
    elif move == 'shield':
        player_stats['arm'] = 7
    elif move == 'poison':
        boss_stats['hp'] -= 3
    elif move == 'recharge':
        player_stats['mana'] += 101
    return player_stats, boss_stats

def do_counters(player_stats, boss_stats):
    for c in player_stats['counters']:
        if player_stats['counters'][c]:
            player_stats, boss_stats = do_magic(c, player_stats, boss_stats)
            player_stats['counters'][c] -= 1
    if not player_stats['counters']['shield']:
        player_stats['arm'] = 0
    return player_stats, boss_stats

def pk(player_stats, boss_stats, moveset):
    # print(player_stats, boss_stats)
    # print('------------')
        
    for move in moveset: # player goes
        
        player_stats, boss_stats = do_counters(player_stats, boss_stats)

        if move == 'magic_missile':
            player_stats['mana'] -= 53
            player_stats, boss_stats = do_magic(move, player_stats, boss_stats)

        elif move == 'drain':
            player_stats['mana'] -= 73
            player_stats, boss_stats = do_magic(move, player_stats, boss_stats)

        elif move == 'shield':
            player_stats['mana'] -= 113
            player_stats['counters']['shield'] += 6 #6-1, since it already did it once
        elif move == 'poison':
            player_stats['mana'] -= 173
            player_stats['counters']['poison'] += 6
        elif move == 'recharge':
            player_stats['mana'] -= 229
            player_stats['counters']['recharge'] += 5

        # print(move, player_stats, boss_stats)
        if player_stats['hp'] <= 0:
            return 'boss wins'
        elif boss_stats['hp'] <= 0:
            return 'player wins'

        #boss goes
        player_stats, boss_stats = do_counters(player_stats, boss_stats)
        if player_stats['hp'] <= 0:
            return 'boss wins'
        elif boss_stats['hp'] <= 0:
            return 'player wins'
        
        player_stats['hp'] -= max(1, boss_stats['dmg']-player_stats['arm'])
        # print('boss_turn', player_stats, boss_stats)
        if player_stats['hp'] <= 0:
            return 'boss wins'
        elif boss_stats['hp'] <= 0:
            return 'player wins'
        
        # print('------------')
        
    return 'no winner'

# print(pk(player_stats, boss_stats, moveset))

search_space = 4



sol = float('inf')
for j in range(0, search_space +1):
    for perm in permutations(list(spells.keys()) + ['magic_missile', 'drain']*3 , j): 
        mana_outlay = sum([spells[i]['mana_cost'] for i in perm])
        player_stats = {'hp': 50, 'mana': 500, 'arm': 0, 'counters': {'shield': 0, 'poison': 0, 'recharge': 0}}
        boss_stats = {'hp': boss_hp, 'dmg': boss_dmg}
        if pk(player_stats, boss_stats, perm) == 'player wins':
            sol = min((sol, mana_outlay))

print(sol)