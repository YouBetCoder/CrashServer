import decimal

import statsmodels.api as sm
import pandas as pd


def predict_next_decimal_arima(data):
    """Predicts the next decimal in a sequence using ARIMA.

    Args:
      data: A list of decimals.

    Returns:
      The predicted next decimal.
    """

    # Create a pandas Series
    series = pd.Series(data)

    # Check stationarity
    result = sm.tsa.stattools.adfuller(series)
    if result[1] > 0.05:  # Not stationary
        series = series.diff().dropna()

    # Model identification (adjust p, d, q based on ACF/PACF)
    p = 1  # Example
    d = 1 if result[1] > 0.05 else 0  # Differencing order
    q = 1  # Example

    # Model estimation
    model = sm.tsa.ARIMA(series, order=(p, d, q))
    results = model.fit()

    # Forecast the next decimal
    forecast = results.forecast(steps=1)

    return decimal.Decimal(float(forecast.values[0]))
