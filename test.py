import pandas as pd
import numpy as np

dataframe1 = pd.read_csv("cols.csv")
dataframe2 = pd.read_csv("data.csv")

dataframe =  pd.DataFrame()

# print(dataframe1)
# print(dataframe2.head())
col = []
for item in dataframe1["column_name"]:
	col.append(item)

dataframe2.columns = col
print(dataframe2.columns)