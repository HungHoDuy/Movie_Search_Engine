import pandas as pd
from data_filter import *


def ZtoA_df(keyword):
    re_list = pd.read_csv('data_done.csv')
    df = re_list[0]
    # print(df)
    keyword = ' '.join(re_list[1])
    df = df.sort_values(by="title", ascending=False)
    return df

# ZtoA_df('irod mad').to_csv('result_sample.csv')