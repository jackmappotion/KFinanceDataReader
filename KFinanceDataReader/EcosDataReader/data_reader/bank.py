import pandas as pd
from ._data_reader import _DataReader


class BankDataReader(_DataReader):
    def get_deposit_df(self, start_date, end_date):
        """예금 말잔"""
        deposit_df = self.ecos_fetcher.fetch_item_value_df('104Y013', 'M', start_date, end_date)
        deposit_df = deposit_df[deposit_df['ITEM_CODE1'].isin(['BCB1', 'BCB2', 'BCB8'])]
        deposit_df = deposit_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        deposit_df.columns.name = None
        return deposit_df

    def get_deposit_by_owner_df(self, start_date, end_date):
        """예금 집단별"""
        deposit_by_owner_df = self.ecos_fetcher.fetch_item_value_df('104Y009', 'M', start_date, end_date)
        deposit_by_owner_df = deposit_by_owner_df[
            deposit_by_owner_df['ITEM_CODE1'].isin(['1000000', '1010000', '1020000', '1030000', '1040000', '1050000'])
        ]
        deposit_by_owner_df = deposit_by_owner_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        deposit_by_owner_df.columns.name = None
        return deposit_by_owner_df

    def get_loan_df(self, start_date, end_date):
        """부채 말잔"""
        loan_df = self.ecos_fetcher.fetch_item_value_df('104Y016', 'M', start_date, end_date)
        loan_df = loan_df[loan_df['ITEM_CODE1'].isin(['BDCA21', 'BDCA31', 'BDCA2E', 'BDCA1'])]
        loan_df = loan_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        loan_df.columns.name = None
        return loan_df

    def get_overdue_loan_rate_df(self, start_date, end_date):
        """연체율"""
        overdue_loan_rate_df = self.ecos_fetcher.fetch_item_value_df('901Y054', 'M', start_date, end_date)
        ('MO3AB', 'AB'), ('MO3AA', 'AB'), ('MO3AC', 'AB')
        overdue_loan_rate_df = overdue_loan_rate_df[
            ((overdue_loan_rate_df['ITEM_CODE1'] == 'MO3AB') & (overdue_loan_rate_df['ITEM_CODE2'] == 'AB'))
            | ((overdue_loan_rate_df['ITEM_CODE1'] == 'MO3AA') & (overdue_loan_rate_df['ITEM_CODE2'] == 'AB'))
            | ((overdue_loan_rate_df['ITEM_CODE1'] == 'MO3AC') & (overdue_loan_rate_df['ITEM_CODE2'] == 'AB'))
        ]
        overdue_loan_rate_df = overdue_loan_rate_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        overdue_loan_rate_df.columns.name = None
        return overdue_loan_rate_df

    def get_bok_asset_df(self, start_date, end_date):
        """한국은행 자산"""
        bok_assets_df = self.ecos_fetcher.fetch_item_value_df('732Y001', 'M', start_date, end_date)
        bok_assets_df = bok_assets_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        bok_assets_df.columns.name = None
        return bok_assets_df
