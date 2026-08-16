# Question 4 - Deep Learning
# Oregon Hospital Data

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Dense

df = pd.read_csv("Final_Assignment/OR_hos_prices1.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

df = df.drop(columns=["Unnamed: 0"])

num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

print(df.isnull().sum().sum())

sns.histplot(data=df, x="X-ray: Chest", kde=True)
plt.title("X-ray Chest Price Distribution")
plt.show()

sns.histplot(data=df, x="X-ray: Extremities", kde=True)
plt.title("X-ray Extremities Distribution")
plt.show()

sns.scatterplot(data=df, x="X-ray: Chest", y="X-ray: Extremities")
plt.title("Chest X-ray vs Extremities X-ray")
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(
    df[["X-ray: Chest", "X-ray: Extremities",
        "Ultrasound", "Colonoscopy",
        "MRI: Spine"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Hospital Procedure Correlation")
plt.show()

features = [
    "X-ray: Chest",
    "X-ray: Extremities",
    "Ultrasound",
    "X-ray: Spine",
    "Cardiovascular: Electrocardiography",
    "Colonoscopy",
    "Cardiovascular: Echocardiography",
    "Ultrasound: Obstetrical",
    "MRI: Spine",
    "CT scan with contrast: Abdomen/GI",
    "Mammography",
    "CT scan: Chest"
]

data = df[features].values

scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)

X = []
y = []

for row in scaled:
    X.append(row[:-1])
    y.append(row[-1])

X = np.array(X)
y = np.array(y)

split = int(len(X) * 0.8)

X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)


# RNN

rnn = Sequential([
    SimpleRNN(32, activation="tanh", input_shape=(X_train.shape[1], 1)),
    Dense(1)
])

rnn.compile(optimizer="adam", loss="mse")

rnn.fit(X_train, y_train, epochs=30, batch_size=8, verbose=0)

rnn_pred = rnn.predict(X_test, verbose=0)


# LSTM

lstm = Sequential([
    LSTM(32, activation="tanh", input_shape=(X_train.shape[1], 1)),
    Dense(1)
])

lstm.compile(optimizer="adam", loss="mse")

lstm.fit(X_train, y_train, epochs=30, batch_size=8, verbose=0)

lstm_pred = lstm.predict(X_test, verbose=0)


# GRU

gru = Sequential([
    GRU(32, activation="tanh", input_shape=(X_train.shape[1], 1)),
    Dense(1)
])

gru.compile(optimizer="adam", loss="mse")

gru.fit(X_train, y_train, epochs=30, batch_size=8, verbose=0)

gru_pred = gru.predict(X_test, verbose=0)


# Metrics

models = {
    "RNN": rnn_pred,
    "LSTM": lstm_pred,
    "GRU": gru_pred
}

for name, pred in models.items():

    mae = mean_absolute_error(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))

    print("\n", name)
    print("MAE:", mae)
    print("RMSE:", rmse)


# Prediction Comparison

results = pd.DataFrame({
    "Actual": y_test,
    "RNN": rnn_pred.flatten(),
    "LSTM": lstm_pred.flatten(),
    "GRU": gru_pred.flatten()
})

print(results)

plt.figure(figsize=(10,6))

plt.plot(results["Actual"], label="Actual")
plt.plot(results["RNN"], label="RNN")
plt.plot(results["LSTM"], label="LSTM")
plt.plot(results["GRU"], label="GRU")

plt.title("RNN vs LSTM vs GRU")
plt.xlabel("Hospital")
plt.ylabel("Scaled Procedure Price")
plt.legend()
plt.show()