import pandas as pd

data = {
    'timestamp': ['2022-04-30T00:00:00', '2022-04-30T01:00:00', '2022-04-30T02:00:00'],
    'aqi': [27, 26, 25]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nData types:")
print(df.dtypes)

df['timestamp'] = pd.to_datetime(df['timestamp'])
print("\nDataFrame after conversion:")
print(df)
print("\nNew data types:")
print(df.dtypes)