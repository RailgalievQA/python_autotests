import requests

host='https://api.pokemonbattle.me:9104'


response = requests.post(url=f'{host}/trainers/reg', 
                        json={
                            "trainer_token": "6df92b5317436e684b748ff16ee5be8c",
                            "email": "8963741@mail.ru",
                            "password": "Iloveqa1"
                            },
                            headers={'Content-Type': 'application/json'}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')


response = requests.post(url=f'{host}/trainers/confirm_email', 
                        json={"trainer_token": "6df92b5317436e684b748ff16ee5be8c"},
                        headers={'Content-Type': 'application/json'}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

response = requests.post(url=f'{host}/pokemons', 
                        json={"name": "generate",
                              "photo": "generate"},
                        headers={'Content-Type': 'application/json','trainer_token': '6df92b5317436e684b748ff16ee5be8c'}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')


response = requests.put(url=f'{host}/pokemons', 
                        json={ "pokemon_id": "21141","name": "Pytest","photo": "https://dolnikov.ru/pokemons/albums/008.png"},
                        headers={'Content-Type': 'application/json','trainer_token': '6df92b5317436e684b748ff16ee5be8c'}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')


response = requests.post(url=f'{host}/trainers/add_pokeball', 
                        json={  "pokemon_id": "21141"},
                        headers={'Content-Type': 'application/json','trainer_token': '6df92b5317436e684b748ff16ee5be8c'}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')