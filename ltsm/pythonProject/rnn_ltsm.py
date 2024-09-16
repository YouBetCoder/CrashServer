import os
from time import sleep

from dotenv import load_dotenv

from predictCrash.logg import logger

load_dotenv()


from predictCrash.wait_and_predict import wait_and_predict

print(os.environ);

def main():
    last_round_id = 0
    while True:
        try:
            last_round_id = wait_and_predict(last_round_id)
        except Exception as e:
            logger.error("Error in rnn loop",exc_info=1)
            sleep(5)


if __name__ == '__main__':
    main()
