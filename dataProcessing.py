import pandas as pd
import json

def preprocess_movie_data(file_path):
    df = pd.read_csv(file_path, low_memory=False)

    def parse_json(x):
        try:
            return json.loads(x.replace("'", "\""))
        except (json.JSONDecodeError, AttributeError):
            return []

    df['genres'] = df['genres'].apply(parse_json)

    df['genres'] = df['genres'].apply(lambda genres: ', '.join([genre['name'] for genre in genres]) if isinstance(genres, list) else '')

    df['production_companies'] = df['production_companies'].apply(parse_json)

    df['production_companies'] = df['production_companies'].apply(lambda companies: ', '.join([company['name'] for company in companies]) if isinstance(companies, list) else '')

    df['production_countries'] = df['production_countries'].apply(parse_json)

    df['production_countries'] = df['production_countries'].apply(lambda countries: ', '.join([country['name'] for country in countries]) if isinstance(countries, list) else '')
    
    df['belongs_to_collection'] = df['belongs_to_collection'].apply(parse_json)

    df['belongs_to_collection'] = df['belongs_to_collection'].apply(lambda collections: ', '.join([collection['name'] for collection in collections]) if isinstance(collections, list) else '')

    return df

# df_processed = preprocess_movie_data("C:\\Users\\ADMIN\\Desktop\Movie_Search_Engine\\data\\movies_metadata.csv")

# df_processed['genres'] = df_processed['genres'].str.split(', ')
# all_genres = sum(df_processed['genres'], [])
# unique_genres = list(set(all_genres))
# unique_genres.remove('')
# unique_genres = [genre.replace(' ', '_') for genre in unique_genres]


# df_processed['production_companies'] = df_processed['production_companies'].str.split(',')
# all_companies = sum(df_processed['production_companies'], [])
# unique_production_companies = list(set(all_companies))
# unique_production_companies.remove('')
# unique_production_companies = [company.replace(' ', '_') for company in unique_production_companies]

# df_processed['production_countries'] = df_processed['production_countries'].str.split(',')
# all_countries = sum(df_processed['production_countries'], [])
# unique_production_countries = list(set(all_countries))
# unique_production_countries.remove('')
# unique_production_countries = [country.replace(' ', '_') for country in unique_production_countries]

# unique_languages = list(set(''.join(str(items)) for items in df_processed['original_language']))

# df_processed['production_countries'] = df_processed['production_countries'].str.split(',')
# all_countries = sum(df_processed['production_countries'], [])
# unique_production_countries = list(set(all_countries))
# unique_production_countries.remove('')
# unique_production_countries = [country.replace(' ', '_') for country in unique_production_countries]

# print(unique_genres)