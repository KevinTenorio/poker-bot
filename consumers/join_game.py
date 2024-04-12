import requests
from domain.schemas.match import JoinGame

DEALER_URL = 'http://dealer:8000'
MY_API_URL = 'https://f222-177-37-174-87.ngrok-free.app'

async def post_join_game(data: JoinGame) -> dict:
    url = DEALER_URL + '/join-game'
    response = requests.post(
        url=url, json=data, timeout=30)
    print(response.json())
    return response.json()

my_data = JoinGame(
    {
        "id": "kevin.souza@lccv.ufal.br",
        "name": "Kevin Tenório",
        "public_api_url": MY_API_URL
    }
)

post_join_game(my_data)