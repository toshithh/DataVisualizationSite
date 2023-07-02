import pandas as pd

x = pd.read_json("assignment/jsondata.json")
x.to_csv("assignment/data.csv")