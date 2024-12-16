from .base import DataReader

class SectorDataReader(DataReader):
    def __init__(self):
        super().__init__()

    def get_kospi_sector_df(self):
        """코스피 sector 정보"""
        data = {
            'bld': 'dbms/MDC/STAT/standard/MDCSTAT03901',
            'locale': 'ko_KR',
            'mktId': 'STK',
            'trdDd': self.get_latest_weekday().strftime("%Y%m%d"),
            'money': '1',
            'csvxls_isNo': 'false',
        }
        df = self.fetcher.fetch(data, 'block1')
        df = df.iloc[:,:-1]
        df.columns = [
            '종목코드','종목명','시장구분','업종명','종가','대비','등락률','시가총액'
            ]
        return df

    def get_kosdaq_sector_df(self):
        """코스닥 sector 정보"""
        data = {
            'bld': 'dbms/MDC/STAT/standard/MDCSTAT03901',
            'locale': 'ko_KR',
            'mktId': 'KSQ',
            # 'segTpCd': 'ALL',
            'trdDd': self.get_latest_weekday().strftime("%Y%m%d"),
            'money': '1',
            'csvxls_isNo': 'false',
        }
        df = self.fetcher.fetch(data, 'block1')
        df = df.iloc[:,:-1]
        df.columns = [
            '종목코드','종목명','시장구분','업종명','종가','대비','등락률','시가총액'
            ]
        return df
