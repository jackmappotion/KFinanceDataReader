from ._macro_data_reader import MacroDataReader
from ._market_data_reader import MarketDataReader
from ._corp_data_reader import CorpDataReader


class KFinanceDataReader:
    def __init__(self):
        self.MacroDataReader = MacroDataReader
        self.MarketDataReader = MarketDataReader
        self.CorpDataReader = CorpDataReader
