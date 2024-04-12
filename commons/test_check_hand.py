from gen_random_card import gen_random_card
from check_hand import check_hand

hand = []
for _ in range(5):
    card = gen_random_card()
    while hand.count(card) != 0:
        card = gen_random_card()
    hand.append(card)
bet, cards_to_swap = check_hand(hand, 1)
new_cards = []
for card in cards_to_swap:
    new_card = gen_random_card()
    while new_card in hand or new_card in new_cards:
        new_card = gen_random_card()
    new_cards.append(new_card)
new_hand = []
for card in hand:
    if card in cards_to_swap:
        new_hand.append(new_cards.pop())
    else:
        new_hand.append(card)
bet, cards_to_swap = check_hand(new_hand, 2)