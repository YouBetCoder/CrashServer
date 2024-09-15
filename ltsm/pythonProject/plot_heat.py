import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import pytz
from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
import os
from get_all_game_results import get_all_game_results, get_last_1000_game_results

load_dotenv()

webhook_url = os.environ.get('WEBHOOK_DISCORD_HEAT', None)
if webhook_url is None:
    raise RuntimeError("No webhook URL found in environment variables")


def post_heatmap_to_discord(results, title):
    df = pd.DataFrame([
        {
            'game_result': float(r.game_result),
            'timestamp': datetime.fromtimestamp(r.no_more_bets_at, tz=pytz.UTC),
            'round_id': r.active_game_room_round_id
        } for r in results
    ])

    df = df.sort_values('timestamp')
    df['hour_utc'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek

    pivot = df.pivot_table(
        values='game_result',
        index='hour_utc',
        columns='day_of_week',
        aggfunc='mean'
    )

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot, cmap='YlOrRd', annot=True, fmt='.2f')
    plt.title('Average Game Result by Hour (UTC) and Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Hour of Day (UTC)')
    plt.xticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.yticks(range(0, 24, 2), [f'{h:02d}:00' for h in range(0, 24, 2)])
    plt.tight_layout()

    image_file = 'heat_map.png'
    plt.savefig(image_file, format='png', dpi=300, bbox_inches='tight')

    high_numbers = df[df['game_result'] > 60]
    avg_result = df['game_result'].mean()
    highest_hour = pivot.mean(axis=1).idxmax()
    highest_hour_avg = pivot.mean(axis=1).max()
    highest_day_index = pivot.mean(axis=0).idxmax()
    highest_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][highest_day_index]
    highest_day_avg = pivot.mean(axis=0).max()

    webhook = DiscordWebhook(url=webhook_url)

    with open(image_file, "rb") as f:
        webhook.add_file(file=f.read(), filename='heat_map.png')

    embed = DiscordEmbed(title=title, color=242424)
    embed.set_image(url="attachment://heat_map.png")
    embed.add_embed_field(name="Total High Numbers (>60)", value=f"{len(high_numbers)}")
    embed.add_embed_field(name="Average Game Result", value=f"{avg_result:.2f}")
    embed.add_embed_field(name="Highest Average Hour (UTC)", value=f"{highest_hour:02d}:00 ({highest_hour_avg:.2f})")
    embed.add_embed_field(name="Highest Average Day", value=f"{highest_day} ({highest_day_avg:.2f})")

    webhook.add_embed(embed)
    response = webhook.execute()

    if response.status_code == 200:
        print("Heatmap and analysis successfully posted to Discord!")
    else:
        print(f"Failed to post to Discord. Status code: {response.status_code}")


if __name__ == "__main__":
   # results = get_all_game_results()
    results2 = get_last_1000_game_results()
   # post_heatmap_to_discord(results, "Heat Map All Time Results")
   # post_heatmap_to_discord(results2, "Heat Map Last 1000 games")
