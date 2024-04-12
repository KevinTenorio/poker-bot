import requests

DEALER_URL = 'https://57405e80-d9e0-4eb1-897d-51304945e739.mock.pstmn.io'
MY_API_URL = 'https://f222-177-37-174-87.ngrok-free.app'

def post_join_game(data) -> dict:
    url = DEALER_URL + '/join-game'
    response = requests.post(
        url=url, json=data, timeout=30)
    print(response)
    return response

my_data = {
        "id": "kevin.souza@lccv.ufal.br",
        "name": "Kevin Tenório",
        "public_api_url": MY_API_URL
    }

post_join_game(my_data)
