
# Question 2 - Machine Learning
# USA Hospitals Dataset

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("Final_Assignment/Hospitals.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

df = df.replace("NOT AVAILABLE", np.nan)

print(df.isnull().sum())

df["POPULATION"] = pd.to_numeric(df["POPULATION"], errors="coerce")
df["BEDS"] = pd.to_numeric(df["BEDS"], errors="coerce")
df["TTL_STAFF"] = pd.to_numeric(df["TTL_STAFF"], errors="coerce")

df = df.replace(-999, np.nan)

df["POPULATION"] = df["POPULATION"].fillna(df["POPULATION"].median())
df["BEDS"] = df["BEDS"].fillna(df["BEDS"].median())
df["TTL_STAFF"] = df["TTL_STAFF"].fillna(df["TTL_STAFF"].median())

print(df[["POPULATION", "BEDS", "TTL_STAFF"]].describe())

sns.histplot(data=df, x="BEDS", kde=True)
plt.title("Hospital Beds Distribution")
plt.show()

sns.histplot(data=df, x="POPULATION", kde=True)
plt.title("Hospital Population Distribution")
plt.show()

sns.scatterplot(data=df, x="POPULATION", y="BEDS", hue="STATUS")
plt.title("Population and Hospital Beds")
plt.show()

sns.boxplot(data=df, x="STATUS", y="BEDS")
plt.title("Beds by Hospital Status")
plt.show()

sns.countplot(data=df, y="TYPE",
              order=df["TYPE"].value_counts().head(10).index)
plt.title("Hospital Types")
plt.show()

sns.heatmap(
    df[["POPULATION", "BEDS", "TTL_STAFF", "LATITUDE", "LONGITUDE"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Hospital Data Correlation")
plt.show()

X = df[["POPULATION", "TTL_STAFF", "LATITUDE", "LONGITUDE"]]
y = df["BEDS"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

linear_model = LinearRegression()
forest_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

linear_model.fit(X_train, y_train)
forest_model.fit(X_train, y_train)

linear_pred = linear_model.predict(X_test)
forest_pred = forest_model.predict(X_test)

print("Linear Regression")
print("MAE:", mean_absolute_error(y_test, linear_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, linear_pred)))
print("R2:", r2_score(y_test, linear_pred))

print("\nRandom Forest")
print("MAE:", mean_absolute_error(y_test, forest_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, forest_pred)))
print("R2:", r2_score(y_test, forest_pred))

results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": forest_pred
})

print(results.head(10))

sns.scatterplot(data=results, x="Actual", y="Predicted")
plt.title("Actual vs Predicted Hospital Beds")
plt.show()