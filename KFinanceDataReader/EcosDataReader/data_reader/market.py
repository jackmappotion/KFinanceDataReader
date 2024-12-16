import pandas as pd
from ._data_reader import _DataReader


class MarketDataReader(_DataReader):

    def get_kospi_df(self, start_date, end_date):
        """KOSPI 지수, 거래량, 거래대금, 외국인순매수"""
        # kospi_지수
        kospi_value = self.ecos_fetcher.fetch_item_value_df('802Y001', 'D', start_date, end_date, '0001000')
        kospi_value = self.df2series(kospi_value, '코스피_지수')
        # kospi_거래량
        kospi_volume_cnt = self.ecos_fetcher.fetch_item_value_df('802Y001', 'D', start_date, end_date, '0002000')
        kospi_volume_cnt = self.df2series(kospi_volume_cnt, '코스피_거래량')
        # kospi_거래대금
        kospi_volume_won = self.ecos_fetcher.fetch_item_value_df('802Y001', 'D', start_date, end_date, '0003000')
        kospi_volume_won = self.df2series(kospi_volume_won, '코스피_거래대금')
        # kospi_외국인순매수
        kospi_foreign_buy = self.ecos_fetcher.fetch_item_value_df('802Y001', 'D', start_date, end_date, '0030000')
        kospi_foreign_buy = self.df2series(kospi_foreign_buy, '코스피_외국인순매수')
        kospi_df = pd.concat([kospi_value, kospi_volume_cnt, kospi_volume_won, kospi_foreign_buy], axis=1)
        return kospi_df

    def get_kosdaq_df(self, start_date, end_date):
        """KOSDAQ 지수, 거래량, 거래대금, 외국인순매수"""
        # kosdaq_지수
        kosdaq_value = self.ecos_fetcher.fetch_item_value_df('802Y001', 'D', start_date, end_date, '0089000')
        kosdaq_value = self.df2series(kosdaq_value, '코스닥_지수')
        # kosdaq_거래량
        kosdaq_volume_cnt = self.ecos_fetcher.fetch_item_value_df('802Y001', 'D', start_date, end_date, '0090000')
        kosdaq_volume_cnt = self.df2series(kosdaq_volume_cnt, '코스닥_거래량')
        # kosdaq_거래대금
        kosdaq_volume_won = self.ecos_fetcher.fetch_item_value_df('802Y001', 'D', start_date, end_date, '0091000')
        kosdaq_volume_won = self.df2series(kosdaq_volume_won, '코스닥_거래대금')
        # kosdaq_외국인순매수
        kosdaq_foreign_buy = self.ecos_fetcher.fetch_item_value_df('802Y001', 'D', start_date, end_date, '0113000')
        kosdaq_foreign_buy = self.df2series(kosdaq_foreign_buy, '코스닥_외국인순매수')
        kosdaq_df = pd.concat([kosdaq_value, kosdaq_volume_cnt, kosdaq_volume_won, kosdaq_foreign_buy], axis=1)
        return kosdaq_df

    def get_balance_df(self, start_date, end_date):
        """예탁금 / 파생거래 예탁금 / 미수금"""
        # 투자자 예탁금
        invest_deposit = self.ecos_fetcher.fetch_item_value_df('901Y056', 'M', start_date, end_date, 'S23A')
        invest_deposit = self.df2series(invest_deposit, '투자자_예탁금')

        # 파생거래 예탁금
        derivative_deposit = self.ecos_fetcher.fetch_item_value_df('901Y056', 'M', start_date, end_date, 'S23B')
        derivative_deposit = self.df2series(derivative_deposit, '파생거래_예탁금')

        # 미수금
        unpaid_balance = self.ecos_fetcher.fetch_item_value_df('901Y056', 'M', start_date, end_date, 'S23D')
        unpaid_balance = self.df2series(unpaid_balance, '미수금')

        balance_df = pd.concat([invest_deposit, derivative_deposit, unpaid_balance], axis=1)
        return balance_df

    def get_derivative_df(self, start_date, end_date):
        """파생거래 관련 데이터"""
        # 선물_계약수
        future_volume_cnt = self.ecos_fetcher.fetch_item_value_df('901Y057', 'M', start_date, end_date, 'S25A')
        future_volume_cnt = self.df2series(future_volume_cnt, '선물_계약수')

        # 선물_계약금액
        future_volume_won = self.ecos_fetcher.fetch_item_value_df('901Y057', 'M', start_date, end_date, 'S25C')
        future_volume_won = self.df2series(future_volume_won, '선물_계약금액')

        # CALL_옵션_계약수
        call_option_volume_cnt = self.ecos_fetcher.fetch_item_value_df('901Y058', 'M', start_date, end_date, 'S26BA')
        call_option_volume_cnt = self.df2series(call_option_volume_cnt, 'CALL_옵션_계약수')

        # CALL_옵션_계약금액
        call_option_volume_won = self.ecos_fetcher.fetch_item_value_df('901Y058', 'M', start_date, end_date, 'S26BC')
        call_option_volume_won = self.df2series(call_option_volume_won, 'CALL_옵션_계약금액')

        # PUT_옵션_계약수
        put_option_volume_cnt = self.ecos_fetcher.fetch_item_value_df('901Y058', 'M', start_date, end_date, 'S26CA')
        put_option_volume_cnt = self.df2series(put_option_volume_cnt, 'PUT_옵션_계약수')

        # PUT_옵션_계약금액
        put_option_volume_won = self.ecos_fetcher.fetch_item_value_df('901Y058', 'M', start_date, end_date, 'S26CC')
        put_option_volume_won = self.df2series(put_option_volume_won, 'PUT_옵션_계약금액')

        derivative_df = pd.concat(
            [
                future_volume_cnt,
                future_volume_won,
                call_option_volume_cnt,
                call_option_volume_won,
                put_option_volume_cnt,
                put_option_volume_won,
            ],
            axis=1,
        )
        return derivative_df
