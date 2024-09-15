import os

from servicestack import JsonServiceClient

from predictCrash.dtos import ApiQueryActiveRoomPredictionResults


def get_all_game_results():
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
        response = client.get(ApiQueryActiveRoomPredictionResults(),
                              args={'OrderByDesc': 'Id', 'Take': 1000, 'Skip': skip})
    results.sort(key=lambda x: x.active_game_room_round_id, reverse=False)
    return results


def get_last_1000_game_results():
    host = os.environ.get("HOST", 'https://localhost:5001')
    host_key = os.environ.get("APIKEY", None)
    client = JsonServiceClient(host)
    client.set_bearer_token(host_key)
    client.headers['X-Api-Key'] = host_key
    response = client.get(ApiQueryActiveRoomPredictionResults(), args={'OrderByDesc': 'Id', 'Take': 10})
    return response.results
