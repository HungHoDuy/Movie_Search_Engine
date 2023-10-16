import pandas as pd
from dataAdd import dataAdd_df

def popularity_df(keyword):
    df = dataAdd_df(keyword)
    df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
    df = df.sort_values(by='popularity', ascending=False)
    return df

popularity_df('batman').to_csv('sample.csv')