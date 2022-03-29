import pandas as pd

introverts_dict = pd.read_csv("Datasets/introverts_df.csv")
extroverts_dict = pd.read_csv("Datasets/extroverts_df.csv")

print(introverts_dict.head())
print(extroverts_dict.head())