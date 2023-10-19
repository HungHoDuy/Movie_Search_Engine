import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data_filter import DataFilter

def relevant_df(keyword):
    def keyword_similarity_advanced(title):
        # Create a TF-IDF vectorizer
        tfidf_vectorizer = TfidfVectorizer()
        movie_title = str(title)
        # Fit and transform the vectorizer on the keyword and movie title
        tfidf_matrix = tfidf_vectorizer.fit_transform([keyword.lower(), movie_title.lower()])
        # print(tfidf_matrix)
        # Calculate the cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

        return similarity * 100  # Convert to percentage

    re_list = DataFilter(keyword)
    df = re_list[0]
    print(df)
    keyword = ' '.join(re_list[1])
    df['score'] = df['title'].apply(keyword_similarity_advanced)
    df = df.sort_values(by='score', ascending=False)
    return df

# relevant_df('youd namd +animation').to_csv('result_sample.csv')