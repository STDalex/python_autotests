import requests

URL = 'https://api.pokemonbattle-stage.ru/v2'
TOKEN = 'insert_your_trainer_token_here'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}

create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = {"name":"PyTestPock1", "photo_id": -1})
print(create.text)
pokemon_id = create.json()['id'];

change = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = {"pokemon_id": pokemon_id, "name":"PyTestPock2"})
print(change.text)

catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = {"pokemon_id": pokemon_id})
print(catch.text)

delete = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = {"pokemon_id": pokemon_id})
print(delete.text)