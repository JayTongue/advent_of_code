from collections import Counter
from helpers.timer_func import timer

@timer
def main():
	data = [(hand, int(bid)) for hand, bid in (cards.split(' ') for cards in open('data/7.txt', 'r').read().split('\n'))]
	fives, fours, fulls, threes, twos, ones, high = sort_hands(data)
	big_list = rank(fives, fours, fulls, threes, twos, ones, high)
	total_winnings = 0
	for count, bid in enumerate(big_list):
		total_winnings += (count + 1) * bid
	print(f'Total Winnings: {total_winnings}')


def rank(fives, fours, fulls, threes, twos, ones, high):
	rank_dict = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
	big_list = []
	for hand_type in (fives, fours, fulls, threes, twos, ones, high):
		translated = [([rank_dict[card] for card in hand[0]], hand[1])for hand in hand_type]
		translated = sorted(translated, key=lambda x: x[0], reverse=True)
		for play in translated:
			big_list.append(play[1])
	big_list = reversed(big_list)
	return big_list
			

def sort_hands(data):
	fives, fours, fulls, threes, twos, ones, high = set(), set(), set(), set(), set(), set(), set()
	for cards, bid in data:
		hand = Counter(cards)
		hand = sorted(hand.values(), reverse=True)
		if 5 in hand:
			fives.add((cards, bid))
		elif 4 in hand:
			fours.add((cards, bid))
		elif 3 in hand:
			if 2 in hand:
				fulls.add((cards, bid))
			else:
				threes.add((cards, bid))
		elif hand.count(2) == 2:
			twos.add((cards, bid))
		elif hand.count(2) == 1:
			ones.add((cards, bid))		
		else:
			high.add((cards, bid))
	return fives, fours, fulls, threes, twos, ones, high


if __name__ == '__main__':
	main()