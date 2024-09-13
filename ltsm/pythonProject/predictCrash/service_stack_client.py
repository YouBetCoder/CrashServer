import os

from servicestack import JsonServiceClient, Authenticate

host = os.environ.get("HOST", 'https://localhost:5001')
host_key = os.environ.get("APIKEY", None)


def create_client():

    client = JsonServiceClient(host)
    client.set_bearer_token(host_key)

    client.headers['X-Api-Key'] = host_key

    return client


