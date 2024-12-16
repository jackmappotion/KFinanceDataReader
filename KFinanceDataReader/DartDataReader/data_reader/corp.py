import pandas as pd
import zipfile
import xmltodict
from io import BytesIO
from ..fetcher import DartFetcher

class CorpDataReader(DartFetcher):
    def get_corp_df(self):
        resp = self.get_resp('api/corpCode.xml')
        if resp:
            resp_dict = self.resp2dict(resp)
            resp_df = pd.DataFrame(resp_dict['result']['list'])
            return resp_df
        return None

    @staticmethod
    def resp2dict(resp) -> dict:
        """
        input : bytes (zip file -> that contains COPRCODE.xml)
        return : dict
        """
        with zipfile.ZipFile(BytesIO(resp.content)) as zip_r:
            with zip_r.open('CORPCODE.xml') as f:
                resp_dict = xmltodict.parse(f.read())
        return resp_dict