import pandas as pd

df =  pd.read_csv('predictions.csv')
df = df.iloc[3:]
df.to_csv('predictions.csv',index=False)