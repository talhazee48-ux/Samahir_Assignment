# Question 1 - Machine Learning
# UCI Heart Disease - Cleveland Dataset

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("Final_Assignment/heart_disease_cleveland.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df.isnull().sum())

df["ca"] = df["ca"].fillna(df["ca"].median())
df["thal"] = df["thal"].fillna(df["thal"].median())

print(df["target"].value_counts())

sns.countplot(data=df, x="target")
plt.title("Heart Disease Distribution")
plt.show()

sns.histplot(data=df, x="age", hue="target", kde=True)
plt.title("Age and Heart Disease")
plt.show()

sns.boxplot(data=df, x="target", y="chol")
plt.title("Cholesterol by Heart Disease")
plt.show()

sns.scatterplot(data=df, x="age", y="thalach", hue="target")
plt.title("Age vs Maximum Heart Rate")
plt.show()

plt.figure(figsize=(10, 7))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Heart Disease Correlation")
plt.show()

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

log_model = LogisticRegression(max_iter=1000)
tree_model = DecisionTreeClassifier(max_depth=5, random_state=42)
forest_model = RandomForestClassifier(n_estimators=100, random_state=42)

log_model.fit(X_train, y_train)
tree_model.fit(X_train, y_train)
forest_model.fit(X_train, y_train)

log_pred = log_model.predict(X_test)
tree_pred = tree_model.predict(X_test)
forest_pred = forest_model.predict(X_test)

print("Logistic Regression Accuracy:",
      accuracy_score(y_test, log_pred))

print("Decision Tree Accuracy:",
      accuracy_score(y_test, tree_pred))

print("Random Forest Accuracy:",
      accuracy_score(y_test, forest_pred))

print("\nLogistic Regression")
print(classification_report(y_test, log_pred))

print("\nDecision Tree")
print(classification_report(y_test, tree_pred))

print("\nRandom Forest")
print(classification_report(y_test, forest_pred))

cm = confusion_matrix(y_test, forest_pred)

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()