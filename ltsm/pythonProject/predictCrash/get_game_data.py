import os
from time import sleep

from predictCrash.dtos import ApiQueryActiveGameRoom, ActiveGameRoom
from predictCrash.logg import logger
from predictCrash.service_stack_client import create_client

room_id = int(os.environ.get('ROOM_ID', 1))
client = create_client()


def get_data():
    response = client.get(ApiQueryActiveGameRoom(room_id=room_id), args={'OrderByDesc': 'Id', 'Take': 100})
    items = response.results
    items.reverse()
    data = list(map(lambda x: float(x.game_result), items))  # Apply conversion to float here
    return items, data


def get_is_new_round(last_round_id):
    response = client.get(ApiQueryActiveGameRoom(room_id=room_id), args={'OrderByDesc': 'Id', 'Take': 1})
    items = response.results
    if len(items) > 0:
        last_game = items[0]
        logger.info(f"Comparing rounds {last_game.round_id} > {last_round_id} ")
        return last_game.round_id > last_round_id
    return False


def get_next_game(last_round_id):
    while True:
        if not get_is_new_round(last_round_id):
            sleep(4)
            continue
        items, data = get_data()
        last_game: ActiveGameRoom = items[-1]
        return items, data, last_game, last_game.round_id
