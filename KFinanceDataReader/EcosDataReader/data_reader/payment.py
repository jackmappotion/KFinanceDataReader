import pandas as pd
from ._data_reader import _DataReader


class PaymentDataReader(_DataReader):
    def get_payment_cnt_df(self, start_date, end_date):
        """지급수단 건별"""
        payment_cnt_df = self.ecos_fetcher.fetch_item_value_df('602Y002', 'M', start_date, end_date)
        payment_cnt_df = payment_cnt_df[
            (payment_cnt_df['ITEM_CODE1'].isin(['D0000', 'D1000', 'D2000', 'E0000', 'E1000', 'E1100', 'E1300', 'E3000']))
            & (payment_cnt_df['ITEM_CODE2'] == 'EACH')
        ]
        payment_cnt_df = payment_cnt_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        payment_cnt_df.columns.name = None
        return payment_cnt_df

    def get_payment_won_df(self, start_date, end_date):
        """지급수단 총액"""
        payment_won_df = self.ecos_fetcher.fetch_item_value_df('602Y002', 'M', start_date, end_date)
        payment_won_df = payment_won_df[
            (payment_won_df['ITEM_CODE1'].isin(['D0000', 'D1000', 'D2000', 'E0000', 'E1000', 'E1100', 'E1300', 'E3000']))
            & (payment_won_df['ITEM_CODE2'] == 'MONEY')
        ]
        payment_won_df = payment_won_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        payment_won_df.columns.name = None
        return payment_won_df

    def get_total_credit_card_df(self, start_date, end_date):
        """개인 총합 신용카드"""
        total_credit_card_df = self.ecos_fetcher.fetch_item_value_df('601Y003', 'M', start_date, end_date)
        total_credit_card_df = total_credit_card_df[
            total_credit_card_df['ITEM_CODE1'].isin(
                ['101000', '101010', '101020', '101030', '201000', '201010', '201020', '201030', '301000']
            )
        ]
        total_credit_card_df = total_credit_card_df[total_credit_card_df['ITEM_NAME2'] == '합계'].pivot(
            index='TIME', columns='ITEM_NAME1', values='DATA_VALUE'
        )
        total_credit_card_df.columns.name = None
        return total_credit_card_df

    def get_bank_credit_card_df(self, start_date, end_date):
        """개인 은행권 신용카드"""
        bank_credit_card_df = self.ecos_fetcher.fetch_item_value_df('601Y003', 'M', start_date, end_date)
        bank_credit_card_df = bank_credit_card_df[
            bank_credit_card_df['ITEM_CODE1'].isin(
                ['101000', '101010', '101020', '101030', '201000', '201010', '201020', '201030', '301000']
            )
        ]
        bank_credit_card_df = bank_credit_card_df[bank_credit_card_df['ITEM_NAME2'] == '은행계'].pivot(
            index='TIME', columns='ITEM_NAME1', values='DATA_VALUE'
        )
        bank_credit_card_df.columns.name = None
        return bank_credit_card_df

    def get_not_bank_credit_card_df(self, start_date, end_date):
        """개인 비은행권 신용카드"""
        not_bank_credit_card_df = self.ecos_fetcher.fetch_item_value_df('601Y003', 'M', start_date, end_date)
        not_bank_credit_card_df = not_bank_credit_card_df[
            not_bank_credit_card_df['ITEM_CODE1'].isin(
                ['101000', '101010', '101020', '101030', '201000', '201010', '201020', '201030', '301000']
            )
        ]
        not_bank_credit_card_df = not_bank_credit_card_df[not_bank_credit_card_df['ITEM_NAME2'] == '비은행계'].pivot(
            index='TIME', columns='ITEM_NAME1', values='DATA_VALUE'
        )
        not_bank_credit_card_df.columns.name = None
        return not_bank_credit_card_df
