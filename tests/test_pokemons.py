import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "6a7a9f0b427e36f2259b3e943ed707c0"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = "22872"


def test_status_code():
    response = requests.get(url=f"{URL}/trainers", params={"trainer_id": TRAINER_ID})
    assert response.status_code == 200


def test_trainer_name():
    response_get = requests.get(
        url=f"{URL}/trainers", params={"trainer_id": TRAINER_ID}
    )
    assert response_get.json()["data"][0]["trainer_name"] == "1А Ревальт из Сирии"
