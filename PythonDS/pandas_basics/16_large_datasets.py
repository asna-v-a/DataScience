"""
Handling Large Datasets Efficiently
"""
import pandas as pd

chunk_size = 10000
for chunk in pd.read_csv("C:/Users/asnav/Desktop/DataScience/PythonDS/pandas_basics/files/heart.csv", chunksize=chunk_size):
    print(chunk.head())  # Process in chunks
