from sqlalchemy import Column, String, UUID, Integer
from sqlalchemy.dialects.postgresql import ARRAY
from domain.models.generic import GenericBase

class Match(GenericBase):
    __tablename__ = "matches"

    id = Column("id", UUID(as_uuid=True), primary_key=True)
    opponent = Column("opponent", String, nullable=False)
    first_hand = Column("first_hand", ARRAY(String), nullable=False)
    second_hand = Column("second_hand", ARRAY(String), nullable=True)
    player_first_bet = Column("player_first_bet", Integer, nullable=True)
    player_second_bet = Column("player_second_bet", Integer, nullable=True)
    opponent_first_bet = Column("opponent_first_bet", Integer, nullable=True)
    opponent_second_bet = Column("opponent_second_bet", Integer, nullable=True)
    result = Column("result", String, nullable=True)
    balance = Column("balance", Integer, nullable=True)
