import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
from dotenv import load_dotenv

load_dotenv()
from get_all_game_results import get_all_game_results

results = get_all_game_results()
# Assuming 'results' is your list of ActiveGameResult objects
# Convert the list of objects to a DataFrame
df = pd.DataFrame([
    {
        'game_result': float(r.game_result),
        'timestamp': datetime.fromtimestamp(r.time_recorded, tz=pytz.UTC),
        'round_id': r.active_game_room_round_id
    } for r in results
])

# Sort the DataFrame by timestamp
df = df.sort_values('timestamp')

# Extract UTC hour and day of week
df['hour_utc'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek

# Filter for high numbers and group by hour and day
high_numbers = df[df['game_result'] > 60]
high_numbers_by_hour = high_numbers.groupby('hour_utc').size()
high_numbers_by_day = high_numbers.groupby('day_of_week').size()

# Create the plot
plt.figure(figsize=(16, 6))

# Subplot for high numbers by hour
plt.subplot(1, 2, 1)
high_numbers_by_hour.plot(kind='bar')
plt.title('High Numbers (>60) by Hour (UTC)')
plt.xlabel('Hour of Day (UTC)')
plt.ylabel('Count')
plt.xticks(range(0, 24, 2))  # Show every other hour for readability

# Subplot for high numbers by day of week
plt.subplot(1, 2, 2)
high_numbers_by_day.plot(kind='bar')
plt.title('High Numbers (>60) by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Count')
plt.xticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

plt.tight_layout()
plt.show()

# Print summary statistics
print(f"Total high numbers (>60): {len(high_numbers)}")
print(f"Most common UTC hour for high numbers: {high_numbers_by_hour.idxmax()} ({high_numbers_by_hour.max()} occurrences)")
print(f"Most common day for high numbers: {['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][high_numbers_by_day.idxmax()]} ({high_numbers_by_day.max()} occurrences)")