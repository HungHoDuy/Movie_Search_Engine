import pandas as pd
from data_filter import DataFilter
import ast

def cast_name(data_str):
    data_list = ast.literal_eval(str(data_str))
    names = '+'.join(item['name'] for item in data_list)
    return names

def genres_name(data_str):
    data_list = eval(str(data_str))
    names = '+'.join(item['name'] for item in data_list)
    return names

def find_name(data_inp):
    data_str = str(data_inp)
    start = data_str.find("'name': '") + len("'name': '")
    end = data_str.find("'", start)
    return data_str[start:end]

def find_director(data_str):
    start_index = data_str.find("'job': 'Director', 'name': '") + len("'job': 'Director', 'name': '")
    end_index = data_str.find("'", start_index)
    return data_str[start_index:end_index]

def dataAdd(keyword):
    df = DataFilter(keyword)

    credit_file_links = '/home/chunporo/Documents/GitHub/Movie_Search_Engine/data/credits.csv'
    keyword_file_links = '/home/chunporo/Documents/GitHub/Movie_Search_Engine/data/keywords.csv'

    credits_df = pd.read_csv(credit_file_links, low_memory=False)
    keyword_df = pd.read_csv(keyword_file_links)

    df['id'] = df['id'].astype(str)
    credits_df['id'] = credits_df['id'].astype(str)
    keyword_df['id'] = keyword_df['id'].astype(str)

    df = pd.merge(df, credits_df, on='id', how='inner')
    df = pd.merge(df, keyword_df, on='id', how='inner')
    df['cast'] = df['cast'].apply(cast_name)
    df['keywords'] = df['keywords'].apply(cast_name)
    # print(df.belongs_to_collection.values[0])
    df['belongs_to_collection'] = df['belongs_to_collection'].apply(find_name)
    df['crew'] = df['crew'].apply(find_director)
    df['genres'] = df['genres'].apply(genres_name)
    df['production_companies'] = df['production_companies'].apply(genres_name)
    df['production_countries'] = df['production_countries'].apply(genres_name)
    df['spoken_languages'] = df['spoken_languages'].apply(genres_name)
    # print(credits_df.cast.values[0])
    df.to_csv('sample.csv')
dataAdd('batman')