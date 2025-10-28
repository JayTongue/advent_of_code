import re
import tqdm
import math


def main():
    infile = open('data/13.txt', 'r').read()
    infile = infile.split('\n\n')

    total_cost = 0

    for machine in tqdm.tqdm(infile):
        machine = machine.split('\n')
        but_a, but_b, prize = machine
        but_a = convert_buttons_to_dict(but_a)
        but_b = convert_buttons_to_dict(but_b)
        prize = convert_buttons_to_dict(prize)
        machine = {'p': prize, 'a': but_a, 'b': but_b}
        # print(machine)
        cost = find_possibles(machine)
        
        total_cost += cost
    print(f'Total Cost to play possible games: {total_cost}')


def find_possibles(machine):
    possible_x = find_button_possibles(int(machine['p']['x']), machine['a']['x'], machine['b']['x'])
    possible_y = find_button_possibles(int(machine['p']['y']), machine['a']['y'], machine['b']['y'])
    possibles = [x for x in possible_x if x in possible_y]

    if not possibles:
        cost = 0
    elif len(possibles) == 1:
        cost = calculate_cost(tuple(possibles)[0])
    elif len(possibles) > 1:
        possible_costs = []
        for possible in possibles:
            cost = calculate_cost(possible)
            possible_costs.append(cost)
        cost = possible_costs.index(min(possible_costs))
    # print(cost)
    return cost



def calculate_cost(possibles: tuple):
    # print(possibles)
    a, b = possibles
    return a * 3 + b 


def find_button_possibles(target, a, b):
    possible_matches = []
    gcd, x0, y0 = gcdExtended(a, b)
    
    if target % gcd != 0:
        return possible_matches
    
    x0 *= target // gcd
    y0 *= target // gcd
    
    k_min = int(-x0 * gcd / b)
    k_max = int(y0 * gcd / a)
    
    for k in range(k_min, k_max + 1):
        x = x0 + (b // gcd) * k
        y = y0 - (a // gcd) * k
        
        if x >= 0 and y >= 0:
            possible_matches.append((x, y))
    return possible_matches


def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def convert_buttons_to_dict(button):
    x, y = re.findall(r'\d+', button)
    button = {'x': int(x), 'y': int(y)}
    return button    
        

if __name__ == '__main__':
    main()