import pandas as pd


def get_chunked_list(_list, n):
    return [_list[i : i + n] for i in range(0, len(_list), n)]


def safe_concat(df_list):
    filtered_df_list = list(filter(lambda x: x is not None, df_list))
    if filtered_df_list:
        return pd.concat(filtered_df_list, axis=0)
    return pd.DataFrame()
