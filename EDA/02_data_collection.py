"""
Data Collection in EDA
Loading data from various sources like CSV, Excel, and JSON.
"""

import pandas as pd
import sqlite3

# Load CSV file
df_csv = pd.read_csv("C:/Users/asnav/Desktop/DataScience/EDA/files/sample.csv")
print("CSV Data Sample:\n", df_csv.head())

# Load Excel file
df_excel = pd.read_excel("C:/Users/asnav/Desktop/DataScience/EDA/files/sample.xlsx")
print("\nExcel Data Sample:\n", df_excel.head())

# Load JSON file
df_json = pd.read_json("C:/Users/asnav/Desktop/DataScience/EDA/files/sample.json")
print("\nJSON Data Sample:\n", df_json.head())


# Path to the database
db_path = "C:/Users/asnav/Desktop/DataScience/EDA/files/sample.db"

# Connect to the database
conn = sqlite3.connect(db_path)

# Check available tables
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Available Tables in Database:\n", tables)

# Fetch data from 'users' table
df_sql = pd.read_sql("SELECT * FROM users", conn)
conn.close()

# Display data
print("\nSQL Database Data Sample:\n", df_sql)