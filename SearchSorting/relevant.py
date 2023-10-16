import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dataAdd import dataAdd_df

def relevant_df(keyword):
    df = dataAdd_df(keyword)
    features = ['keywords', 'cast', 'genres', 'crew']
    for feature in features:
        df[feature] = df[feature].fillna('')

    def combined_features(row):
        return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['crew']

    df['combined_features'] = df.apply(combined_features, axis=1)
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['combined_features'])
    # print("Count Matrix: ", count_matrix.toarray())
    cosine_sim = cosine_similarity(count_matrix)
    movie_user_like = keyword.title() # if keyword dont appear in title will choose number[0]
    def get_index_from(title):
        return df[df.title == title].index[0]

    movie_index = get_index_from(movie_user_like)

    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    # print(sorted_similar_movies)
    def get_title_from_index(index):
        return df[df.index == index]["title"].values[0]

    i = 0
    movie_list = []
    for movies in sorted_similar_movies:
        movie_list.append(movies[0])
    df = df.reindex(movie_list)
    return df

relevant_df('your name').to_csv('sample.csv')
