import pandas as pd
from data_filter import DataFilter


def popularity_df(keyword):
    df = DataFilter(keyword)
    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
    df = df.sort_values(by="popularity", ascending=False)
    return df


# a = popularity_df('your name +animation')
# a.to_csv()
# print(a.poster_path.values[0])
