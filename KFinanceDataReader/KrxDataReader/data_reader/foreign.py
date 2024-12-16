from ..fetcher import KrxFetcher
from .base import DataReader

class ForeignDataReader(DataReader):
    def __init__(self, scode_lcode_dict):
        super().__init__()
        self.scode_lcode_dict = scode_lcode_dict
    
    def get_kospi_foreign_hold_df(self, start_date, end_date):
        """코스피 외국인 보유량"""
        date_ranges = self.split_date_ranges(start_date, end_date, 2)
        data = self.get_market_foreign_hold_data()
        data['mktId'] = 'STK'
        
        df = self.fetcher.fetch_with_date_ranges(data,'block1', date_ranges)
        df.columns = [
            '날짜','전체_시가총액','외국인_시가총액','외국인_시가총액_비율','전체_주식수','외국인_주식수','외국인_주식수_비율'
            ]
        return df

    def get_kosdaq_foreign_hold_df(self, start_date, end_date):
        """코스닥 외국인 보유량"""
        date_ranges = self.split_date_ranges(start_date, end_date, 2)
        data = self.get_market_foreign_hold_data()
        data['mktId'] = 'KSQ'
        
        df = self.fetcher.fetch_with_date_ranges(data,'block1', date_ranges)
        df.columns = [
            '날짜','전체_시가총액','외국인_시가총액','외국인_시가총액_비율','전체_주식수','외국인_주식수','외국인_주식수_비율'
            ]
        return df

    def get_stock_foreign_hold_df(self, scode, start_date, end_date):
        """주식 외국인 보유량"""
        date_ranges = self.split_date_ranges(start_date, end_date, 2)
        data = self.get_stock_foreign_hold_data()
        data['isuCd'] = self.scode_lcode_dict[scode]
        df = self.fetcher.fetch_with_date_ranges(data, 'output', date_ranges)
        df = df.drop(columns=['FLUC_TP_CD'])
        df.columns = [
            '날짜','종가','대비','등락률','전체_주식수','외국인_주식수','외국인_주식수_비율','외국인_한도수량','외국인_한도소진율'
            ]
        return df

    def get_market_foreign_hold_data(self):
        data = {
            'bld': 'dbms/MDC/STAT/standard/MDCSTAT03601',
            'locale': 'ko_KR',
            'segTpCd': 'ALL',
            'share': '2',
            'money': '3',
            'csvxls_isNo': 'false',
        }
        return data

    def get_stock_foreign_hold_data(self):
        data = {
            'bld': 'dbms/MDC/STAT/standard/MDCSTAT03702',
            'locale': 'ko_KR',
            'searchType': '2',
            'mktId': 'ALL',
            'param1isuCd_finder_stkisu0_1': 'ALL',
            'share': '1',
            'csvxls_isNo': 'false',
        }
        return data
