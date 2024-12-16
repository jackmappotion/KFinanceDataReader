import pandas as pd
from ._data_reader import _DataReader


class GlobalIndexDataReader(_DataReader):
    def get_global_interest_df(self, start_date, end_date):
        """주요국 기준금리"""
        global_interest_df = self.ecos_fetcher.fetch_item_value_df('902Y006', 'M', start_date, end_date)
        global_interest_df = global_interest_df[global_interest_df['ITEM_CODE1'].isin(['KR', 'US', 'XM', 'JP'])]
        global_interest_df = global_interest_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        global_interest_df.columns.name = None
        return global_interest_df

    def get_global_short_interest_df(self, start_date, end_date):
        """주요국 단기금리"""
        global_short_interest_df = self.ecos_fetcher.fetch_item_value_df('902Y023', 'M', start_date, end_date)
        global_short_interest_df = global_short_interest_df[global_short_interest_df['ITEM_CODE1'] == 'IR3TIB']
        global_short_interest_df = global_short_interest_df.pivot(index='TIME', columns='ITEM_NAME2', values='DATA_VALUE')
        global_short_interest_df.columns.name = None
        return global_short_interest_df

    def get_global_long_interest_df(self, start_date, end_date):
        """주요국 장기금리"""
        global_long_interest_df = self.ecos_fetcher.fetch_item_value_df('902Y023', 'M', start_date, end_date)
        global_long_interest_df = global_long_interest_df[global_long_interest_df['ITEM_CODE1'] == 'IRLT']
        global_long_interest_df = global_long_interest_df.pivot(index='TIME', columns='ITEM_NAME2', values='DATA_VALUE')
        global_long_interest_df.columns.name = None
        return global_long_interest_df

    def get_global_market_index_df(self, start_date, end_date):
        """주요국 주가지수"""
        global_market_index_df = self.ecos_fetcher.fetch_item_value_df('902Y002', 'M', start_date, end_date)
        global_market_index_df = global_market_index_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        global_market_index_df.columns.name = None
        return global_market_index_df

    def get_global_ppi_df(self, start_date, end_date):
        """주요국 생산자물가지수"""
        global_ppi_df = self.ecos_fetcher.fetch_item_value_df('902Y007', 'M', start_date, end_date)
        global_ppi_df = global_ppi_df[global_ppi_df['ITEM_CODE1'].isin(['KR', 'US', 'CN', 'JP'])]
        global_ppi_df = global_ppi_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        global_ppi_df.columns.name = None
        return global_ppi_df

    def get_global_cpi_df(self, start_date, end_date):
        """주요국 소비자물가지수"""
        global_cpi_df = self.ecos_fetcher.fetch_item_value_df('902Y008', 'M', start_date, end_date)
        global_cpi_df = global_cpi_df[global_cpi_df['ITEM_CODE1'].isin(['KR', 'US', 'CN', 'JP'])]
        global_cpi_df = global_cpi_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        global_cpi_df.columns.name = None
        return global_cpi_df
