import itertools

items = {'Weapons': {'Dagger': {'cost':  8, 'damage': 4, 'armor': 0},
'Shortsword': {'cost': 10, 'damage': 5, 'armor': 0},
'Warhammer': {'cost': 25, 'damage': 6, 'armor': 0},
'Longsword': {'cost': 40, 'damage': 7, 'armor': 0},
'Greataxe': {'cost': 74, 'damage': 8, 'armor': 0}},
'Armor': {'Leather':  {'cost':  13, 'damage': 0, 'armor': 1},
'Chainmail':  {'cost':  31, 'damage': 0, 'armor': 2},
'Splintmail':  {'cost':  53, 'damage': 0, 'armor': 3},
'Bandedmail':  {'cost':  75, 'damage': 0, 'armor': 4},
'Platemail':  {'cost': 102, 'damage': 0, 'armor': 5},
'Nothing':  {'cost':  0, 'damage': 0, 'armor': 0}},
'Rings': {'Damage +1':  {'cost':  25, 'damage': 1, 'armor': 0},
'Damage +2':  {'cost':  50, 'damage': 2, 'armor': 0},
'Damage +3':  {'cost': 100, 'damage': 3, 'armor': 0},
'Defense +1':  {'cost':  20, 'damage': 0, 'armor': 1},
'Defense +2':  {'cost':  40, 'damage': 0, 'armor': 2},
'Defense +3':  {'cost':  80, 'damage': 0, 'armor': 3}}}

with open('2015/data/21.txt', 'r') as infile:
    boss_hp, boss_dmg, boss_arm = [int(i.split(': ')[1]) for i in infile.read().split('\n')]

def pk(pk_boss, pk_player):
    while pk_boss['hp'] >= 0 and pk_player['hp'] >= 0:
        pk_boss['hp'] -= max(pk_player['dmg'] - pk_boss['arm'], 1)
        if pk_boss['hp'] <= 0:
            return True
        pk_player['hp'] -= max(pk_boss['dmg'] - pk_player['arm'], 1)
        if pk_player['hp'] <= 0:
            return False

ring_choices = list(itertools.chain.from_iterable(itertools.combinations(items['Rings'].keys(), r) for r in range(0, 3)))

sol = 0
for wep in items['Weapons']:
    for armor in items['Armor']:
        for ring in ring_choices:
            cost = items['Weapons'][wep]['cost'] +   items['Armor'][armor]['cost'] +   sum([items['Rings'][r]['cost'] for r in ring])
            dmg =  items['Weapons'][wep]['damage'] + items['Armor'][armor]['damage'] + sum([items['Rings'][r]['damage'] for r in ring])
            arm =  items['Weapons'][wep]['armor'] +  items['Armor'][armor]['armor'] +  sum([items['Rings'][r]['armor'] for r in ring])

            if not pk({'hp': boss_hp, 'dmg': boss_dmg, 'arm': boss_arm}, {'hp': 100, 'dmg': dmg, 'arm': arm}):
                sol = max(cost, sol)
print(sol)