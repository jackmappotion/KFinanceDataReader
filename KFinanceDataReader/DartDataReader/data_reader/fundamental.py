import pandas as pd
from ..fetcher import DartFetcher
from ..utils import get_chunked_list, safe_concat


class FundamentalDataReader(DartFetcher):
    def get_single_fundamental_df(self, corp_code, year, reprt):
        detail_url = 'api/fnlttSinglAcnt.json'
        resp = self.get_resp(detail_url, corp_code=corp_code, bsns_year=year, reprt_code=reprt)
        if resp:
            return self.resp2df(resp)
        else:
            return pd.DataFrame()

    def get_multi_fundamental_df(self, corp_codes, year, reprt):
        detail_url = "api/fnlttMultiAcnt.json"
        chunked_corps = get_chunked_list(corp_codes, 99)
        fundamentals_list = []
        for chunked_corp in chunked_corps:
            resp = self.get_resp(detail_url, corp_code=",".join(chunked_corp), bsns_year=year, reprt_code=reprt)
            resp_df = self.resp2df(resp)
            fundamentals_list.append(resp_df)
        return safe_concat(fundamentals_list)

    @staticmethod
    def resp2df(resp):
        try:
            resp_json = resp.json()
            resp_df = pd.DataFrame(resp_json["list"])
            return resp_df
        except:
            None
