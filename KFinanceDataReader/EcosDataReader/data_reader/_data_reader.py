import pandas as pd
from ..fetcher import EcosFetcher


class _DataReader:
    def __init__(self, api_key):
        self.api_key = api_key
        self.ecos_fetcher = EcosFetcher(api_key)

    @staticmethod
    def df2series(df, name):
        series = df.set_index("TIME")['DATA_VALUE']
        series.name = name
        return series
