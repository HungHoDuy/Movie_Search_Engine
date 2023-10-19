import pandas as pd
from data_filter import *


def AtoZ_df(keyword):
    re_list = pd.read_csv('data_done.csv')
    df = re_list[0]
    # print(df)
    keyword = ' '.join(re_list[1])
    df = df.sort_values(by="title", ascending=True)
    return df

# AtoZ_df('irod mad').to_csv('result_sample.csv')