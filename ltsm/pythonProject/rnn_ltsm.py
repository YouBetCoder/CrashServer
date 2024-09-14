from dotenv import load_dotenv

load_dotenv()

from predictCrash.wait_and_predict import wait_and_predict
import os


def main():
    last_round_id = 0
    while True:
        last_round_id = wait_and_predict(last_round_id)


if __name__ == '__main__':
    main()
