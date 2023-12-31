import pandas as pd

df = pd.read_csv('movie_preprocessing.csv',low_memory=False)
def change_value(value):
    return str(value).replace(' ','_')

df['genres'] = df['genres'].apply(change_value)
df['original_language'] = df['original_language'].apply(change_value)
df['production_companies'] = df['production_companies'].apply(change_value)
df['production_countries'] =df['production_countries'].apply(change_value)
df['belongs_to_collection']  =df['belongs_to_collection'].apply(change_value)
df['cast'] = df ['cast'].apply(change_value)
df['crew'] = df ['crew'].apply(change_value)
df['keywords'] = df ['keywords'].apply(change_value)


df.to_csv('filter.csv')