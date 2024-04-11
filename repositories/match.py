from sqlalchemy.orm import Session
from fastapi import HTTPException
from domain.models.match import Match
from domain.schemas.match import FirstRoundReceive
from uuid import UUID

def post_match(db: Session, data: FirstRoundReceive, bet: int, cards_to_swap: list[str]):
    request_dict = data.model_dump()
    second_hand: list[str] = request_dict['cards'].copy()
    for card in cards_to_swap:
        second_hand.remove(card)
        second_hand.append(None)
    new_dict = {
        "id": request_dict['match_id'],
        "opponent": request_dict['opponent_id'],
        "first_hand": request_dict['cards'],
        "second_hand": second_hand,
        "player_first_bet": bet,
        "player_second_bet": None,
        "opponent_first_bet": None,
        "opponent_second_bet": None,
        "result": None,
        "balance": None,
    }
    new_match = Match(**new_dict)
    db.add(new_match)

    db.commit()
    db.refresh(new_match)
    return new_match

def get_match(db: Session, match_id: UUID):
    db_match = db.query(Match).filter(Match.id == match_id).first()
    if db_match is None:
        raise HTTPException(status_code=404, detail=f'Match of id={match_id} not found')
    return db_match

def put_match(db: Session, match_id: UUID, match: Match):
    db_match = get_match(db, match_id)
    request_dict = match
    for key, value in request_dict.items():
        setattr(db_match, key, value)
    db.commit()
    return db_match


