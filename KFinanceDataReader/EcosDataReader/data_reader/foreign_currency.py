import pandas as pd
from ._data_reader import _DataReader


class ForeignCurrencyDataReader(_DataReader):

    def get_foreign_currency_df(self, start_date, end_date):
        won_dollar = self.ecos_fetcher.fetch_item_value_df('731Y001', 'D', start_date, end_date, '0000001')
        won_dollar = self.df2series(won_dollar, '원_달러')

        won_yen = self.ecos_fetcher.fetch_item_value_df('731Y001', 'D', start_date, end_date, '0000002')
        won_yen = self.df2series(won_yen, '원_엔')

        won_euro = self.ecos_fetcher.fetch_item_value_df('731Y001', 'D', start_date, end_date, '0000003')
        won_euro = self.df2series(won_euro, '원_유로')

        won_yuan = self.ecos_fetcher.fetch_item_value_df('731Y001', 'D', start_date, end_date, '0000053')
        won_yuan = self.df2series(won_yuan, '원_위안')

        foreign_currency_df = pd.concat([won_dollar, won_yen, won_euro, won_yuan], axis=1)
        return foreign_currency_df
