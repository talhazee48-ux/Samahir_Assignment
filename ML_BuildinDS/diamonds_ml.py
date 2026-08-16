# Diamonds Dataset
# Hugging Face

import pandas as pd
from datasets import load_dataset

dataset = load_dataset("mstz/diamonds", "cut")

df = dataset["train"].to_pandas()

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df.isnull().sum())

df.to_csv("diamonds_ml.csv", index=False)

print("CSV file created successfully")
print("Rows:", len(df))