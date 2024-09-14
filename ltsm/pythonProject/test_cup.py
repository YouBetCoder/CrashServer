import decimal
from typing import List

from dotenv import load_dotenv

load_dotenv()
from get_all_game_results import get_all_game_results
from predictCrash.dtos import ActiveGameResult
from predictCrash.teacup import detect_enders_teacup

results = get_all_game_results()

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
