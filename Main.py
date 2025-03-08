import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "6a7a9f0b427e36f2259b3e943ed707c0"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}

# 1 тело для создания покемона
create_pokemon = {"name": "Abu", "photo_id": 50}

response1 = requests.post(
    url=f"{URL}/pokemons", headers=HEADER, json=create_pokemon
)  # Запрос на создание покемона
print(response1.text)  # отобразить ответ в виде текста в терминале
pokemon_id = response1.json()["id"]

# 2 тело для изменения покемона
rename_pokemon = {"pokemon_id": pokemon_id, "name": "Aboba", "photo_id": 50}

response2 = requests.put(
    url=f"{URL}/pokemons", headers=HEADER, json=rename_pokemon
)  # Запрос на переименование (изменение) покемона
print(response2.text)  # отобразить ответ в виде текста в терминале

# 3 Ловля в шар
add_in_ball = {"pokemon_id": pokemon_id}

response3 = requests.post(
    url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=add_in_ball
)  # Запрос на ловлю
print(response3.text)
