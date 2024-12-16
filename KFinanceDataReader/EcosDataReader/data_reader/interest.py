import pandas as pd
from ._data_reader import _DataReader


class InterestDataReader(_DataReader):
    """금리"""

    def get_interest_rate_df(self, start_date, end_date):
        """금리"""
        # 한국은행 기준금리
        base_ir = self.ecos_fetcher.fetch_item_value_df('722Y001', 'M', start_date, end_date, '0101000')
        base_ir = self.df2series(base_ir, '기준금리')

        # 수신금리
        deposit_ir = self.ecos_fetcher.fetch_item_value_df('121Y002', 'M', start_date, end_date, 'BEABAA2')
        deposit_ir = self.df2series(deposit_ir, '수신금리')

        # 대출금리
        loan_ir = self.ecos_fetcher.fetch_item_value_df('121Y006', 'M', start_date, end_date, 'BECBLA01')
        loan_ir = self.df2series(loan_ir, '대출금리')
        interest_rate_df = pd.concat([base_ir, deposit_ir, loan_ir], axis=1)
        return interest_rate_df

    def get_national_treasury_df(self, start_date, end_date):
        """국고채"""
        # 국고채 1년
        nt_1_year = self.ecos_fetcher.fetch_item_value_df('817Y002', 'D', start_date, end_date, '010190000')
        nt_1_year = self.df2series(nt_1_year, '국고채_1년')

        # 국고채 3년
        nt_3_year = self.ecos_fetcher.fetch_item_value_df('817Y002', 'D', start_date, end_date, '010200000')
        nt_3_year = self.df2series(nt_3_year, '국고채_3년')

        # 국고채 5년
        nt_5_year = self.ecos_fetcher.fetch_item_value_df('817Y002', 'D', start_date, end_date, '010200001')
        nt_5_year = self.df2series(nt_5_year, '국고채_5년')

        # 국고채 10년
        nt_10_year = self.ecos_fetcher.fetch_item_value_df('817Y002', 'D', start_date, end_date, '010210000')
        nt_10_year = self.df2series(nt_10_year, '국고채_10년')

        # 국고채 20년
        nt_20_year = self.ecos_fetcher.fetch_item_value_df('817Y002', 'D', start_date, end_date, '010220000')
        nt_20_year = self.df2series(nt_20_year, '국고채_20년')

        national_treasury_df = pd.concat([nt_1_year, nt_3_year, nt_5_year, nt_10_year, nt_20_year], axis=1)
        return national_treasury_df
