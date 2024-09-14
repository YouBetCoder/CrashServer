import decimal
from typing import List

from servicestack import JsonServiceClient
from dotenv import load_dotenv

from predictCrash.dtos import ApiQueryActiveGameRoom, ApiQueryActiveRoomPredictionResults, ActiveGameResult
from teacup import detect_enders_teacup

load_dotenv()
import os

host = os.environ.get("HOST", 'https://localhost:5001')
host_key = os.environ.get("APIKEY", None)

client = JsonServiceClient(host)
client.set_bearer_token(host_key)

client.headers['X-Api-Key'] = host_key

response = client.get(ApiQueryActiveRoomPredictionResults(), args={'OrderByDesc': 'Id', 'Take': 1000})
results = []
print(f"total records {response.total}")
skip = 0
while len(response.results) > 0:
    results = results + response.results
    skip = skip + 1000
    response = client.get(ApiQueryActiveRoomPredictionResults(), args={'OrderByDesc': 'Id', 'Take': 1000, 'Skip': skip})

results.sort(key=lambda x: x.active_game_room_round_id, reverse=False)

success = 0
fail = 0
tries = 0
for i in range(len(results) - 3):
    items: List[ActiveGameResult] = results[i:i + 4]

    decimals = list(map(lambda x: x.game_result, items))

    if detect_enders_teacup(decimals):
        print("Tea cup")
        print(list(map(lambda x: x.active_game_room_round_id, items)))
        print(list(map(lambda x: x.game_result, items)))
        next_result = results[i + 4]
        tries = tries + 1
        if next_result.game_result > decimal.Decimal(2):
            success = success + 1
        else:
            fail = fail + 1

        print(f"Next result,{next_result.active_game_room_round_id} {next_result.game_result}")

success_tries = round(success / tries, 2)
print(f"Results {success} / {tries} = {success_tries}")
