import pandas as pd
from ._data_reader import _DataReader


class EconomicIndexDataReader(_DataReader):

    def get_macro_economic_index_df(self, start_date, end_date):
        """주요경기 지표"""
        composite_leading_index = self.ecos_fetcher.fetch_item_value_df('901Y067', 'M', start_date, end_date, 'I16B')
        composite_leading_index = self.df2series(composite_leading_index, '경기종합지수')

        facility_investment_index = self.ecos_fetcher.fetch_item_value_df('901Y066', 'M', start_date, end_date, 'I15A')
        facility_investment_index = self.df2series(facility_investment_index, '설비투자지수')

        manufacturing_index = self.ecos_fetcher.fetch_item_value_df('901Y032', 'M', start_date, end_date, 'I11A')
        manufacturing_index = manufacturing_index[manufacturing_index['ITEM_CODE2'].isin(['1', '3', '5'])]
        manufacturing_index = manufacturing_index.pivot(index='TIME', columns='ITEM_NAME2', values='DATA_VALUE')
        manufacturing_index.columns.name = None

        economic_index_df = pd.concat([composite_leading_index, facility_investment_index, manufacturing_index], axis=1)
        return economic_index_df

    def get_unemployment_cnt_df(self, start_date, end_date):
        """실업급여 수"""
        unemployment_cnt_df = self.ecos_fetcher.fetch_item_value_df('901Y084', 'M', start_date, end_date)
        unemployment_cnt_df = unemployment_cnt_df[unemployment_cnt_df['ITEM_CODE2'] == 'P']
        unemployment_cnt_df = unemployment_cnt_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        unemployment_cnt_df.columns.name = None
        return unemployment_cnt_df

    def get_unemployment_won_df(self, start_date, end_date):
        """실업급여 금액"""
        unemployment_won_df = self.ecos_fetcher.fetch_item_value_df('901Y084', 'M', start_date, end_date)
        unemployment_won_df = unemployment_won_df[unemployment_won_df['ITEM_CODE2'] == 'A']
        unemployment_won_df = unemployment_won_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        unemployment_won_df.columns.name = None
        return unemployment_won_df

    def get_house_info_df(self, start_date, end_date):
        """미분양"""
        unselled_house_df = self.ecos_fetcher.fetch_item_value_df('901Y074', 'M', start_date, end_date)
        unselled_house_df = unselled_house_df[unselled_house_df['ITEM_CODE1'].isin(['I410A', 'I410B'])]
        unselled_house_df = unselled_house_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE')
        unselled_house_df.columns.name = None
        unselled_house_df.columns = [f'미분양_{column}' for column in unselled_house_df.columns]

        approved_house_df = self.ecos_fetcher.fetch_item_value_df('901Y037', 'M', start_date, end_date)
        approved_house_df = approved_house_df[
            (approved_house_df['ITEM_CODE1'].str.startswith('I43AB')) & (approved_house_df['ITEM_CODE2'] == '1')
        ]
        approved_house_df = approved_house_df.pivot(index='TIME', columns='ITEM_NAME1', values='DATA_VALUE').loc[
            :, ['용도별', '주거용', '상업용']
        ]
        approved_house_df.columns.name = None
        approved_house_df.columns = [f'건축허가_{column}' for column in approved_house_df.columns]

        building_house_df = self.ecos_fetcher.fetch_item_value_df('901Y103', 'M', start_date, end_date)
        building_house_df = building_house_df[
            (building_house_df['ITEM_CODE2'].str.startswith('I47AB')) & (building_house_df['ITEM_CODE1'] == '1')
        ]
        building_house_df = building_house_df.pivot(index='TIME', columns='ITEM_NAME2', values='DATA_VALUE').loc[
            :, ['용도별', '주거용', '상업용']
        ]
        building_house_df.columns.name = None
        building_house_df.columns = [f'건축착공_{column}' for column in building_house_df.columns]
        house_info_df = pd.concat([unselled_house_df, approved_house_df, building_house_df], axis=1)
        return house_info_df
