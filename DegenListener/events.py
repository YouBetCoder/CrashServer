import decimal
import json
import os

import websocket
from datetime import datetime

from dtos import ActiveGameRoom, CreateActiveGameRoom
from service_stack_client import create_client

client = create_client()

room_id = os.environ.get("ROOM_ID", 1)
register = {
    "id": "424b99e4-ff98-49d3-9498-e4a5457e3d36",
    "payload": {
        "data": json.dumps({
            'query': 'subscription ActiveGameRoomSubscription($gameNumber: String!, $roomId: String!) {\n  onActiveGameRoomUpdated(gameNumber: $gameNumber, roomId: $roomId) {\n    gameNumber\n    roomId\n    roundId\n    gameStatus\n    gamePhase\n    gameResult\n    players {\n      pubkey\n      lamports\n      choice\n      reward\n      username\n    }\n    noMoreBetsAt\n  }\n}\n',
            'variables': {'gameNumber': '2', 'roomId': f'{room_id}'}
        }),
        "extensions": {
            "authorization": {
                "host": "nfttalsd3vagzomgk3yxyxjvuq.appsync-api.us-east-2.amazonaws.com",
                "x-amz-date": "20240909T191434Z",
                "x-api-key": "da2-6wh5hjo6jneprn7caqnirsx2ay",
                "x-amz-user-agent": "aws-amplify/6.2.0 api/1 framework/1"
            }
        }
    },
    "type": "start"
}

seen = {room_id: {}}


def degen_on_open(wsapp: websocket.WebSocket):
    wsapp.send(json.dumps(register))


def degen_on_close(wsapp: websocket.WebSocket, status_code, status_message):
    print("close")


def degen_on_error(wsapp: websocket.WebSocket, message):
    print(message)


def degen_on_reconnect(wsapp: websocket.WebSocket):
    print("reconnect")


def degen_on_ping(wsapp: websocket.WebSocket, message):
    print(message)


def handle_payload(wsapp: websocket.WebSocket, payload: dict):
    data = payload.get('data', None)
    if data is None:
        return
    update_message: dict | None = data.get('onActiveGameRoomUpdated', None)
    if update_message is None:
        return

    game_phase = update_message.get('gamePhase')
    if game_phase is None:
        print("NO GAME PHASE FOUND -- WEIRD")
        return
    print(f"Game Phase: {game_phase}")
    if game_phase != 'GAME_DISTRIBUTION_STARTED':
        return

    date: str | None = update_message.get('noMoreBetsAt', None)
    game_number: str | None = update_message.get('gameNumber', None)
    current_room_id: str | None = update_message.get('roomId', None)
    round_id: str | None = update_message.get('roundId', None)
    game_status: str | None = update_message.get('gameStatus', None)
    game_phase: str | None = update_message.get('gamePhase', None)
    game_result: str | None = update_message.get('gameResult', None)
    if any(value is None for value in [date, game_number, room_id, round_id, game_status, game_phase, game_result]):
        print(f'INVALID DATA {payload}')
        return

    if seen[room_id].get(round_id) is not None:
        return
    seen[room_id][round_id] = 1

    datetime_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')  # parses the date string into a datetime object
    date_timestamp = int(datetime_obj.timestamp())

    active_game = CreateActiveGameRoom(
        game_number=int(game_number),
        room_id=int(current_room_id),
        round_id=int(round_id),
        game_status=game_status,
        game_phase=game_phase,
        game_result=decimal.Decimal(float(game_result)),
        no_more_bets_at=date_timestamp,

    )
    send_result = client.send(active_game)
    print(update_message)
    print(send_result)


def degen_on_message(wsapp: websocket.WebSocket, message):
    try:
        msg_data = json.loads(message)
        msg_type = msg_data.get('type')
        if msg_type is not None and msg_type == "start_ack":
            print("websock starting")
            return
        payload = msg_data.get('payload')
        if payload is not None:
            handle_payload(wsapp, payload)
            return

        print(f"Got message {msg_data} ")
    except Exception as e:
        print(f"Could not read: {message}")
        print((str(e)))


