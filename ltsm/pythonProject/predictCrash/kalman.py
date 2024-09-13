import numpy as np


class KalmanFilter:
    def __init__(self, initial_state, initial_estimate_error, process_variance, measurement_variance):
        self.state = initial_state
        self.estimate_error = initial_estimate_error
        self.process_variance = process_variance
        self.measurement_variance = measurement_variance

    def predict(self):
        # State transition (assuming constant state)
        self.state = self.state
        # Error in estimate
        self.estimate_error = self.estimate_error + self.process_variance

    def update(self, measurement):
        # Kalman gain
        kalman_gain = self.estimate_error / (self.estimate_error + self.measurement_variance)
        # Update state estimate
        self.state = self.state + kalman_gain * (measurement - self.state)
        # Update estimate error
        self.estimate_error = (1 - kalman_gain) * self.estimate_error

    def get_state(self):
        return self.state


def predict_next_kalman(data, n_predictions=1):
    # Initialize Kalman filter
    initial_state = data[0]
    initial_estimate_error = 1
    process_variance = np.var(np.diff(data)) # Variance of differences
    measurement_variance = np.var(data)

    kf = KalmanFilter(initial_state, initial_estimate_error, process_variance, measurement_variance)

    # Update Kalman filter with historical data
    for measurement in data:
        kf.predict()
        kf.update(measurement)

    # Predict next n values
    predictions = []
    for _ in range(n_predictions):
        kf.predict()
        predictions.append(kf.get_state())

    return predictions
