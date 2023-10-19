import pandas as pd
from data_filter import DataFilter
from fuzzywuzzy import fuzz

def relevant_df(keyword):
    def keyword_similarity_advanced(title):
        if keyword.lower() == title.lower():
            return 500

        # Calculate the partial ratio between the keyword and the title
        similarity = fuzz.partial_ratio(keyword.lower(), title.lower())

        return similarity  # Convert to percentage

    re_list = DataFilter(keyword)
    df = re_list[0]
    # print(df)
    keyword = ' '.join(re_list[1])
    if keyword != '':
        df['score'] = df['title'].apply(keyword_similarity_advanced)
        df = df.sort_values(by='score', ascending=False)
    return df

# relevant_df('+science_fiction').to_csv('result_sample.csv')