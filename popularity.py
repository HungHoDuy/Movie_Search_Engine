import pandas as pd
from data_filter import DataFilter


def popularity_df(keyword):
    re_list = DataFilter(keyword)
    df = re_list[0]
    # print(df)
    keyword = ' '.join(re_list[1])
    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
    df = df.sort_values(by="popularity", ascending=False)
    return df


# a = popularity_df('your name +animation')
# a.to_csv()
# print(a.poster_path.values[0])
