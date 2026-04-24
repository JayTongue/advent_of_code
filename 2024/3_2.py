import re


def main():
    infile = open('data/3.txt', 'r', encoding='utf-8')

    
    all_matches = []
    for line in infile:
        matches = match_pattern(line)
        all_matches += matches
    
    total = 0

    do = True
    for instruction in all_matches:
        if instruction[0]:
            multiple = multiply(instruction[0])
            if do:
                total += multiple
        elif instruction[1]:
            do = True
        elif instruction[2]:
            do = False
    print(total)
    

def match_pattern(line):
    pattern = r'(mul\(\d+?,\d+?\))|(do\(\))|(don\'t\(\))'
    matches = re.findall(pattern, line)
    return matches
        

def multiply(match):

    total = 0
    number_1 = int(re.findall(r'\(\d+?,', match)[0][1:-1])
    number_2 = int(re.findall(r',\d+?\)', match)[0][1:-1])
    total += (number_1 * number_2)
    
    return total




if __name__ == '__main__':
    main()