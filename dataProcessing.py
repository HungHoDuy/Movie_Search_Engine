import pandas as pd
import json
from langcodes import Language
import numpy as np
#import math
import ast
def preprocess_movie_data(file_path):
    df = pd.read_csv(file_path, low_memory=False)

    def parse_json(x):
        try:
            return json.loads(x.replace("'", "\""))
        except (json.JSONDecodeError, AttributeError):
            return []

    df['genres'] = df['genres'].apply(parse_json)

    df['genres'] = df['genres'].apply(lambda genres: ','.join([genre['name'] for genre in genres]) if isinstance(genres, list) else '')

    df['production_companies'] = df['production_companies'].apply(parse_json)

    df['production_companies'] = df['production_companies'].apply(lambda companies: ','.join([company['name'] for company in companies]) if isinstance(companies, list) else '')

    df['production_countries'] = df['production_countries'].apply(parse_json)

    df['production_countries'] = df['production_countries'].apply(lambda countries: ','.join([country['name'] for country in countries]) if isinstance(countries, list) else '')

    df['belongs_to_collection'] = df['belongs_to_collection'].apply(parse_json)

    # df['belongs_to_collection'] = df['belongs_to_collection'].apply(lambda collections: ','.join([collection['name'] for collection in collections]) if isinstance(collections, list) else '')
    #Add some feature(Huynh Quoc Trung)
    df['spoken_languages'] = df['spoken_languages'].apply(parse_json)
    df['spoken_languages'] = df['spoken_languages'].apply(lambda genres: ','.join([genre['name'] for genre in genres]) if isinstance(genres, list) else '')
    df['year'] = pd.to_datetime(df['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
    def code_to_language(code):
        try:
            language = Language.get(code)
            return language.display_name() if language else code
        except Exception as e:
            print(f"Error: {e}")
            return code

    df['original_language'] = df['original_language'].apply(code_to_language)
    credit_file_links = 'credits.csv'
    keyword_file_links = 'keywords.csv'
    link_file_links = 'links.csv'

    credits_df = pd.read_csv(credit_file_links, low_memory=False)
    keyword_df = pd.read_csv(keyword_file_links)
    link_df = pd.read_csv(link_file_links)

    df['id'] = df['id'].astype(str)
    credits_df['id'] = credits_df['id'].astype(str)
    keyword_df['id'] = keyword_df['id'].astype(str)
    link_df['movieId'] = link_df['movieId'].astype(str)

    df = pd.merge(df, credits_df, on='id', how='left')
    df = pd.merge(df, keyword_df, on='id', how='left')
    df= df.merge(link_df, left_on='id', right_on='movieId', how='left')
    # def poster_find(poster_path):
    #     return 'https://image.tmdb.org/t/p/original/' + poster_path
    # df['poster_path'] = df['tmdbId'].apply(poster_find)
    def find_name(data_inp):
        data_str = str(data_inp)
        start = data_str.find("'name': '") + len("'name': '")
        end = data_str.find("'", start)
        return data_str[start:end]
    df['belongs_to_collection'] = df['belongs_to_collection'].apply(find_name)

    def cast_name(data_str):
        try:
            data_list = ast.literal_eval(str(data_str))
            names = ','.join(item['name'] for item in data_list)
            return names
        except ValueError as ve:
            print(f"ValueError occurred: {ve}")
            return ""  # or handle it in some other way
        except Exception as e:
            print(f"Error occurred: {e}")
            return ""  # or handle it in some other way

    def find_director(data_str):
        data_change = str(data_str)
        start_index = data_change.find("'job': 'Director', 'name': '") + len("'job': 'Director', 'name': '")
        end_index = data_change.find("'", start_index)
        return data_change[start_index:end_index]

    df['crew'] = df['crew'].apply(find_director)
    df['cast'] = df['cast'].apply(cast_name)
    df['keywords'] = df['keywords'].apply(cast_name)
    return df

df_processed = preprocess_movie_data("movies_metadata.csv")

# df_processed['genres'] = df_processed['genres'].str.split(', ')
# all_genres = sum(df_processed['genres'], [])
# unique_genres = list(set(all_genres))
# unique_genres.remove('')
# unique_genres = [genre.replace(' ', '_') for genre in unique_genres]
#
# df_processed['production_companies'] = df_processed['production_companies'].str.split(',')
# all_companies = sum(df_processed['production_companies'], [])
# unique_production_companies = list(set(all_companies))
# unique_production_companies.remove('')
# unique_production_companies = [company.replace(' ', '_') for company in unique_production_companies]
#
# df_processed['production_countries'] = df_processed['production_countries'].str.split(',')
# all_countries = sum(df_processed['production_countries'], [])
# unique_production_countries = list(set(all_countries))
# unique_production_countries.remove('')
# unique_production_countries = [country.replace(' ', '_') for country in unique_production_countries]
#
# unique_languages = list(set(''.join(str(items)) for items in df_processed['original_language']))

# def code_to_language(code):
#     try:
#         language = Language.get(code)
#         return language.display_name() if language else code
#     except Exception as e:
#         print(f"Error: {e}")
#         return code
#
# language_codes =  unique_language
#
# languages = [code_to_language(code) for code in language_codes]
# my_list = languages
# languages_cleaned_list = [item for item in my_list if not (isinstance(item, float) and math.isnan(item))]
# df_processed.to_csv('movie_preprocessing.csv')