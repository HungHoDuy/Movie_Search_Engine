from ast import literal_eval
import numpy as np
import pandas as pd
from data_filter import DataFilter

def rating_df(keyword):
    df = DataFilter(keyword)
    df.to_csv('input.csv')
    vote_counts = df[df['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = df[df['vote_average'].notnull()]['vote_average'].astype('int')
    C = 5.244896612406511
    m = 434.0


    def convert_to_list(data_str):
        return data_str.split('+')
    df['genres'] = df['genres'].apply(convert_to_list)
    qualified = df[(df['vote_count'] >= m) & (df['vote_count'].notnull()) & (df['vote_average'].notnull())][['title', 'year', 'vote_count', 'vote_average', 'popularity', 'genres']]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')

    def weighted_rating(x):
        v = x['vote_count']
        R = x['vote_average']
        return (v / (v + m) * R) + (m / (m + v) * C)

    qualified['score'] = qualified.apply(weighted_rating, axis=1)
    qualified = qualified.sort_values('score', ascending=False).head(df.shape[1])
    df = df.reindex(qualified.index)
    def genres_to_str(data_list):
        return '+'.join(item for item in data_list)
    df['genres'] = df['genres'].apply(genres_to_str)
    
    return df

# rating_df('+romance').to_csv('sample.csv')
