import sys
from time import sleep

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import pytz
from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
import os
from get_all_game_results import get_all_game_results, get_unix_time_stamp_hours, get_timestamp_10_minutes_ago, \
    get_unix_time_stamp_days_ago, get_unix_time_stamp_minutes

load_dotenv()

webhook_url = os.environ.get('WEBHOOK_DISCORD_HEAT', None)
if webhook_url is None:
    raise RuntimeError("No webhook URL found in environment variables")

webhook_url_dist = os.environ.get('WEBOOK_DISCORD_DIST', None)
if webhook_url_dist is None:
    raise RuntimeError("No webhook URL (webhook_url_dist) found in environment variables")


def post_donut_chart_to_discord(results, title):
    df = pd.DataFrame([
        {
            'game_result': float(r.game_result),
            'timestamp': datetime.fromtimestamp(r.time_recorded, tz=pytz.UTC),
            'round_id': r.round_id
        } for r in results
    ])

    # Define the ranges
    ranges = ['1-10', '11-30', '31-60', '60+']

    # Create a function to categorize the results
    def categorize(value):
        if 1 <= value <= 10:
            return '1-10'
        elif 11 <= value <= 30:
            return '11-30'
        elif 31 <= value <= 60:
            return '31-60'
        else:
            return '60+'

    # Apply the categorization
    df['category'] = df['game_result'].apply(categorize)

    # Count the occurrences in each category
    category_counts = df['category'].value_counts().reindex(ranges, fill_value=0)

    # Create the donut chart
    plt.figure(figsize=(10, 10))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    plt.title('Distribution of Game Results')

    # Create the circle at the center to make it a donut chart
    center_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)

    # Save the chart
    image_file = 'donut_chart.png'
    plt.savefig(image_file, format='png', dpi=300, bbox_inches='tight')
    plt.close()

    # Calculate statistics
    total_games = len(df)
    avg_result = df['game_result'].mean()
    highest_result = df['game_result'].max()
    lowest_result = df['game_result'].min()

    # Create and send Discord webhook
    webhook = DiscordWebhook(url=webhook_url_dist)

    with open(image_file, "rb") as f:
        webhook.add_file(file=f.read(), filename='donut_chart.png')

    embed = DiscordEmbed(title=title, color=242424)
    embed.set_image(url="attachment://donut_chart.png")
    embed.add_embed_field(name="Total Games", value=f"{total_games}")
    embed.add_embed_field(name="Average Game Result", value=f"{avg_result:.2f}")
    embed.add_embed_field(name="Highest Result", value=f"{highest_result:.2f}")
    embed.add_embed_field(name="Lowest Result", value=f"{lowest_result:.2f}")

    for range_name in ranges:
        count = category_counts[range_name]
        percentage = (count / total_games) * 100
        embed.add_embed_field(name=f"{range_name} Range", value=f"{count} ({percentage:.1f}%)")

    webhook.add_embed(embed)
    response = webhook.execute()

    if response.status_code == 200:
        print("Donut chart and analysis successfully posted to Discord!")
    else:
        print(f"Failed to post to Discord. Status code: {response.status_code}")


def post_heatmap_to_discord(results, title):
    df = pd.DataFrame([
        {
            'game_result': float(r.game_result),
            'timestamp': datetime.fromtimestamp(r.time_recorded, tz=pytz.UTC),
            'round_id': r.round_id
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


def post_frequency_heatmap_to_discord(results, title):
    df = pd.DataFrame([
        {
            'game_result': float(r.game_result),
            'timestamp': datetime.fromtimestamp(r.time_recorded, tz=pytz.UTC),
            'round_id': r.round_id
        } for r in results
    ])

    df = df.sort_values('timestamp')
    df['hour_utc'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek

    # Create a new column for results over 10
    df['over_10'] = df['game_result'] > 10

    # Create pivot table for frequency of results over 10
    pivot = df.pivot_table(
        values='over_10',
        index='hour_utc',
        columns='day_of_week',
        aggfunc='mean'  # This gives us the proportion of results over 10
    )

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot, cmap='YlOrRd', annot=True, fmt='.2%')  # Format as percentage
    plt.title('Frequency of Game Results Over 10 by Hour (UTC) and Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Hour of Day (UTC)')
    plt.xticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.yticks(range(0, 24, 2), [f'{h:02d}:00' for h in range(0, 24, 2)])
    plt.tight_layout()

    image_file = 'heat_map.png'
    plt.savefig(image_file, format='png', dpi=300, bbox_inches='tight')

    total_games = len(df)
    games_over_10 = df['over_10'].sum()
    proportion_over_10 = games_over_10 / total_games
    highest_hour = pivot.mean(axis=1).idxmax()
    highest_hour_freq = pivot.mean(axis=1).max()
    highest_day_index = pivot.mean(axis=0).idxmax()
    highest_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][highest_day_index]
    highest_day_freq = pivot.mean(axis=0).max()

    webhook = DiscordWebhook(url=webhook_url)

    with open(image_file, "rb") as f:
        webhook.add_file(file=f.read(), filename='heat_map.png')

    embed = DiscordEmbed(title=title, color=242424)
    embed.set_image(url="attachment://heat_map.png")
    embed.add_embed_field(name="Total Games", value=f"{total_games}")
    embed.add_embed_field(name="Games Over 10", value=f"{games_over_10}")
    embed.add_embed_field(name="Proportion Over 10", value=f"{proportion_over_10:.2%}")
    embed.add_embed_field(name="Highest Frequency Hour (UTC)", value=f"{highest_hour:02d}:00 ({highest_hour_freq:.2%})")
    embed.add_embed_field(name="Highest Frequency Day", value=f"{highest_day} ({highest_day_freq:.2%})")

    webhook.add_embed(embed)
    response = webhook.execute()

    if response.status_code == 200:
        print("Heatmap and analysis successfully posted to Discord!")
    else:
        print(f"Failed to post to Discord. Status code: {response.status_code}")


if __name__ == "__main__":
    one_day_ago = get_unix_time_stamp_days_ago(1)
    one_week_ago = get_unix_time_stamp_days_ago(7)
    one_month_ago = get_unix_time_stamp_days_ago(30)
    ten_minutes = get_unix_time_stamp_minutes(10)
    hour_ago = get_unix_time_stamp_minutes(60)
    results_hour_ago = get_all_game_results(hour_ago)
    results_ten_minutes = get_all_game_results(ten_minutes)
    results_weak = get_all_game_results(one_week_ago)
    results_day = get_all_game_results(one_day_ago)
    results_month = get_all_game_results(one_month_ago)

    post_donut_chart_to_discord(results_day, "Score distribution Last Day")
    post_donut_chart_to_discord(results_hour_ago, "Score distribution 1 hour ago")
    post_donut_chart_to_discord(results_ten_minutes, "Score distribution 10 minutes ago")

    post_heatmap_to_discord(results_month, "Heat Map Last Month")
    post_heatmap_to_discord(results_weak, "Heat Map Last Weak")
    post_heatmap_to_discord(results_day, "Heat Map Last Day")
    post_frequency_heatmap_to_discord(results_month, "Frequency Heat Map Last Month")
    post_frequency_heatmap_to_discord(results_weak, "Frequency Heat Map Last Weak")
    post_frequency_heatmap_to_discord(results_day, "Frequency Heat Map Last Day")
    post_heatmap_to_discord(results_day, "Heat Map Day")
