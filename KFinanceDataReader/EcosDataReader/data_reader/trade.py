import pandas as pd
from ._data_reader import _DataReader

class TradeDataReader(_DataReader):
    """무역"""

    def get_trade_balance_df(self, start_date, end_date):
        """경상수지"""
        trade_balance_df = self.ecos_fetcher.fetch_item_value_df('301Y013', 'M', start_date, end_date)
        trade_balance_df = trade_balance_df[trade_balance_df['ITEM_CODE1'].isin(['000000', '100000', '200000', '300000', '400000'])]
        trade_balance_df = trade_balance_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        trade_balance_df.columns.name = None
        return trade_balance_df

    def get_trade_export_country_df(self, start_date, end_date):
        """수출 국가별 / 총액"""
        trade_export_df = self.ecos_fetcher.fetch_item_value_df('901Y011', 'M', start_date, end_date)
        trade_export_df = trade_export_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        trade_export_df.columns.name = None
        return trade_export_df

    def get_trade_import_country_df(self, start_date, end_date):
        """수입 국가별 / 총액"""
        trade_import_df = self.ecos_fetcher.fetch_item_value_df('901Y012', 'M', start_date, end_date)
        trade_import_df = trade_import_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        trade_import_df.columns.name = None
        return trade_import_df

    def get_trade_export_product_df(self, start_date, end_date):
        """수출 품목별 / 총액"""
        trade_export_df = self.ecos_fetcher.fetch_item_value_df('403Y001', 'M', start_date, end_date)
        code_name_dict = trade_export_df.set_index('ITEM_CODE1')['ITEM_NAME1'].to_dict()
        trade_export_df = trade_export_df.pivot(index='TIME', columns='ITEM_CODE1', values='DATA_VALUE')
        trade_export_df.columns = list(map(lambda x: code_name_dict[x], trade_export_df.columns))
        trade_export_df.columns.name = None
        return trade_export_df
    
    def get_trade_import_product_df(self, start_date, end_date):
        """수입 품목별 / 총액"""
        trade_import_df = self.ecos_fetcher.fetch_item_value_df('403Y003', 'M', start_date, end_date)
        code_name_dict = trade_import_df.set_index('ITEM_CODE1')['ITEM_NAME1'].to_dict()
        trade_import_df = trade_import_df.pivot(index='TIME', columns='ITEM_CODE1', values='DATA_VALUE')
        trade_import_df.columns = list(map(lambda x: code_name_dict[x], trade_import_df.columns))
        trade_import_df.columns.name = None
        return trade_import_df