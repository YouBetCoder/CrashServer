import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import data_for_charts

# Sample data structure based on your input
data_charts = data_for_charts.data_charts

# Create DataFrame from data_charts and apply floor function
df = pd.DataFrame(data_charts).applymap(np.floor)

# Plot all columns as a time series
plt.figure(figsize=(10, 6))

# Plot each column on the same line graph
plt.plot(df.index, df['gameResult'], marker='o', label='GameResult', color='black', linestyle='--')
# plt.plot(df.index, df['prediction'], marker='o', label='Prediction', color='blue')
# plt.plot(df.index, df['prediction2'], marker='o', label='Prediction2', color='green')
plt.plot(df.index, df['prediction4'], marker='o', label='Prediction4', color='orange')
plt.plot(df.index, df['predictionArima'], marker='o', label='PredictionArima', color='red')

# Adding labels and title
plt.title('GameResult and Predictions Over Time')
plt.xlabel('Time (Index)')
plt.ylabel('Values (Floored)')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
