import pandas as pd
import json

def preprocess_movie_data(file_path): # This function is not working correctly, please fix it change type of data in columns to string (Trung Huynh Quoc)
    # Đọc dữ liệu từ file CSV vào DataFrame
    df = pd.read_csv(file_path, low_memory=False)

    # Chuyển các chuỗi JSON hợp lệ trong cột 'genres' thành danh sách
    def parse_json(x):
        try:
            return json.loads(x.replace("'", "\""))
        except (json.JSONDecodeError, AttributeError):
            return []

    df['genres'] = df['genres'].apply(parse_json)

    # Trích xuất giá trị 'name' từ cột 'genres' và ghi đè cột 'genres' với danh sách các tên thể loại
    df['genres'] = df['genres'].apply(lambda genres: [genre['name'] for genre in genres] if isinstance(genres, list) else [])

    # Xử lý cột 'production_companies'
    df['production_companies'] = df['production_companies'].apply(parse_json)

    # Trích xuất giá trị 'name' từ cột 'production_companies' và ghi đè cột 'production_companies' với danh sách các tên công ty sản xuất
    df['production_companies'] = df['production_companies'].apply(lambda companies: [company['name'] for company in companies] if isinstance(companies, list) else [])

    # Xử lý cột 'production_countries'
    df['production_countries'] = df['production_countries'].apply(parse_json)

    # Trích xuất giá trị 'name' từ cột 'production_countries' và ghi đè cột 'production_countries' với danh sách các tên quốc gia sản xuất
    df['production_countries'] = df['production_countries'].apply(lambda countries: [country['name'] for country in countries] if isinstance(countries, list) else [])

    return df


# Sử dụng hàm và lưu kết quả vào biến df_processed
df_processed = preprocess_movie_data("/home/chunporo/Documents/GitHub/Movie_Search_Engine/data/movies_metadata.csv")

unique_genres = list(set([genre.lower() for genres in df_processed['genres'] for genre in genres]))

unique_production_countries = list(set([country.lower() for countries in df_processed['production_countries'] for country in countries]))

unique_production_companies = list(set([company.lower() for companies in df_processed['production_companies'] for company in companies]))

unique_language = list(set([language for language in df_processed['original_language']]))

def find_name(data_str):
    start = data_str.find("'name': '") + len("'name': '")
    end = data_str.find("'", start)
    return data_str[start:end]


unique_collection = list(set(find_name(str(collection).lower()) for collection in df_processed['belongs_to_collection']))
unique_collection.pop(0)
