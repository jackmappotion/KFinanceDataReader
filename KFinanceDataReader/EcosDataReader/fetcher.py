import requests
import pandas as pd

import datetime as dt


class EcosFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://ecos.bok.or.kr/api'

    @staticmethod
    def _format_time(period, datetime_str):
        datetime_dt = dt.datetime.strptime(datetime_str, "%Y-%m-%d")
        if period == 'A':
            return datetime_dt.strftime("%Y")
        elif period == 'Q':
            quarter = (datetime_dt.month - 1) // 3 + 1
            return f"{datetime_dt.year}Q{quarter}"
        elif period == 'M':
            return datetime_dt.strftime("%Y%m")
        elif period == 'D':
            return datetime_dt.strftime("%Y%m%d")
        else:
            raise ValueError('Invalid Time')

    def _get_resp(self, params):
        query_params = '/'.join(params.values())
        url = f"{self.base_url}/{query_params}"
        resp = requests.get(url)
        return resp

    def fetch_stat_code_df(self):
        params = {
            "서비스명": "StatisticTableList",
            "인증키": self.api_key,
            "요청유형": "json",
            "언어구분": "kr",
            "요청시작건수": "1",
            "요청종료건수": "99999",
            # "통계표코드": 통계표코드,
        }
        resp = self._get_resp(params)
        stat_code_df = pd.DataFrame(resp.json()['StatisticTableList']['row'])
        return stat_code_df

    def fetch_item_code_df(self, stat_code):
        params = {
            "서비스명": "StatisticItemList",
            "인증키": self.api_key,
            "요청유형": "json",
            "언어구분": "kr",
            "요청시작건수": "1",
            "요청종료건수": "99999",
            "통계표코드": stat_code,
        }
        resp = self._get_resp(params)
        item_code_df = pd.DataFrame(resp.json()['StatisticItemList']['row'])
        return item_code_df

    def fetch_item_value_df(
        self,
        stat_code,
        period,
        start_date,
        end_date,
        통계항목코드1=None,
        통계항목코드2=None,
        통계항목코드3=None,
        통계항목코드4=None,
    ):
        params = {
            "서비스명": "StatisticSearch",
            "인증키": self.api_key,
            "요청유형": "json",
            "언어구분": "kr",
            "요청시작건수": "1",
            "요청종료건수": "99999",
            "통계표코드": stat_code,
            "주기": period,
            "검색시작일자": self._format_time(period, start_date),
            "검색종료일자": self._format_time(period, end_date),
            "통계항목코드1": '' if 통계항목코드1 is None else 통계항목코드1,
            "통계항목코드2": '' if 통계항목코드2 is None else 통계항목코드2,
            "통계항목코드3": '' if 통계항목코드3 is None else 통계항목코드3,
            "통계항목코드4": '' if 통계항목코드4 is None else 통계항목코드4,
        }
        resp = self._get_resp(params)
        item_code_df = pd.DataFrame(resp.json()['StatisticSearch']['row'])
        return item_code_df
