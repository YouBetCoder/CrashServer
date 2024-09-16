import os
import time
from datetime import datetime, timedelta

import pytz
from servicestack import JsonServiceClient

from predictCrash.dtos import ApiQueryActiveRoomPredictionResults, ApiQueryActiveGameRoom


def get_timestamp_10_minutes_ago():
    # Get the current time in UTC
    now = datetime.now()

    # Subtract 10 minutes
    ten_minutes_ago = now - timedelta(minutes=10)

    # Convert to Unix timestamp (seconds since epoch)
    timestamp = int(ten_minutes_ago.timestamp())

    return timestamp


def get_all_game_results(ago):
    host = os.environ.get("HOST", 'https://localhost:5001')
    host_key = os.environ.get("APIKEY", None)
    client = JsonServiceClient(host)
    client.set_bearer_token(host_key)
    client.headers['X-Api-Key'] = host_key
    response = client.get(ApiQueryActiveGameRoom(room_id=1),
                          args={'OrderByDesc': 'Id', 'Take': 1000, "timeRecordedGreaterThan": str(ago)
                                })
    results = []
    print(f"total records {response.total}")
    skip = 0
    while len(response.results) > 0:
        results = results + response.results
        skip = skip + 1000
        response = client.get(ApiQueryActiveGameRoom(room_id=1),
                              args={'OrderByDesc': 'Id', 'Take': 1000, 'Skip': skip,
                                    "timeRecordedGreaterThan": ago})
    results.sort(key=lambda x: x.round_id, reverse=False)
    return results




def get_unix_time_stamp_minutes(minutes_ago):
    """Gets the Unix timestamp for a given number of days ago.

    Args:
      days_ago: The number of days to subtract from the current time.

    Returns:
      The Unix timestamp for the specified time.
    """

    # Get the current time in seconds since the Unix epoch.
    current_time = time.time()

    # Calculate the time for the specified number of days ago.
    target_time = current_time - (minutes_ago  * 60)

    return int(target_time)


def get_unix_time_stamp_hours(hours_ago):
    """Gets the Unix timestamp for a given number of days ago.

    Args:
      days_ago: The number of days to subtract from the current time.

    Returns:
      The Unix timestamp for the specified time.
    """

    # Get the current time in seconds since the Unix epoch.
    current_time = time.time()

    # Calculate the time for the specified number of days ago.
    target_time = current_time - (hours_ago * 60 * 60)

    return int(target_time)



def get_unix_time_stamp_days_ago(days_ago):
    """Gets the Unix timestamp for a given number of days ago.

    Args:
      days_ago: The number of days to subtract from the current time.

    Returns:
      The Unix timestamp for the specified time.
    """

    # Get the current time in seconds since the Unix epoch.
    current_time = time.time()

    # Calculate the time for the specified number of days ago.
    target_time = current_time - (days_ago * 24 * 60 * 60)

    return int(target_time)


# Get Unix timestamps for 1 week, 1 month, and 1 day prior.


def get_last_1000_game_results():
    host = os.environ.get("HOST", 'https://localhost:5001')
    host_key = os.environ.get("APIKEY", None)
    client = JsonServiceClient(host)
    client.set_bearer_token(host_key)
    client.headers['X-Api-Key'] = host_key
    response = client.get(ApiQueryActiveGameRoom(room_id=1),
                          args={'OrderByDesc': 'Id', 'Take': 1000, "noMoreBetsAtGreaterThan": str(one_day_ago)})
    return response.results
