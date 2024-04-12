from sqlalchemy.orm import Session
from domain.schemas.match import FirstRoundReceive, FirstRoundResponse, SecondRoundReceive, SecondRoundResponse, ResultReceive
from repositories import match as match_repository
from commons.check_hand import check_hand


def first_round(db: Session, data: FirstRoundReceive):
    bet, cards_to_swap = check_hand(data.cards, 1)
    match_repository.post_match(db, data, bet, cards_to_swap)
    return FirstRoundResponse(bet=bet, cardsToSwap=cards_to_swap)

def second_round(db: Session, data: SecondRoundReceive):
    match = match_repository.get_match(db, data.match_id)
    second_hand = []
    for card in match.second_hand:
        if card:
            second_hand.append(card)
        else:
            second_hand.append(data.new_cards.pop(0))
    new_bet, _ = check_hand(second_hand, 2)
    new_match = {
        "id": match.id,
        "opponent": match.opponent,
        "first_hand": match.first_hand,
        "second_hand": second_hand,
        "player_first_bet": match.player_first_bet,
        "player_second_bet": new_bet,
        "opponent_first_bet": data.match_bet - match.player_first_bet,
        "opponent_second_bet": None,
        "result": None,
        "balance": None,
    }
    match_repository.put_match(db, data.match_id, new_match)
    return SecondRoundResponse(bet=new_bet)

def result(db: Session, data: ResultReceive):
    match = match_repository.get_match(db, data.match_id)
    opponent_second_bet = abs(data.your_match_balance) - match.player_first_bet - match.player_second_bet - match.opponent_first_bet
    new_match = {
        "id": match.id,
        "opponent": match.opponent,
        "first_hand": match.first_hand,
        "second_hand": match.second_hand,
        "player_first_bet": match.player_first_bet,
        "player_second_bet": match.player_second_bet,
        "opponent_first_bet": match.opponent_first_bet,
        "opponent_second_bet": opponent_second_bet,
        "result": data.result,
        "balance": data.your_match_balance,
    }
    match_repository.put_match(db, data.match_id, new_match)
    return {"message": "Match finished"}