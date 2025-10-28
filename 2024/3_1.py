import re


def main():
    infile = open('data/3.txt', 'r', encoding='utf-8')

    
    all_matches = []
    for line in infile:
        matches = match_pattern(line)
        all_matches += matches
    
    total = make_multiples(all_matches)
    print(total)
    

def match_pattern(line):
    pattern = r'mul\(\d+?,\d+?\)'
    matches = re.findall(pattern, line)
    return matches
        

def make_multiples(all_matches):

    total = 0
    for match in all_matches:
        number_1 = int(re.findall(r'\(\d+?,', match)[0][1:-1])
        number_2 = int(re.findall(r',\d+?\)', match)[0][1:-1])
        total += (number_1 * number_2)
    
    return total




if __name__ == '__main__':
    main()