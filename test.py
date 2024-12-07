import csv
import pandas as pd
# Define the new rows to append
new_rows = [
    ["Emily", "Clark", 29, "emily.clark@example.com"],
    ["Michael", "Johnson", 31, "michael.johnson@example.com"]
]

# Open the file in append mode and write the new rows
file_path = "baku_aqi.csv" 
# Replace with your file path

df = pd.read_csv(file_path)

# Get the index of the last column


print(len(df))

# Save the updated DataFrame to a new CSV file


