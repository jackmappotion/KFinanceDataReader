from .DartDataReader import DartDataReader


class CorpDataReader:
    def __init__(self, dart_api_key):
        self.dart_data_reader = DartDataReader(dart_api_key)
        self.corp_df = self.dart_data_reader.corp_data_reader.get_corp_df()
        self.stock_corp_dict = self.corp_df.set_index('stock_code')['corp_code'].to_dict()

    def get_fundamental_df(self, stock_code, reprt_code, year):
        corp_code = self.stock_corp_dict[stock_code]
        fundamental_df = self.dart_data_reader.fundamental_data_reader.get_single_fundamental_df(corp_code, year, reprt_code)
        return fundamental_df

    def get_fundamentals_df(self, stock_codes, reprt_code, year):
        corp_codes = list(self.corp_df[self.corp_df['stock_code'].isin(stock_codes)]['corp_code'])
        fundamental_df = self.dart_data_reader.fundamental_data_reader.get_multi_fundamental_df(corp_codes, year, reprt_code)
        return fundamental_df
