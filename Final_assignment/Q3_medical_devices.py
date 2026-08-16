# Question 3 - Deep Learning
# FDA AI Medical Devices Authorizations & Recalls

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Dense

df = pd.read_csv("Final_Assignment/fda_ai_medical_devices.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

df["final_decision_date"] = pd.to_datetime(df["final_decision_date"])

monthly = (
    df.groupby(df["final_decision_date"].dt.to_period("M"))
    .size()
    .reset_index(name="authorizations")
)

monthly["final_decision_date"] = monthly["final_decision_date"].dt.to_timestamp()

print(monthly.head())
print(monthly.tail())

sns.lineplot(data=monthly, x="final_decision_date", y="authorizations")
plt.title("FDA AI Medical Device Authorizations Over Time")
plt.xticks(rotation=45)
plt.show()

sns.histplot(data=monthly, x="authorizations", kde=True)
plt.title("Monthly Authorization Distribution")
plt.show()

sns.boxplot(data=monthly, y="authorizations")
plt.title("Monthly Authorization Spread")
plt.show()

values = monthly["authorizations"].values.astype(float)

scaler = MinMaxScaler()
scaled = scaler.fit_transform(values.reshape(-1, 1))

look_back = 12

X = []
y = []

for i in range(look_back, len(scaled)):
    X.append(scaled[i-look_back:i, 0])
    y.append(scaled[i, 0])

X = np.array(X)
y = np.array(y)

split = int(len(X) * 0.8)

X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))


# RNN Model

rnn = Sequential([
    SimpleRNN(32, activation="tanh", input_shape=(look_back, 1)),
    Dense(1)
])

rnn.compile(optimizer="adam", loss="mse")

rnn.fit(X_train, y_train, epochs=30, batch_size=8, verbose=0)

rnn_pred = rnn.predict(X_test, verbose=0)


# LSTM Model

lstm = Sequential([
    LSTM(32, activation="tanh", input_shape=(look_back, 1)),
    Dense(1)
])

lstm.compile(optimizer="adam", loss="mse")

lstm.fit(X_train, y_train, epochs=30, batch_size=8, verbose=0)

lstm_pred = lstm.predict(X_test, verbose=0)


# GRU Model

gru = Sequential([
    GRU(32, activation="tanh", input_shape=(look_back, 1)),
    Dense(1)
])

gru.compile(optimizer="adam", loss="mse")

gru.fit(X_train, y_train, epochs=30, batch_size=8, verbose=0)

gru_pred = gru.predict(X_test, verbose=0)


# Convert Predictions Back

actual = scaler.inverse_transform(y_test.reshape(-1, 1))

rnn_pred = scaler.inverse_transform(rnn_pred)
lstm_pred = scaler.inverse_transform(lstm_pred)
gru_pred = scaler.inverse_transform(gru_pred)


# Model Metrics

models = {
    "RNN": rnn_pred,
    "LSTM": lstm_pred,
    "GRU": gru_pred
}

for name, pred in models.items():
    mae = mean_absolute_error(actual, pred)
    rmse = np.sqrt(mean_squared_error(actual, pred))

    print("\n", name)
    print("MAE:", mae)
    print("RMSE:", rmse)


# Compare Predictions

comparison = pd.DataFrame({
    "Actual": actual.flatten(),
    "RNN": rnn_pred.flatten(),
    "LSTM": lstm_pred.flatten(),
    "GRU": gru_pred.flatten()
})

print(comparison.tail(10))


# Prediction Comparison

plt.figure(figsize=(12, 6))
plt.plot(comparison["Actual"], label="Actual")
plt.plot(comparison["RNN"], label="RNN")
plt.plot(comparison["LSTM"], label="LSTM")
plt.plot(comparison["GRU"], label="GRU")
plt.title("RNN vs LSTM vs GRU Predictions")
plt.legend()
plt.show()