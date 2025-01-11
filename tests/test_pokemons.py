import requests

URL = 'https://api.pokemonbattle-stage.ru/v2'
HEADER = {'Content-Type': 'application/json'}
TRAINER_NAME = 'STDalex'
TRAINER_ID = '1509'

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200


def test_current_trainer_name():
    response_get = requests.get(url=f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == TRAINER_NAME