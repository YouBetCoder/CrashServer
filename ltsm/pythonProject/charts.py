from data_for_charts import data_charts

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

# Sample data structure based on your input
data_charts = data_charts


# Create DataFrame from data_charts and apply floor function
df = pd.DataFrame(data_charts).applymap(np.floor)

# Line plot for gameResult and predictions over time
plt.figure(figsize=(10, 6))

# Plotting each column as a line
plt.plot(df.index, df['gameResult'], label='Game Result', marker='o', color='black', linestyle='--')
#plt.plot(df.index, df['prediction'], label='Prediction', marker='o', color='blue')
#plt.plot(df.index, df['prediction2'], label='Prediction 2', marker='o', color='green')
plt.plot(df.index, df['prediction4'], label='Prediction 4', marker='o', color='orange')
plt.plot(df.index, df['predictionArima'], label='Prediction Arima', marker='o', color='red')

# Adding title and labels
plt.title('Game Result and Predictions Over Time')
plt.xlabel('Time (Data Points)')
plt.ylabel('Values')

# Displaying legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()