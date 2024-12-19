import pandas as pd
import FinanceDataReader as finance_data_reader
from .KrxDataReader import KrxDataReader


class MarketDataReader:
    def __init__(self):
        self.finance_data_reader = finance_data_reader
        self.krx_data_reader = KrxDataReader()

    def get_kospi_info_df(self):
        """
        stock_name, stock_code, sector
        """
        kospi_sector_df = self.krx_data_reader.sector_data_reader.get_kospi_sector_df()
        kospi_sector_df['시가총액'] = kospi_sector_df['시가총액'].str.replace(',', '').astype(float)
        kospi_sector_df['종가'] = kospi_sector_df['종가'].str.replace(',', '').astype(float)
        kospi_sector_df['총주식수'] = (kospi_sector_df['시가총액'] / kospi_sector_df['종가']).astype(int)

        rename_dict = {
            '종목코드': 'stock_code',
            '종목명': 'stock_name',
            '업종명': 'sector',
            '총주식수': 'shares',
        }

        kospi_sector_df = kospi_sector_df.rename(columns=rename_dict)
        kospi_info_df = kospi_sector_df.loc[:, list(rename_dict.values())]
        return kospi_info_df

    def get_kospi_ohlcv_df(self, start_date, end_date):
        """
        date, open, high, low, close, volume, marcap
        """
        kospi_ohlcv_df = self.finance_data_reader.DataReader('KOSPI', start_date, end_date)

        kospi_ohlcv_df.columns = [col.lower() for col in kospi_ohlcv_df.columns]
        kospi_ohlcv_df.index.name = 'date'

        kospi_ohlcv_df = kospi_ohlcv_df.loc[:, ['open', 'high', 'low', 'close', 'volume', 'marcap']]
        return kospi_ohlcv_df

    def get_kospi_trader_df(self, start_date, end_date):
        """
        date, individual, foreign, corp
        """
        ###
        kospi_buy_trade_df = self.krx_data_reader.trader_data_reader.get_kospi_buy_trade_df(start_date, end_date)
        kospi_buy_trade_df = kospi_buy_trade_df.set_index('날짜')
        kospi_buy_trade_df = kospi_buy_trade_df.map(lambda x: x.replace(',', '')).astype(float)
        buy_trade_df = pd.concat(
            [
                kospi_buy_trade_df.loc[:, '전체'],
                kospi_buy_trade_df.loc[:, ['금융투자', '보험', '투신', '사모', '은행', '기타금융', '기타법인']]
                .sum(axis=1)
                .rename('기관'),
                kospi_buy_trade_df.loc[:, ['외국인', '기타외국인']].sum(axis=1).rename('외국인'),
                kospi_buy_trade_df.loc[:, '연기금'],
                kospi_buy_trade_df.loc[:, '개인'],
            ],
            axis=1,
        )
        buy_trade_df.columns = [col + '_매수' for col in buy_trade_df.columns]
        ###
        kospi_sell_trade_df = self.krx_data_reader.trader_data_reader.get_kospi_sell_trade_df(start_date, end_date)
        kospi_sell_trade_df = kospi_sell_trade_df.set_index('날짜')
        kospi_sell_trade_df = kospi_sell_trade_df.map(lambda x: x.replace(',', '')).astype(float)

        sell_trade_df = pd.concat(
            [
                kospi_sell_trade_df.loc[:, '전체'],
                kospi_sell_trade_df.loc[:, ['금융투자', '보험', '투신', '사모', '은행', '기타금융', '기타법인']]
                .sum(axis=1)
                .rename('기관'),
                kospi_sell_trade_df.loc[:, ['외국인', '기타외국인']].sum(axis=1).rename('외국인'),
                kospi_sell_trade_df.loc[:, '연기금'],
                kospi_sell_trade_df.loc[:, '개인'],
            ],
            axis=1,
        )
        sell_trade_df.columns = [col + '_매도' for col in sell_trade_df.columns]
        kospi_trade_df = pd.concat([buy_trade_df, sell_trade_df], axis=1)
        kospi_trade_df.index.name = 'date'

        kospi_trade_df.index = pd.to_datetime(kospi_trade_df.index, format='%Y/%m/%d')
        return kospi_trade_df

    def get_kosdaq_info_df(self):
        """
        stock_name, stock_code, sector
        """
        kosdaq_sector_df = self.krx_data_reader.sector_data_reader.get_kosdaq_sector_df()
        kosdaq_sector_df['시가총액'] = kosdaq_sector_df['시가총액'].str.replace(',', '').astype(float)
        kosdaq_sector_df['종가'] = kosdaq_sector_df['종가'].str.replace(',', '').astype(float)
        kosdaq_sector_df['총주식수'] = (kosdaq_sector_df['시가총액'] / kosdaq_sector_df['종가']).astype(int)

        rename_dict = {
            '종목코드': 'stock_code',
            '종목명': 'stock_name',
            '업종명': 'sector',
            '총주식수': 'shares',
        }

        kosdaq_sector_df = kosdaq_sector_df.rename(columns=rename_dict)
        kosdaq_info_df = kosdaq_sector_df.loc[:, list(rename_dict.values())]
        return kosdaq_info_df

    def get_kosdaq_ohlcv_df(self, start_date, end_date):
        """
        date, open, high, low, close, volume
        """
        kosdaq_ohlcv_df = self.finance_data_reader.DataReader('KOSDAQ', start_date, end_date)

        kosdaq_ohlcv_df.columns = [col.lower() for col in kosdaq_ohlcv_df.columns]
        kosdaq_ohlcv_df.index.name = 'date'

        kosdaq_ohlcv_df = kosdaq_ohlcv_df.loc[:, ['open', 'high', 'low', 'close', 'volume', 'marcap']]
        return kosdaq_ohlcv_df

    def get_kosdaq_trader_df(self, start_date, end_date):
        """
        date, individual, foreign, corp
        """
        kosdaq_buy_trade_df = self.krx_data_reader.trader_data_reader.get_kosdaq_buy_trade_df(start_date, end_date)
        kosdaq_buy_trade_df = kosdaq_buy_trade_df.set_index('날짜')
        kosdaq_buy_trade_df = kosdaq_buy_trade_df.map(lambda x: x.replace(',', '')).astype(float)
        buy_trade_df = pd.concat(
            [
                kosdaq_buy_trade_df.loc[:, '전체'],
                kosdaq_buy_trade_df.loc[:, ['금융투자', '보험', '투신', '사모', '은행', '기타금융', '기타법인']]
                .sum(axis=1)
                .rename('기관'),
                kosdaq_buy_trade_df.loc[:, ['외국인', '기타외국인']].sum(axis=1).rename('외국인'),
                kosdaq_buy_trade_df.loc[:, '연기금'],
                kosdaq_buy_trade_df.loc[:, '개인'],
            ],
            axis=1,
        )
        buy_trade_df.columns = [col + '_매수' for col in buy_trade_df.columns]
        ###
        kosdaq_sell_trade_df = self.krx_data_reader.trader_data_reader.get_kosdaq_sell_trade_df(start_date, end_date)
        kosdaq_sell_trade_df = kosdaq_sell_trade_df.set_index('날짜')
        kosdaq_sell_trade_df = kosdaq_sell_trade_df.map(lambda x: x.replace(',', '')).astype(float)

        sell_trade_df = pd.concat(
            [
                kosdaq_sell_trade_df.loc[:, '전체'],
                kosdaq_sell_trade_df.loc[:, ['금융투자', '보험', '투신', '사모', '은행', '기타금융', '기타법인']]
                .sum(axis=1)
                .rename('기관'),
                kosdaq_sell_trade_df.loc[:, ['외국인', '기타외국인']].sum(axis=1).rename('외국인'),
                kosdaq_sell_trade_df.loc[:, '연기금'],
                kosdaq_sell_trade_df.loc[:, '개인'],
            ],
            axis=1,
        )
        sell_trade_df.columns = [col + '_매도' for col in sell_trade_df.columns]
        kosdaq_trade_df = pd.concat([buy_trade_df, sell_trade_df], axis=1)
        kosdaq_trade_df.index.name = 'date'

        kosdaq_trade_df.index = pd.to_datetime(kosdaq_trade_df.index, format='%Y/%m/%d')
        return kosdaq_trade_df

    def get_stock_ohlcv_df(self, stock_code, start_date, end_date):
        """
        date, open, high, low, close, volume
        """
        stock_ohlcv_df = self.finance_data_reader.DataReader(stock_code, start_date, end_date)
        stock_ohlcv_df.columns = [col.lower() for col in stock_ohlcv_df.columns]
        stock_ohlcv_df.index.name = 'date'
        return stock_ohlcv_df

    def get_stocks_ohlcv_df(self, stock_codes, start_date, end_date):
        """
        date, open, high, low, close, volume
        """
        ohlcv_dfs = list()
        for stock_code in stock_codes:
            _ohlcv_df = self.finance_data_reader.DataReader(stock_code, start_date, end_date)
            _ohlcv_df['stock_code'] = stock_code
            ohlcv_dfs.append(_ohlcv_df)
        ohlcv_df = pd.concat(ohlcv_dfs, axis=0)
        ohlcv_df.columns = [col.lower() for col in ohlcv_df.columns]
        ohlcv_df.index.name = 'date'
        return ohlcv_df

    def get_stock_trader_df(self, stock_code, start_date, end_date):
        """
        date, individual, foreign, corp
        """
        stock_buy_trade_df = self.krx_data_reader.trader_data_reader.get_stock_buy_trade_df(stock_code, start_date, end_date)
        stock_buy_trade_df = stock_buy_trade_df.set_index('날짜')
        stock_buy_trade_df = stock_buy_trade_df.map(lambda x: x.replace(',', '')).astype(float)
        buy_trade_df = pd.concat(
            [
                stock_buy_trade_df.loc[:, '전체'],
                stock_buy_trade_df.loc[:, ['금융투자', '보험', '투신', '사모', '은행', '기타금융', '기타법인']]
                .sum(axis=1)
                .rename('기관'),
                stock_buy_trade_df.loc[:, ['외국인', '기타외국인']].sum(axis=1).rename('외국인'),
                stock_buy_trade_df.loc[:, '연기금'],
                stock_buy_trade_df.loc[:, '개인'],
            ],
            axis=1,
        )
        buy_trade_df.columns = [col + '_매수' for col in buy_trade_df.columns]
        ###
        stock_sell_trade_df = self.krx_data_reader.trader_data_reader.get_stock_sell_trade_df(stock_code, start_date, end_date)
        stock_sell_trade_df = stock_sell_trade_df.set_index('날짜')
        stock_sell_trade_df = stock_sell_trade_df.map(lambda x: x.replace(',', '')).astype(float)

        sell_trade_df = pd.concat(
            [
                stock_sell_trade_df.loc[:, '전체'],
                stock_sell_trade_df.loc[:, ['금융투자', '보험', '투신', '사모', '은행', '기타금융', '기타법인']]
                .sum(axis=1)
                .rename('기관'),
                stock_sell_trade_df.loc[:, ['외국인', '기타외국인']].sum(axis=1).rename('외국인'),
                stock_sell_trade_df.loc[:, '연기금'],
                stock_sell_trade_df.loc[:, '개인'],
            ],
            axis=1,
        )
        sell_trade_df.columns = [col + '_매도' for col in sell_trade_df.columns]
        stock_trade_df = pd.concat([buy_trade_df, sell_trade_df], axis=1)
        stock_trade_df.index.name = 'date'

        stock_trade_df.index = pd.to_datetime(stock_trade_df.index, format='%Y/%m/%d')
        return stock_trade_df
