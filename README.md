# KFinanceDataReader

## Install
```
pip install KFinanceDataReader
```

## 요약

한국의 주요 금융 데이터 추출을 위한 library

- 거시경제 지표 [ECOS](https://ecos.bok.or.kr/api/#/)
- 시장 지표 [KRX](https://data.krx.co.kr/)
- 기업 재무제표 지표 [DART](https://dart.fss.or.kr/)

## 장점

본 프로젝트는 다양한 source의 금융데이터를 활용하기 편한 형식으로 수집한다.
1. 데이터 수집 파라미터 형식의 통일
2. 추출된 데이터 형식의 통일


## 요구사항
- 거시경제 지표 추출을 위해 `ECOS API KEY`가 필요하다.
- 기업 재무제표 지표 추출을 위해 `DART API KEY`가 필요하다.

## example을 확인하세용.

```py
from KFinanceDataReader import KFinanceDataReader

k_finance_data_reader = KFinanceDataReader()


# 거시 경제 지표(한국은행 API-KEY 필요)

MacroDataReader = k_finance_data_reader.MacroDataReader
macro_data_reader = MacroDataReader(ecos_api_key)

## 금리 (기준금리, 예금금리, 대출금리)
interest_rate_df = macro_data_reader.get_interest_rate_df(start_date, end_date)

## 채권 (국고채 1년 / 국고채 3년 / 국고채 5년 / 국고채 10년 / 국고채 20년)
bond_yield_df = macro_data_reader.get_bond_yield_df(start_date, end_date)

## 환율 관련 (원/달러, 원/엔화, 원/위안, 원/유로)
exchange_rate_df = macro_data_reader.get_exchange_rate_df(start_date, end_date)

## 물가 지수 (소비자 물가지수 / 생산자 물가지수 / 수출 물가지수 / 수입 물가지수)
price_index_df = macro_data_reader.get_price_index_df(start_date, end_date)

## 무역 (무역수지 / 수출 총지수 / 수출 총액 / 수입 총지수 / 수입 총액)
trade_balance_df = macro_data_reader.get_trade_balance_df(start_date, end_date)

"""------------------------------------------------------------------"""

# 시장 데이터
MarketDataReader = k_finance_data_reader.MarketDataReader
market_data_reader = MarketDataReader()


kospi_info_df = market_data_reader.get_kospi_info_df()
kospi_ohlcv_df = market_data_reader.get_kospi_ohlcv_df(start_date, end_date)
kospi_trader_df = market_data_reader.get_kospi_trader_df(start_date, end_date)

kosdaq_info_df = market_data_reader.get_kosdaq_info_df()
kosdaq_ohlcv_df = market_data_reader.get_kosdaq_ohlcv_df(start_date, end_date)
kosdaq_trader_df = market_data_reader.get_kosdaq_trader_df(start_date, end_date)

"""------------------------------------------------------------------"""

# 기업 재무제표 (DART API-KEY 필요)
CorpDataReader = k_finance_data_reader.CorpDataReader
corp_data_reader = CorpDataReader(dart_api_key)


reprt_codes = [
    '11011',  # 사업보고서
    '11012',  # 반기보고서
    '11013',  # 1분기보고서
    '11014',  # 3분기보고서
]
years = [
    '2024',
    '2023',
    '2022',
    '2021',
    '2020',
]

reprt_code = '11011'
year = '2023'

fundamentals_df = corp_data_reader.get_fundamentals_df(stock_codes, reprt_code, year)
```