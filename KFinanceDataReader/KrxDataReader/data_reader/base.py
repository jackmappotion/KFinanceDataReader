import datetime as dt
from ..fetcher import KrxFetcher

class DataReader:
    def __init__(self):
        self.fetcher = KrxFetcher()

    @staticmethod
    def format_datetime(datetime_str):
        datetime_dt = dt.datetime.strptime(datetime_str, '%Y-%m-%d')
        return datetime_dt

    @staticmethod
    def get_latest_weekday():
        yesterday = dt.datetime.now() - dt.timedelta(days=1)
        # 주말 처리: 토요일(5)이면 금요일(-1), 일요일(6)이면 금요일(-2)
        if yesterday.weekday() == 5:  # 토요일
            latest_weekday = yesterday - dt.timedelta(days=1)
        elif yesterday.weekday() == 6:  # 일요일
            latest_weekday = yesterday - dt.timedelta(days=2)
        else:
            latest_weekday = yesterday
        return latest_weekday
    
    def split_date_ranges(self, start_date, end_date, years=2):
        start_date = self.format_datetime(start_date)
        end_date = self.format_datetime(end_date)
        ranges = []
        while start_date < end_date:
            range_end = start_date + dt.timedelta(days=years*365)
            if range_end > end_date:
                range_end = end_date
            ranges.append((start_date, range_end))
            start_date = range_end + dt.timedelta(days=1)
        return ranges