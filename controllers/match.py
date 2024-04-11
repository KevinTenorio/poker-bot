from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_session
from domain.schemas.match import FirstRoundReceive, FirstRoundResponse, SecondRoundReceive, SecondRoundResponse, ResultReceive
from services import match as match_service

router = APIRouter()

TAGS = ["Match"]

@router.get("/health/liveness", tags=["Liveness"], summary='Check if the service is alive', status_code=200)
def liveness():
    return {"status": "alive"} if Depends(get_session) else {"status": "dead"}

@router.post("/first-round", tags=TAGS, summary='Start the first round of a new match', status_code=201, response_model=FirstRoundResponse)
def first_round(data: FirstRoundReceive, db: Session = Depends(get_session)):
    return match_service.first_round(db, data)

@router.post("/second-round", tags=TAGS, summary='Start the second round of a match', status_code=201, response_model=SecondRoundResponse)
def second_round(data: SecondRoundReceive, db: Session = Depends(get_session)):
    return match_service.second_round(db, data)

@router.post("/result", tags=TAGS, summary='Finish the match', status_code=201)
def result(data: ResultReceive, db: Session = Depends(get_session)):
    return match_service.result(db, data)
