from .data_reader.corp import CorpDataReader
from .data_reader.fundamental import FundamentalDataReader


class DartDataReader:
    def __init__(self, api_key):
        self.api_key = api_key
        self.corp_data_reader = CorpDataReader(api_key)
        self.fundamental_data_reader = FundamentalDataReader(api_key)
    
    
