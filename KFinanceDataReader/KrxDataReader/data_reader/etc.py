from .base import DataReader

class EtcDataReader(DataReader):
    def __init__(self):
        super().__init__()
        
    def get_base_df(self):
        data = {
            "bld": "dbms/MDC/STAT/standard/MDCSTAT01901",
            "locale": "ko_KR",
            "mktId": "ALL",
            "share": "1",
            "csvxls_isNo": "false",
        }
        df = self.fetcher.fetch(data, 'OutBlock_1')
        df.columns = [
            '표준코드','단축코드','한글종목명','한글종목약명','영문종목명','상장일',
            '시장구분','증권구분','소속부','주식종류','액면가','상장주식수'
            ]
        return df

    def get_dividend_df(self):
        """배당 정보 추출"""
        data = {
            'bld': 'dbms/MDC/STAT/standard/MDCSTAT03501',
            'locale': 'ko_KR',
            'searchType': '1',
            'mktId': 'ALL',
            'trdDd': self.get_latest_weekday().strftime("%Y%m%d"),
            'csvxls_isNo': 'false',
        }
        df = self.fetcher.fetch(data, 'output')
        df = df.loc[:,['ISU_SRT_CD','ISU_ABBRV','TDD_CLSPRC','DPS']]
        df.columns = [
            '종목코드','종목명','종가','주당배당금'
            ]
        return df
