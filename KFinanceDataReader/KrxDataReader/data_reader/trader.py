from .base import DataReader


class TraderDataReader(DataReader):
    def __init__(self, scode_lcode_dict):
        super().__init__()
        self.scode_lcode_dict = scode_lcode_dict

    def get_kospi_buy_trade_df(self, start_date, end_date):
        """코스피 매수 거래자 추출"""
        date_ranges = self.split_date_ranges(start_date, end_date, 2)
        data = self.get_market_trader_data()
        data['askBid'] = '2'
        data['mktId'] = 'STK'
        data['etf'] = 'EF'
        data['etn'] = 'EN'
        data['elw'] = 'EW'
        df = self.fetcher.fetch_with_date_ranges(data,'output', date_ranges)
        df.columns = [
            '날짜', '금융투자', '보험', '투신', '사모', '은행','기타금융', '연기금', '기타법인',
            '개인', '외국인','기타외국인', '전체'
            ]
        return df

    def get_kospi_sell_trade_df(self, start_date, end_date):
        """코스피 매도 거래자 추출"""
        date_ranges = self.split_date_ranges(start_date, end_date, 2)
        data = self.get_market_trader_data()
        data['askBid'] = '1'
        data['mktId'] = 'STK'
        data['etf'] = 'EF'
        data['etn'] = 'EN'
        data['elw'] = 'EW'
        df = self.fetcher.fetch_with_date_ranges(data,'output', date_ranges)
        df.columns = [
            '날짜', '금융투자', '보험', '투신', '사모', '은행','기타금융', '연기금', '기타법인',
            '개인', '외국인','기타외국인', '전체'
            ]
        return df

    def get_kosdaq_buy_trade_df(self, start_date, end_date):
        """코스닥 매수 거래자 추출"""
        date_ranges = self.split_date_ranges(start_date, end_date, 2)
        data = self.get_market_trader_data()
        data['askBid'] = '2'
        data['mktId'] = 'KSQ'
        df = self.fetcher.fetch_with_date_ranges(data,'output', date_ranges)
        df.columns = [
            '날짜', '금융투자', '보험', '투신', '사모', '은행','기타금융', '연기금', '기타법인',
            '개인', '외국인','기타외국인', '전체'
            ]
        return df

    def get_kosdaq_sell_trade_df(self, start_date, end_date):
        """코스닥 매도 거래자 추출"""
        date_ranges = self.split_date_ranges(start_date, end_date, 2)
        data = self.get_market_trader_data()
        data['askBid'] = '1'
        data['mktId'] = 'KSQ'
        df = self.fetcher.fetch_with_date_ranges(data,'output', date_ranges)
        df.columns = [
            '날짜', '금융투자', '보험', '투신', '사모', '은행','기타금융', '연기금', '기타법인',
            '개인', '외국인','기타외국인', '전체'
            ]
        return df

    def get_stock_buy_trade_df(self, scode, start_date, end_date):
        """주식 매수 거래자 추출"""
        date_ranges = self.split_date_ranges(start_date, end_date, 2)
        data = self.get_stock_trader_data()
        data['isuCd'] = self.scode_lcode_dict[scode]
        data['askBid'] = '2'
        df = self.fetcher.fetch_with_date_ranges(data,'output', date_ranges)
        df.columns = [
            '날짜', '금융투자', '보험', '투신', '사모', '은행','기타금융', '연기금', '기타법인',
            '개인', '외국인','기타외국인', '전체'
            ]
        return df

    def get_stock_sell_trade_df(self, scode, start_date, end_date):
        """주식 매도 거래자 추출"""
        date_ranges = self.split_date_ranges(start_date, end_date, 2)
        data = self.get_stock_trader_data()
        data['isuCd'] = self.scode_lcode_dict[scode]
        data['askBid'] = '1'
        df = self.fetcher.fetch_with_date_ranges(data,'output', date_ranges)
        df.columns = [
            '날짜', '금융투자', '보험', '투신', '사모', '은행','기타금융', '연기금', '기타법인',
            '개인', '외국인','기타외국인', '전체'
            ]
        return df

    def get_market_trader_data(self):
        data = {
            'bld': 'dbms/MDC/STAT/standard/MDCSTAT02203',
            'locale': 'ko_KR',
            'inqTpCd': '2',
            'trdVolVal': '2',
            'detailView': '1',
            'money': '3',
            'csvxls_isNo': 'false',
        }
        return data

    def get_stock_trader_data(self):
        data = {
            'bld': 'dbms/MDC/STAT/standard/MDCSTAT02303',
            'locale': 'ko_KR',
            'inqTpCd': '2',
            'trdVolVal': '2',
            'detailView': '1',
            'money': '3',
            'csvxls_isNo': 'false',
        }
        return data
