from datetime import datetime

import pandas as pd
import pytz
import seaborn as sns
from matplotlib import pyplot as plt


def plot_time_2(results):
    # Assuming 'results' is your list of ActiveGameResult objects
    # Convert the list of objects to a DataFrame
    df = pd.DataFrame([
        {
            'game_result': float(r.game_result),
            'timestamp': datetime.fromtimestamp(r.time_recorded),
            'round_id': r.active_game_room_round_id
        } for r in results
    ])

    # Sort the DataFrame by timestamp
    df = df.sort_values('timestamp')

    # Add time-based columns
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    df['month'] = df['timestamp'].dt.month
    df['week_of_year'] = df['timestamp'].dt.isocalendar().week

    # 1. Enhanced Heatmap: Game Result Distribution by Hour and Day of Week
    pivot = df.pivot_table(
        values='game_result',
        index=df['timestamp'].dt.hour,
        columns=df['timestamp'].dt.dayofweek,
        aggfunc='mean'
    )

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot, cmap='YlOrRd', annot=True, fmt='.2f')
    plt.title('Average Game Result by Hour and Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Hour of Day')
    plt.show()

    # 2. High Numbers by Hour (Enhanced)
    high_numbers = df[df['game_result'] > 60]
    plt.figure(figsize=(12, 6))
    sns.countplot(data=high_numbers, x='hour', palette='viridis')
    plt.title('Distribution of High Numbers (>60) by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Count of High Numbers')
    plt.show()

    # 3. Monthly Trend of High Numbers
    monthly_high_numbers = high_numbers.groupby('month').size().reset_index(name='count')
    plt.figure(figsize=(12, 6))
    sns.barplot(data=monthly_high_numbers, x='month', y='count', palette='coolwarm')
    plt.title('Monthly Trend of High Numbers (>60)')
    plt.xlabel('Month')
    plt.ylabel('Count of High Numbers')
    plt.show()

    # 4. Weekly Trend of High Numbers
    weekly_high_numbers = high_numbers.groupby('week_of_year').size().reset_index(name='count')
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=weekly_high_numbers, x='week_of_year', y='count', marker='o')
    plt.title('Weekly Trend of High Numbers (>60)')
    plt.xlabel('Week of Year')
    plt.ylabel('Count of High Numbers')
    plt.show()

    # 5. Distribution of Game Results
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x='game_result', kde=True, bins=30)
    plt.title('Distribution of Game Results')
    plt.xlabel('Game Result')
    plt.ylabel('Frequency')
    plt.axvline(x=60, color='r', linestyle='--', label='Threshold (60)')
    plt.legend()
    plt.show()

    # 6. Box Plot of Game Results by Day of Week
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='day_of_week', y='game_result')
    plt.title('Distribution of Game Results by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Game Result')
    plt.axhline(y=60, color='r', linestyle='--', label='Threshold (60)')
    plt.legend()
    plt.show()


def plot_time(results):
    # Assuming 'results' is your list of ActiveGameResult objects
    # Convert the list of objects to a DataFrame
    df = pd.DataFrame([
        {
            'game_result': float(r.game_result),
            'timestamp': datetime.fromtimestamp(r.time_recorded, tz=pytz.UTC),
            'round_id': r.round_id
        } for r in results
    ])

    # Sort the DataFrame by timestamp
    df = df.sort_values('timestamp')



    # 2. Statistical summary
    high_numbers = df[df['game_result'] > 10]
    print(f"Frequency of numbers > 10: {len(high_numbers)} out of {len(df)} ({len(high_numbers) / len(df) * 100:.2f}%)")
    avg_time_between = (high_numbers['timestamp'].diff().mean().total_seconds() / 60)
    print(f"Average time between high numbers: {avg_time_between:.2f} minutes")

    # 3. Time-based clustering
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    high_numbers_by_hour = df[df['game_result'] > 10].groupby('hour').size()
    high_numbers_by_day = df[df['game_result'] > 10].groupby('day_of_week').size()

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    high_numbers_by_hour.plot(kind='bar')
    plt.title('High Numbers by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Count')

    plt.subplot(1, 2, 2)
    high_numbers_by_day.plot(kind='bar')
    plt.title('High Numbers by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

