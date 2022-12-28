import os
import pandas as pd 

def get_file(filename):
    return pd.read_csv(filename)

filename = "test.csv"
data = get_file(filename)
print(data.shape)