import numpy as np
import tensorflow as tf
from keras import Sequential
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2


def create_sequences(data, n_past):
    X, y = [], []
    for i in range(len(data) - n_past):
        X.append(data[i:(i + n_past)])
        y.append(data[i + n_past])
    return np.array(X), np.array(y)


def custom_loss(y_true, y_pred):
    mse = tf.keras.losses.MeanSquaredError()(y_true, y_pred)
    mae = tf.keras.losses.MeanAbsoluteError()(y_true, y_pred)
    return mse + 0.5 * mae


def predict_next_result3(data, n_past=30):
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(np.array(data).reshape(-1, 1))


    model = Sequential([
        LSTM(128, return_sequences=True, input_shape=(n_past, 1), kernel_regularizer=l2(0.01)),
        Dropout(0.3),
        LSTM(64, return_sequences=True, kernel_regularizer=l2(0.01)),
        Dropout(0.3),
        LSTM(32, return_sequences=False, kernel_regularizer=l2(0.01)),
        Dropout(0.3),
        Dense(16, activation='relu', kernel_regularizer=l2(0.01)),
        Dense(1)
    ])

    model.compile(optimizer=Adam(learning_rate=0.001), loss=custom_loss)

    last_sequence = data_scaled[-n_past:].reshape(1, n_past, 1)
    next_result = model.predict(last_sequence)
    return scaler.inverse_transform(next_result)[0][0]
