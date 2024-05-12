import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'enter your token'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Tom",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
body_changename = {
    "pokemon_id": "id_pokemon",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
body_addpokeball = {
    "pokemon_id": "26825"

}


'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

"""response_changename = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_changename)
print(response_changename.text)"""

response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeball)
print(response_addpokeball.text)
