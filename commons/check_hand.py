def parse_card(card: str) -> int:
    if card[0] == 'T':
        return 10
    elif card[0] == 'J':
        return 11
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    elif card[0] == 'A':
        return 14
    else:
        return int(card[0])

def parse_hand(hand: list[str]) -> list[int]:
    parsed_hand = []
    for card in hand:
        parsed_hand.append(parse_card(card))
    return parsed_hand

def unparse_card(card: int) -> str:
    if card == 10:
        return 'T'
    elif card == 11:
        return 'J'
    elif card == 12:
        return 'Q'
    elif card == 13:
        return 'K'
    elif card == 14:
        return 'A'
    else:
        return str(card)

def check_hand(hand: list[str], round: int):
    parsed_hand = parse_hand(hand)
    parsed_hand.sort()

    is_straight = True
    for i in range(1, len(parsed_hand)):
        if parsed_hand[i] != parsed_hand[i - 1] + 1:
            is_straight = False

    is_flush = True
    for i in range(1, len(hand)):
        if hand[i][1] != hand[i - 1][1]:
            is_flush = False

    is_four_of_a_kind = False
    is_three_of_a_kind = False
    is_pair = False
    for i in range(len(parsed_hand)):
        if parsed_hand.count(parsed_hand[i]) == 3:
            is_three_of_a_kind = True
        elif parsed_hand.count(parsed_hand[i]) == 2:
            is_pair = True
        elif parsed_hand.count(parsed_hand[i]) == 4:
            is_four_of_a_kind = True

    is_two_pair = False
    if is_pair:
        is_two_pair = len(set(parsed_hand)) == 3

    print(f'Round {round}:')
    print(f'Hand: {hand}')
    bet = 0
    cards_to_swap = []
    if is_straight and is_flush and parsed_hand[0] == 10:
        print('Royal Flush')
        bet = 200
    elif is_straight and is_flush:
        print('Straight Flush')
        bet = 200
    elif is_four_of_a_kind:
        print('Four of a Kind')
        bet = 200
        for card in hand:
            if parsed_hand.count(parsed_hand[parsed_hand.index(parse_card(card))]) != 4:
                cards_to_swap.append(card)
    elif is_three_of_a_kind and is_pair:
        print('Full House')
        bet = 200
    elif is_flush:
        print('Flush')
        bet = 200
    elif is_straight:
        print('Straight')
        bet = 200
    elif is_three_of_a_kind:
        trios = []
        for card in hand:
            if parsed_hand.count(parsed_hand[parsed_hand.index(parse_card(card))]) == 3:
                trios.append(card)
            else:
                cards_to_swap.append(card)
        print(f'Three of a Kind: {trios[0]}{trios[1]}{trios[2]}')
        if (round == 1):
            bet = 200
        else:
            bet = 180
    elif is_two_pair:
        if (round == 1):
            bet = 150
        else:
            bet = 100
        pairs = []
        for card in hand:
            if parsed_hand.count(parsed_hand[parsed_hand.index(parse_card(card))]) == 2:
                pairs.append(card)
            else:
                cards_to_swap.append(card)
        sorted_pairs = pairs.copy()
        sorted_pairs.sort()
        print(f'Two Pair: {sorted_pairs[0]}{sorted_pairs[1]} - {sorted_pairs[2]}{sorted_pairs[3]}')


    elif is_pair:
        pairs = []
        for card in hand:
            if parsed_hand.count(parsed_hand[parsed_hand.index(parse_card(card))]) == 2:
                pairs.append(card)
            else:
                cards_to_swap.append(card)
        print(f'Pair: {pairs[0]}{pairs[1]}')
        if (round == 1):
            bet = parse_card(pairs[0]) * 7 + 1
        else:
            if parse_card(pairs[0]) > 10:
                bet = parse_card(pairs[0]) * 2
            else:
                bet = 5

    else:
        high_card_parsed = parsed_hand[-1]
        high_card = None
        for card in hand:
            if card[0] == unparse_card(high_card_parsed):
                high_card = card

        print(f'High Card: {high_card}')
        if (round == 1):
            bet = high_card_parsed if high_card_parsed > 10 else 5
        else:
            bet = 0
        if (round == 1):
            cards_to_swap = hand.copy()
            if high_card_parsed > 10:
                cards_to_swap.remove(high_card)


    print(f'Bet: {bet}')
    if (round == 1):
        print(f'Cards to swap: {cards_to_swap}')
    return bet, cards_to_swap

