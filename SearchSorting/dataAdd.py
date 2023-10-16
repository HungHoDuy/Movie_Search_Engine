import pandas as pd
from data_filter import DataFilter
import ast
import numpy as np
import requests
import json

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

def dataAdd_df(keyword):
    df = DataFilter(keyword)

    credit_file_links = '/home/chunporo/Documents/GitHub/Movie_Search_Engine/data/credits.csv'
    keyword_file_links = '/home/chunporo/Documents/GitHub/Movie_Search_Engine/data/keywords.csv'
    link_file_links = '/home/chunporo/Documents/GitHub/Movie_Search_Engine/data/links.csv'

    credits_df = pd.read_csv(credit_file_links, low_memory=False)
    keyword_df = pd.read_csv(keyword_file_links)
    link_df = pd.read_csv(link_file_links)

    df['id'] = df['id'].astype(str)
    credits_df['id'] = credits_df['id'].astype(str)
    keyword_df['id'] = keyword_df['id'].astype(str)
    link_df['id'] = keyword_df['id'].astype(str)

    df = pd.merge(df, credits_df, on='id', how='inner')
    df = pd.merge(df, keyword_df, on='id', how='inner')
    df = pd.merge(df, link_df, on='id', how='inner')
    df.to_csv('sample.csv')
    df['cast'] = df['cast'].apply(cast_name)
    df['keywords'] = df['keywords'].apply(cast_name)
    # print(df.belongs_to_collection.values[0])
    df['belongs_to_collection'] = df['belongs_to_collection'].apply(find_name)
    df['crew'] = df['crew'].apply(find_director)
    df['genres'] = df['genres'].apply(genres_name)
    df['production_companies'] = df['production_companies'].apply(genres_name)
    df['production_countries'] = df['production_countries'].apply(genres_name)
    df['spoken_languages'] = df['spoken_languages'].apply(genres_name)
    df['year'] = pd.to_datetime(df['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
    def poster_find(movie_id):
        target_ur = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c2c3992b8ca4966ce0e58aa69429fafe"
        resp = requests.get(target_ur)
        if resp.status_code == 200:
            resp_json = json.loads(resp.text)
            poster_path = 'https://image.tmdb.org/t/p/original/' + resp_json['poster_path']
        return poster_path
    df['tmdbId'] = df['tmdbId'].astype(int)
    df['tmdbId'] = df['tmdbId'].apply(poster_find)
    # print(df.tmdid)
    # print(poster_link(800))
    # data = response.json()
    # print(credits_df.cast.values[0])
    # df.to_csv('sample.csv')
    return df

# dataAdd_df('batman').to_csv('sample.csv')