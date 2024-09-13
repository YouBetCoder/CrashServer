import numpy as np
from keras import Sequential
from keras.src.callbacks import EarlyStopping
from keras.src.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

from predictCrash.settings import n_past


def predict_next_result(data):

    X_train = []
    y_train = []
    n_future = 30
    #scaler = MinMaxScaler(feature_range=(1, 16))
    #data = np.array(data).reshape(-1, 1)
    #data = scaler.fit_transform(data)
    for i in range(n_past, len(data) - n_future + 1):
        X_train.append(data[i - n_past:i])
        y_train.append(data[i + n_future - 1:i + n_future])
    X_train, y_train = np.array(X_train, dtype=np.float32), np.array(y_train, dtype=np.float32)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(n_past, 1)))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    early_stop = EarlyStopping(monitor='loss', patience=3)
    model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=0, callbacks=[early_stop])
    x = data[-n_past:]
    x = np.array(x).reshape((1, n_past, 1))
    next_result = model.predict(x)
    return next_result
