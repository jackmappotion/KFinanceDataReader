import pandas as pd
from ._data_reader import _DataReader


class MonetaryDataReader(_DataReader):
    def get_m0_df(self, start_date, end_date):
        """본원 통화"""
        m0_last_raw = self.ecos_fetcher.fetch_item_value_df('102Y001', 'M', start_date, end_date, 'ABA2')
        m0_last_raw = self.df2series(m0_last_raw, '본원_말잔_원계열')

        m0_avg_raw = self.ecos_fetcher.fetch_item_value_df('102Y002', 'M', start_date, end_date, 'ABA1')
        m0_avg_raw = self.df2series(m0_avg_raw, '본원_평잔_원계열')

        m0_last_season = self.ecos_fetcher.fetch_item_value_df('102Y003', 'M', start_date, end_date, 'ABA2')
        m0_last_season = self.df2series(m0_last_season, '본원_말잔_계절조정')

        m0_avg_season = self.ecos_fetcher.fetch_item_value_df('102Y004', 'M', start_date, end_date, 'ABA1')
        m0_avg_season = self.df2series(m0_avg_season, '본원_평잔_계절조정')

        m0_df = pd.concat([m0_avg_raw, m0_avg_season, m0_last_raw, m0_last_season], axis=1)
        return m0_df

    def get_m1_df(self, start_date, end_date):
        """협의 통화"""
        m1_last_season = self.ecos_fetcher.fetch_item_value_df('101Y016', 'M', start_date, end_date, 'BBKS00')
        m1_last_season = self.df2series(m1_last_season, 'M1_말잔_계절조정')

        m1_last_raw = self.ecos_fetcher.fetch_item_value_df('101Y017', 'M', start_date, end_date, 'BBKA00')
        m1_last_raw = self.df2series(m1_last_raw, 'M1_말잔_원계열')

        m1_avg_season = self.ecos_fetcher.fetch_item_value_df('101Y018', 'M', start_date, end_date, 'BBLS00')
        m1_avg_season = self.df2series(m1_avg_season, 'M1_평잔_계절조정')

        m1_avg_raw = self.ecos_fetcher.fetch_item_value_df('101Y019', 'M', start_date, end_date, 'BBLA00')
        m1_avg_raw = self.df2series(m1_avg_raw, 'M1_평잔_원계열')

        m1_df = pd.concat([m1_avg_raw, m1_avg_season, m1_last_raw, m1_last_season], axis=1)
        return m1_df

    def get_m2_df(self, start_date, end_date):
        """광의 통화"""
        m2_last_season = self.ecos_fetcher.fetch_item_value_df('101Y001', 'M', start_date, end_date, 'BBGS00')
        m2_last_season = self.df2series(m2_last_season, 'M2_말잔_계절조정')

        m2_last_raw = self.ecos_fetcher.fetch_item_value_df('101Y002', 'M', start_date, end_date, 'BBGA00')
        m2_last_raw = self.df2series(m2_last_raw, 'M2_말잔_원계열')

        m2_avg_season = self.ecos_fetcher.fetch_item_value_df('101Y003', 'M', start_date, end_date, 'BBHS00')
        m2_avg_season = self.df2series(m2_avg_season, 'M2_평잔_계절조정')

        m2_avg_raw = self.ecos_fetcher.fetch_item_value_df('101Y004', 'M', start_date, end_date, 'BBHA00')
        m2_avg_raw = self.df2series(m2_avg_raw, 'M2_평잔_원계열')

        m2_df = pd.concat([m2_avg_raw, m2_avg_season, m2_last_raw, m2_last_season], axis=1)
        return m2_df

    def get_m2_ratio_df(self, start_date, end_date):
        """광의통화 말잔-원계열-비율"""
        m2_household = self.ecos_fetcher.fetch_item_value_df('101Y014', 'M', start_date, end_date, 'BBGAJ1')
        m2_household = self.df2series(m2_household, 'M2_가계_비영리단체')

        m2_corporate = self.ecos_fetcher.fetch_item_value_df('101Y014', 'M', start_date, end_date, 'BBGAJ2')
        m2_corporate = self.df2series(m2_corporate, 'M2_기업')

        m2_financial_corporate = self.ecos_fetcher.fetch_item_value_df('101Y014', 'M', start_date, end_date, 'BBGAJ3')
        m2_financial_corporate = self.df2series(m2_financial_corporate, 'M2_기타_금융기관')

        m2_etc = self.ecos_fetcher.fetch_item_value_df('101Y014', 'M', start_date, end_date, 'BBGAJ4')
        m2_etc = self.df2series(m2_etc, 'M2_기타')

        m2_last_raw_ratio_df = pd.concat([m2_household, m2_corporate, m2_financial_corporate, m2_etc], axis=1)
        return m2_last_raw_ratio_df
