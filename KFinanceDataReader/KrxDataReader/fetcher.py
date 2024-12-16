import requests
import datetime as dt
import pandas as pd


class KrxFetcher:
    def __init__(self) -> None:
        self.headers = {
            'User-Agent': 'Chrome/78.0.3904.87 Safari/537.36',
            'Referer': 'http://data.krx.co.kr/',
        }
        self.url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'

    def fetch(self, data, key):
        return self.data2df(data, key)

    def fetch_with_date_ranges(self, data, key, date_ranges):
        df_list = []
        for start_date, end_date in date_ranges:
            data['strtDd'] = start_date.strftime("%Y%m%d")
            data['endDd'] = end_date.strftime("%Y%m%d")
            _df = self.data2df(data, key)
            df_list.append(_df)
        return pd.concat(df_list, axis=0)

    def data2df(self, data, key):
        resp = requests.post(self.url, data, headers=self.headers)
        df = pd.DataFrame(resp.json().get(key))
        return df
