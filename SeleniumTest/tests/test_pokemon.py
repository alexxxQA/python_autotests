import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'enter your token'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 2267

'''def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response.status_code == 200'''

'''def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'New Name'
'''
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response.status_code == 200   
    
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == '2267'


@pytest.mark.parametrize('key, value', [('id', '2267'), ('trainer_name', 'Clown'), ('city', 'Tokyo')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
