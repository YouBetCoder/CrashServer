import decimal
import os
import time
from typing import List

import numpy
from servicestack import WebServiceException

from predictCrash.arima import predict_next_decimal_arima
from predictCrash.dtos import CreateActiveGameRoomPrediction, ApiQueryActiveGameRoom, NotifyLiveViewDataUpdatedRequest
from predictCrash.fb_prophet import predict_next_result_prophet, predict_next_result_prophet2
from predictCrash.get_game_data import get_next_game
from predictCrash.kalman import predict_next_kalman
from predictCrash.logg import logger

from predictCrash.service_stack_client import create_client
from predictCrash.teacup import detect_enders_teacup
import gc

client = create_client()
import matplotlib.pyplot as plt

decimal_0 = decimal.Decimal(0)

webhook_url = os.environ.get('WEBHOOK_DISCORD', None)
if webhook_url is None:
    raise RuntimeError("No webhook")

webhook_status_url = os.environ.get('WEBHOOK_DISCORD_STATUS', None)
if webhook_status_url is None:
    raise RuntimeError("No  webhook_status_url webhook")

from discord_webhook import DiscordWebhook, DiscordEmbed

yellow = 'FFFF00'
blue = '03b2f8'


def send_predictions_to_discord(last_game, room_id, arima_result, kalman_result, decimal_result_3, decimal_result4,
                                std_dev, last_3_games, last_3_std_dev, last_5_results, teacup_detect):
    try:
        plt.clf()
        plt.plot(last_5_results)
        plt.title('Last 5 Results')
        plt.ylabel('Results')
        plt.xlabel('Games')
        plt.grid(True)

        # Save the plot as a png image
        image_file = 'plot.png'
        plt.savefig(image_file)

        webhook = DiscordWebhook(url=webhook_url)

        # Add the image to webhook
        with open(image_file, "rb") as f:
            webhook.add_file(file=f.read(), filename='plot.png')

        webhook = DiscordWebhook(url=webhook_url)

        # each field as a separate embed

        embed_last_games = DiscordEmbed(title="Last 5 games",
                                        description=f", ".join(last_3_games),
                                        color=yellow)
        teacup = "Yes" if teacup_detect else "No"

        teacup_color = blue if teacup_detect else yellow
        embed_teacup = DiscordEmbed(title="Teacup Detected:",
                                    description=f"{teacup}",
                                    color=teacup_color)

        embed_last_std = DiscordEmbed(title="Last 5 Std Dev",
                                      description=" " + f", ".join(last_3_std_dev),
                                      color=yellow)
        color_arima_result = blue if arima_result >= 2 else 'FF0000'
        embed_arima_result = DiscordEmbed(title="Arima Result", description=f"{arima_result}", color=color_arima_result)
        color_kalman_result = blue if kalman_result >= 2 else 'FF0000'
        embed_kalman_result = DiscordEmbed(title="Prediction 2", description=f"{kalman_result}",
                                           color=color_kalman_result)
        color_decimal_result_3 = blue if decimal_result_3 >= 2 else 'FF0000'
        embed_decimal_result_3 = DiscordEmbed(title="Prediction 3 (weighted)", description=f"{decimal_result_3}",
                                              color=color_decimal_result_3)
        color_decimal_result4 = blue if decimal_result4 >= 2 else 'FF0000'
        embed_decimal_result4 = DiscordEmbed(title="Prediction 4", description=f"{decimal_result4}",
                                             color=color_decimal_result4)
        color_std_dev = blue if std_dev >= 8 else 'FF0000'
        embed_std_dev = DiscordEmbed(title="Std Dev", description=f"{std_dev}", color=color_std_dev)

        color_last_game = blue if last_game.game_result >= 1.6 else 'FF0000'
        embed_last_game_result = DiscordEmbed(title=f"----ROUND :{last_game.round_id}----\n",
                                              description=f"Result: {last_game.game_result}\n"
                                                          f"Next Game is {last_game.round_id + 1}",
                                              color=color_last_game)

        webhook.add_embed(embed_last_game_result)

        webhook.add_embed(embed_last_std)

        webhook.add_embed(embed_last_games)
        webhook.add_embed(embed_teacup)

        webhook.add_embed(embed_kalman_result)

        webhook.add_embed(embed_decimal_result_3)
        webhook.add_embed(embed_decimal_result4)
        webhook.add_embed(embed_std_dev)
        with open(image_file, "rb") as f:
            webhook.add_file(file=f.read(), filename='plot.png')

        webhook.execute()

    except Exception as e:
        logger.error("Error update main webhook", exc_info=1)
    finally:
        gc.collect()


