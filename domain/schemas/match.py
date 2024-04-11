from pydantic import Field, UUID4, EmailStr
from domain.schemas.generic import GenericSchema

class FirstRoundReceive(GenericSchema):
    match_id: UUID4 = Field(example="27079164-594e-4405-9197-7e99194ccbf0", title="Match UUID")
    cards: list[str] = Field(example=["Ah", "Kd", "Jc", "2c", "6h"], title="List of cards")
    opponent_id: EmailStr = Field(example="fulaninho@gmail.com", title="Opponent email id")
    class Config:
        from_attributes = True

class FirstRoundResponse(GenericSchema):
    bet: int
    cardsToSwap: list[str]

class SecondRoundReceive(GenericSchema):
    match_id: UUID4 = Field(example="27079164-594e-4405-9197-7e99194ccbf0", title="Match UUID")
    new_cards: list[str] = Field(example=["Ah", "Kd", "Jc", "2c", "6h"], title="List of cards")
    match_bet: int = Field(example=100, title="Match bet")

class SecondRoundResponse(GenericSchema):
    bet: int

class ResultReceive(GenericSchema):
    match_id: UUID4 = Field(example="27079164-594e-4405-9197-7e99194ccbf0", title="Match UUID")
    result: str = Field(example="LOSS", title="Match result. Can be LOSS, WIN or DRAW")
    your_match_balance: int = Field(example=100, title="Your match balance")

class JoinGame(GenericSchema):
    id: EmailStr = Field(example="fulaninho@gmail.com", title="Your email id")
    name: str = Field(example="Fulaninho", title="Your name")
    public_api_url: str = Field(example="https://api.github.com/users/fulaninho", title="Your public API URL")