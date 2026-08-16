# California Housing Dataset
# Hugging Face

import pandas as pd
from datasets import load_dataset

dataset = load_dataset("gvlassis/california_housing")

train = dataset["train"].to_pandas()
validation = dataset["validation"].to_pandas()
test = dataset["test"].to_pandas()

df = pd.concat(
    [train, validation, test],
    ignore_index=True
)

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df.isnull().sum())

df.to_csv("california_housing_ml.csv", index=False)

print("CSV file created successfully")
print("Rows:", len(df))