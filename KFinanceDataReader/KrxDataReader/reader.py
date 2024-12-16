import time
import datetime as dt

import pandas as pd

from .data_reader.etc import EtcDataReader
from .data_reader.sector import SectorDataReader
from .data_reader.trader import TraderDataReader
from .data_reader.foreign import ForeignDataReader

class KrxDataReader:
    def __init__(self) -> None:
        self.etc_data_reader = EtcDataReader()
        self.sector_data_reader = SectorDataReader()
        self.base_df = self.__get_base_df()
        self.trader_data_reader = TraderDataReader(self.__scode_lcode_dict)
        self.foreign_data_reader = ForeignDataReader(self.__scode_lcode_dict)
    
    def __get_base_df(self):
        """ 기본 정보 """
        base_df = self.etc_data_reader.get_base_df()
        self.__scode_lcode_dict = base_df.set_index('단축코드')['표준코드'].to_dict()
        return base_df