def send_bot_status_message(msg):
    try:
        webhook = DiscordWebhook(url=webhook_status_url)
        embed_teacup = DiscordEmbed(title="BOT STATUS MESSAGE:",
                                    description=msg,
                                    color=yellow)
        webhook.add_embed(embed_teacup)
        webhook.execute()
    except Exception as e:
        logger.error("Error update status webhook", exc_info=1)


def check_items(items: List[ApiQueryActiveGameRoom]) -> bool:
    last_30 = items[-30:]
    current = last_30[0]
    for i in range(1, len(last_30)):
        next = last_30[i]
        # logger.info(f"{current.round_id} -> {next.round_id}")
        if current.round_id + 1 != next.round_id:
            logger.info(f"There are only {i - 1} ordered sequences")
            time.sleep(30)
            send_bot_status_message(f"Bot is retraining {i - 1} dataz to go")
            return False
        current = next
    return True


last_3_std_dev = []


def wait_and_predict(prev_round_id):
    items, data, last_game, last_round_id = get_next_game(prev_round_id)
    if len(items) < 30:
        logger.info("Not enough data to make predictions")
        return last_round_id
    if not check_items(items):
        logger.info("Not enough sequential data to make predictions")
        return last_round_id
    if prev_round_id == last_round_id:
        return last_round_id
    room_id = last_game.room_id
    game_number = last_game.game_number

    logger.info(f"Looking at game {game_number} round {last_round_id} room {room_id}")
    last_30 = data[-30:]
    last_302 = data[-30:]
    arima_result = predict_next_decimal_arima(last_30)

    last_5 = data[-5:]

    #
    # next_result = predict_next_result3(last_30)
    # if isinstance(next_result, numpy.float32):
    #     decimal_result = Decimal(float(next_result))
    # else:
    #     decimal_result = Decimal(float(next_result[0][0]))
    #
    # decimal_result2 = weighted_average(last_30)
    # # if isinstance(next_result2, numpy.float32):
    # #     decimal_result2 = Decimal(float(next_result2))
    # # else:
    # #     decimal_result2 = Decimal(float(next_result2[0][0]))
    #
    # decimal_result3 = decimal.Decimal(0)
    # # next_result3 = predict_next_result3(data[-10:])
    # # if isinstance(next_result3, numpy.float32):
    # #     decimal_result3 = Decimal(float(next_result3))
    # # else:
    # #     decimal_result3 = Decimal(float(next_result3[0][0]))
    #

    next_predictions = predict_next_kalman(data)
    kalman_result = next_predictions[0]

    std_dev = numpy.std(last_30)
    while len(last_3_std_dev) > 4:
        last_3_std_dev.pop()
    last_3_std_dev.append(str(round(std_dev, 2)))
    decimal_result_3 = predict_next_result_prophet2(last_302)
    decimal_result4 = predict_next_result_prophet(last_30)

    teacup_detect = detect_enders_teacup(last_5[-4:])
    last_three_results = list(map(str, last_30[-5:]))
    send_predictions_to_discord(last_game, room_id, arima_result, round(kalman_result, 2), round(decimal_result_3, 2),
                                round(decimal_result4, 2),
                                std_dev, last_three_results, last_3_std_dev, last_5, teacup_detect)
    try:
        result: CreateActiveGameRoomPrediction = CreateActiveGameRoomPrediction(game_number=game_number,
                                                                                room_id=room_id,
                                                                                active_game_room_id=room_id,
                                                                                prediction=std_dev,
                                                                                round_id=last_game.round_id + 1,
                                                                                prediction2=kalman_result,
                                                                                prediction3=decimal_result_3,
                                                                                prediction4=decimal_result4,
                                                                                prediction_arima=arima_result)

        post_result = client.post(result)
        client.post(NotifyLiveViewDataUpdatedRequest(id=int(post_result.id), tea_cup=teacup_detect))
        logger.info(post_result)
    except WebServiceException as we:
        logger.error("Error uploading to server", exc_info=1)
        logger.error(str(we.inner_exception), exc_info=1)
    except Exception as e:
        logger.error("Error uploading to server", exc_info=1)

    return last_round_id
