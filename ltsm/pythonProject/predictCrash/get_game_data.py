import os
from time import sleep

from predictCrash.dtos import ApiQueryActiveGameRoom, ActiveGameRoom
from predictCrash.service_stack_client import create_client

room_id = int(os.environ.get('ROOM_ID', 1))
client = create_client()


def get_data():
    response = client.get(ApiQueryActiveGameRoom(room_id=room_id), args={'OrderByDesc': 'Id', 'Take': 1000})
    items = response.results
    items.reverse()
    data = list(map(lambda x: float(x.game_result), items))  # Apply conversion to float here
    return items, data


def get_next_game(last_round_id):
    items, data = get_data()
    while True:
        last_game: ActiveGameRoom = items[-1]

        if last_game.round_id != last_round_id:
            return items, data, last_game, last_game.round_id
        items, data = get_data()
        sleep(2)
