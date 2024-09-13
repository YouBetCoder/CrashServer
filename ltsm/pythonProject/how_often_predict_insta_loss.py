import pandas as pd
import numpy as np

import data_for_charts

# Sample data structure based on your input
data_charts = data_for_charts.data_charts

# Create DataFrame from data_charts and apply floor function
df = pd.DataFrame(data_charts)

# Filter rows where gameResult is under 2
df_under_2 = df[df['gameResult'] < 2]

# Calculate percentage for prediction4
percent_pred4_under_2 = (df_under_2['prediction4'] < 2).mean() * 100

# Calculate percentage for predictionArima
percent_pred_arima_under_2 = (df_under_2['predictionArima'] < 2).mean() * 100

# Output the results
print(f"Percentage of times Prediction4 was under 2 when GameResult was under 2: {percent_pred4_under_2:.2f}%")
print(f"Percentage of times PredictionArima was under 2 when GameResult was under 2: {percent_pred_arima_under_2:.2f}%")
df_over_2 = df[df['gameResult'] > 2]

# Calculate percentage for prediction4
percent_pred4_over_2 = (df_over_2['prediction4'] > 2).mean() * 100

# Calculate percentage for predictionArima
percent_pred_arima_over_2 = (df_over_2['predictionArima'] > 2).mean() * 100

# Output the results
print(f"Percentage of times Prediction4 was over 2 when GameResult was over 2: {percent_pred4_over_2:.2f}%")
print(f"Percentage of times PredictionArima was over 2 when GameResult was over 2: {percent_pred_arima_over_2:.2f}%")