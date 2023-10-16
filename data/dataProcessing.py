import pandas as pd
import json

def preprocess_movie_data(file_path):
    # Đọc dữ liệu từ file CSV vào DataFrame
    df = pd.read_csv(file_path)

    # Chuyển các chuỗi JSON hợp lệ trong cột 'genres' thành danh sách
    def parse_json(x):
        try:
            return json.loads(x.replace("'", "\""))
        except (json.JSONDecodeError, AttributeError):
            return []

    df['genres'] = df['genres'].apply(parse_json)

    # Trích xuất giá trị 'name' từ cột 'genres' và ghi đè cột 'genres' với danh sách các tên thể loại
    df['genres'] = df['genres'].apply(lambda genres: ', '.join([genre['name'] for genre in genres]) if isinstance(genres, list) else '')

    # Xử lý cột 'production_companies'
    df['production_companies'] = df['production_companies'].apply(parse_json)

    # Trích xuất giá trị 'name' từ cột 'production_companies' và ghi đè cột 'production_companies' với danh sách các tên công ty sản xuất
    df['production_companies'] = df['production_companies'].apply(lambda companies: ', '.join([company['name'] for company in companies]) if isinstance(companies, list) else '')
    # Xử lý cột 'production_countries'
    df['production_countries'] = df['production_countries'].apply(parse_json)

    # Trích xuất giá trị 'name' từ cột 'production_countries' và ghi đè cột 'production_countries' với danh sách các tên quốc gia sản xuất
    df['production_countries'] = df['production_countries'].apply(lambda countries: ', '.join([country['name'] for country in countries]) if isinstance(countries, list) else '')
    
    df['belongs_to_collection'] = df['belongs_to_collection'].apply(parse_json)

    df['belongs_to_collection'] = df['belongs_to_collection'].apply(lambda collections: ', '.join([collection['name'] for collection in collections]) if isinstance(collections, list) else '')

    return df


# Sử dụng hàm và lưu kết quả vào biến df_processed
df_processed = preprocess_movie_data("C:\\Users\\ADMIN\\VSC Projects\\Project\\movies_metadata.csv")

unique_genres = list(set([genre for genres in df_processed['genres'] for genre in genres]))

unique_production_countries = list(set([country for countries in df_processed['production_countries'] for country in countries]))

unique_production_companies = list(set([company for companies in df_processed['production_companies'] for company in companies]))

unique_original_language = list(set([language for languages in df_processed['original_language'] if isinstance(languages, list) for language in languages]))
