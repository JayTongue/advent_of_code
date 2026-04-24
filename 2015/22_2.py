from heapq import heappush, heappop

def solve(boss_hp, boss_dmg, hard_mode=False):
    # State: (mana_spent, player_hp, player_mana, boss_hp, shield_turns, poison_turns, recharge_turns, is_player_turn)
    start = (0, 50, 500, boss_hp, 0, 0, 0, True)
    heap = [start]
    visited = set()
    
    while heap:
        state = heappop(heap)
        mana_spent, php, pmana, bhp, shield, poison, recharge, player_turn = state
        
        # Create state key (without mana_spent for visited check)
        state_key = (php, pmana, bhp, shield, poison, recharge, player_turn)
        if state_key in visited:
            continue
        visited.add(state_key)
        
        # Hard mode: lose 1 HP at start of player turn
        if hard_mode and player_turn:
            php -= 1
            if php <= 0:
                continue
        
        # Apply effects
        armor = 7 if shield > 0 else 0
        if poison > 0:
            bhp -= 3
        if recharge > 0:
            pmana += 101
        
        # Decrement timers
        shield = max(0, shield - 1)
        poison = max(0, poison - 1)
        recharge = max(0, recharge - 1)
        
        if bhp <= 0:
            return mana_spent
        
        if player_turn:
            # Try each spell
            for spell, cost in [('missile', 53), ('drain', 73), ('shield', 113), 
                                ('poison', 173), ('recharge', 229)]:
                if pmana < cost:
                    continue
                
                new_php, new_pmana, new_bhp = php, pmana - cost, bhp
                new_shield, new_poison, new_recharge = shield, poison, recharge
                
                if spell == 'missile':
                    new_bhp -= 4
                elif spell == 'drain':
                    new_php += 2
                    new_bhp -= 2
                elif spell == 'shield':
                    if shield > 0:
                        continue  # Can't cast if active
                    new_shield = 6
                elif spell == 'poison':
                    if poison > 0:
                        continue
                    new_poison = 6
                elif spell == 'recharge':
                    if recharge > 0:
                        continue
                    new_recharge = 5
                
                new_state = (mana_spent + cost, new_php, new_pmana, new_bhp, 
                            new_shield, new_poison, new_recharge, False)
                heappush(heap, new_state)
        else:
            # Boss turn
            damage = max(1, boss_dmg - armor)
            new_php = php - damage
            if new_php > 0:
                new_state = (mana_spent, new_php, pmana, bhp, 
                            shield, poison, recharge, True)
                heappush(heap, new_state)
    
    return float('inf')

# Read input and solve
with open('2015/data/22.txt', 'r') as f:
    boss_hp, boss_dmg = [int(i.split(': ')[1]) for i in f.read().strip().split('\n')]

print("Part 1:", solve(boss_hp, boss_dmg, False))
print("Part 2:", solve(boss_hp, boss_dmg, True))