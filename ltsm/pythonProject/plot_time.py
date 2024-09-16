from dotenv import load_dotenv

from get_all_game_results import get_all_game_results, get_unix_time_stamp_days_ago
from time_plots import plot_time, plot_time_2

load_dotenv()
one_day_ago = get_unix_time_stamp_days_ago(1)
one_week_ago = get_unix_time_stamp_days_ago(7)
one_month_ago = get_unix_time_stamp_days_ago(30)
results = get_all_game_results(one_week_ago)
results_day = get_all_game_results(one_day_ago)
results_month = get_all_game_results(one_month_ago)

plot_time(results)
