from dotenv import load_dotenv

from get_all_game_results import get_all_game_results
from time_plots import plot_time, plot_time_2

load_dotenv()

results = get_all_game_results()
plot_time_2(results)
