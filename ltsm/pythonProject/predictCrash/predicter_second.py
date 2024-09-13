import numpy as np
from keras import Sequential
from keras.src.callbacks import EarlyStopping
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam


def create_sequences(data, n_past):
    X, y = [], []
    for i in range(len(data) - n_past):
        X.append(data[i:(i + n_past)])
        y.append(data[i + n_past])
    return np.array(X), np.array(y)


def predict_next_result2(data, n_past=10):
    scaler = StandardScaler()
    data_scaled =  scaler.fit_transform(np.array(data).reshape(-1, 1))

    X, y = create_sequences(data_scaled, n_past)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=(n_past, 1)),
        Dropout(0.2),
        LSTM(32, return_sequences=False),
        Dropout(0.2),
        Dense(16, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

    early_stop = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)

    model.fit(X_train, y_train, validation_data=(X_test, y_test),
              epochs=500, batch_size=32, verbose=0,
              callbacks=[early_stop])

    # Evaluate the model
    test_loss = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss: {test_loss}")

    last_sequence = data_scaled[-n_past:].reshape(1, n_past, 1)
    next_result = model.predict(last_sequence)
    return scaler.inverse_transform(next_result)[0][0]




def predict_next_result4(data, n_past=10):
    data_scaled = np.array(data).reshape(-1, 1)

    X, y = create_sequences(data_scaled, n_past)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=(n_past, 1)),
        Dropout(0.2),
        LSTM(32, return_sequences=False),
        Dropout(0.2),
        Dense(16, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

    early_stop = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)

    model.fit(X_train, y_train, validation_data=(X_test, y_test),
              epochs=500, batch_size=32, verbose=0,
              callbacks=[early_stop])

    # Evaluate the model
    test_loss = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss: {test_loss}")

    last_sequence = data_scaled[-n_past:].reshape(1, n_past, 1)
    next_result = model.predict(last_sequence)
    return next_result[0][0]