import pandas as pd
from ._data_reader import _DataReader


class PriceIndexDataReader(_DataReader):
    def get_ppi_df(self, start_date, end_date):
        """생산자물가지수"""
        ppi_df = self.ecos_fetcher.fetch_item_value_df('404Y014', 'M', start_date, end_date)
        ppi_df = ppi_df[ppi_df['ITEM_CODE1'].isin(['*AA', '1AA', '2AA', '3AA', '4AA', '5AA'])]
        ppi_df = ppi_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        ppi_df.columns.name = None
        return ppi_df

    def get_cpi_df(self, start_date, end_date):
        """소비자물가지수"""
        cpi_df = self.ecos_fetcher.fetch_item_value_df('901Y009', 'M', start_date, end_date)
        cpi_df = cpi_df[cpi_df['ITEM_CODE1'].isin(['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])]
        cpi_df = cpi_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        cpi_df.columns.name = None
        return cpi_df

    def get_export_pi_df(self, start_date, end_date):
        """수출물가지수"""
        export_pi_df = self.ecos_fetcher.fetch_item_value_df('402Y014', 'M', start_date, end_date)
        export_pi_df = export_pi_df[
            (export_pi_df['ITEM_CODE1'].isin(['*AA', '1AA', '3AA'])) & (export_pi_df['ITEM_CODE2'] == 'D')
        ]
        export_pi_df = export_pi_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        export_pi_df.columns.name = None
        return export_pi_df

    def get_import_pi_df(self, start_date, end_date):
        """수입물가지수"""
        import_pi_df = self.ecos_fetcher.fetch_item_value_df('401Y015', 'M', start_date, end_date)
        import_pi_df = import_pi_df[
            (import_pi_df['ITEM_CODE1'].isin(['*AA', '1AA', '2AA', '3AA'])) & (import_pi_df['ITEM_CODE2'] == 'D')
        ]
        import_pi_df = import_pi_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        import_pi_df.columns.name = None
        return import_pi_df

    def get_housing_price_df(self, start_date, end_date):
        """주택매매가격지수"""
        housing_price_df = self.ecos_fetcher.fetch_item_value_df('901Y062', 'M', start_date, end_date)
        housing_price_df = housing_price_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        housing_price_df.columns.name = None
        return housing_price_df
