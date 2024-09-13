import decimal

import pandas as pd
from prophet import Prophet

from predictCrash.kalman import predict_next_kalman


def predict_next_result_prophet2(data, periods=1):
    for i in range(len(data)):
        if data[i] > 10:
            data[i] = 0

    # Convert data to DataFrame
    df = pd.DataFrame({'ds': pd.date_range(start='2021-01-01', periods=len(data)), 'y': data})

    # Initialize and fit the Prophet model
    model = Prophet(daily_seasonality=True)
    model.fit(df)

    # Create future dataframe for prediction
    future = model.make_future_dataframe(periods=periods)

    # Make prediction
    forecast = model.predict(future)

    # Return the last predicted value
    predicted = forecast['yhat'].iloc[-1]
    return decimal.Decimal(predicted)


def predict_next_result_prophet(data, periods=1):
    # Convert data to DataFrame
    df = pd.DataFrame({'ds': pd.date_range(start='2021-01-01', periods=len(data)), 'y': data})

    # Initialize and fit the Prophet model
    model = Prophet(daily_seasonality=True)
    model.fit(df)

    # Create future dataframe for prediction
    future = model.make_future_dataframe(periods=periods)

    # Make prediction
    forecast = model.predict(future)

    # Return the last predicted value
    predicted = forecast['yhat'].iloc[-1]
    return decimal.Decimal(predicted)


# Example usage
