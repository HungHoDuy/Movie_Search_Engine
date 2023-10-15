import pandas as pd
import ast

# Đọc dữ liệu từ file CSV vào DataFrame
df = pd.read_csv("C:\\Users\\ADMIN\\VSC Projects\\Project\\movies_metadata.csv")

# Chuyển các chuỗi trong cột 'genres' thành danh sách
df['genres'] = df['genres'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Trích xuất giá trị 'name' từ cột 'genres' và ghi đè cột 'genres' với danh sách các tên thể loại
df['genres'] = df['genres'].apply(lambda genres: [genre['name'] for genre in genres] if isinstance(genres, list) else [])

# Loại bỏ các giá trị không hợp lệ trong cột 'production_companies'
df['production_companies'] = df['production_companies'].apply(lambda x: x if isinstance(x, list) else [])

# Trích xuất giá trị 'name' từ cột 'production_companies' và ghi đè cột 'production_companies' với danh sách các tên công ty sản xuất
df['production_companies'] = df['production_companies'].apply(lambda companies: [company['name'] for company in companies] if isinstance(companies, list) else [])

# In ra DataFrame
print(df['production_companies'][0])
