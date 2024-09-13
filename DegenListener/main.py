import os
from dotenv import load_dotenv
load_dotenv()
print(os.environ)
print(os.environ)
import websocket

from events import degen_on_close, degen_on_error, degen_on_reconnect, degen_on_ping, degen_on_message, degen_on_open

def main():
    wsapp = websocket.WebSocketApp(
        "wss://nfttalsd3vagzomgk3yxyxjvuq.appsync-realtime-api.us-east-2.amazonaws.com/graphql?header=eyJob3N0IjoibmZ0dGFsc2QzdmFnem9tZ2szeXh5eGp2dXEuYXBwc3luYy1hcGkudXMtZWFzdC0yLmFtYXpvbmF3cy5jb20iLCJ4LWFtei1kYXRlIjoiMjAyNDA5MDlUMTkwMzE0WiIsIngtYXBpLWtleSI6ImRhMi02d2g1aGpvNmpuZXBybjdjYXFuaXJzeDJheSJ9&payload=e30=",
        on_ping=degen_on_ping,
        on_close=degen_on_close,
        subprotocols=["graphql-ws"],
        on_error=degen_on_error,
        on_open=degen_on_open,
        on_reconnect=degen_on_reconnect,
        on_message=degen_on_message)
    wsapp.run_forever()


def degen_create_headers():
    return {'Sec-WebSocket-Protocol': 'graphql-ws'}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
