import pandas as pd
from .EcosDataReader import EcosDataReader


class MacroDataReader:
    def __init__(self, ecos_api_key):
        self.ecos_data_reader = EcosDataReader(ecos_api_key)

    def get_interest_rate_df(self, start_date, end_date):
        """
        금리 (기준금리, 예금금리, 대출금리)
        """
        df = self.ecos_data_reader.interest_data_reader.get_interest_rate_df(start_date, end_date)
        df.index.name = 'date'
        df = df.rename(columns={'기준금리': '기준금리', '수신금리': '예금금리', '대출금리': '대출금리'})

        df.index = pd.to_datetime(df.index, format='%Y%m')
        df = df.astype(float)
        return df

    def get_bond_yield_df(self, start_date, end_date):
        """
        채권 (국고채 3년 / 국고채 10년 / 국고채 20년)
        """
        df = self.ecos_data_reader.interest_data_reader.get_national_treasury_df(start_date, end_date)
        df.index.name = 'date'

        df.index = pd.to_datetime(df.index, format='%Y%m%d')
        df = df.astype(float)
        return df

    def get_exchange_rate_df(self, start_date, end_date):
        """
        환율 관련 (원/달러, 원/엔화, 원/위안, 원/유로)
        """
        df = self.ecos_data_reader.foreign_currency_data_reader.get_foreign_currency_df(start_date, end_date)
        df.index.name = 'date'

        df.index = pd.to_datetime(df.index, format='%Y%m%d')
        df = df.astype(float)
        return df

    def get_price_index_df(self, start_date, end_date):
        """
        물가 지수 (소비자 물가지수 / 생산자 물가지수 / 수출 물가지수 / 수입 물가지수)
        """
        ppi_df = self.ecos_data_reader.price_index_data_reader.get_ppi_df(start_date, end_date)
        cpi_df = self.ecos_data_reader.price_index_data_reader.get_cpi_df(start_date, end_date)
        export_pi_df = self.ecos_data_reader.price_index_data_reader.get_export_pi_df(start_date, end_date)
        import_pi_df = self.ecos_data_reader.price_index_data_reader.get_import_pi_df(start_date, end_date)
        df = pd.concat(
            [
                cpi_df.loc[:, ['총지수']].rename(columns={'총지수': '소비자물가지수'}),
                ppi_df.loc[:, ['총지수']].rename(columns={'총지수': '생산자물가지수'}),
                export_pi_df.loc[:, ['총지수']].rename(columns={'총지수': '수출물가지수'}),
                import_pi_df.loc[:, ['총지수']].rename(columns={'총지수': '수입물가지수'}),
            ],
            axis=1,
        )
        df.index.name = 'date'
        df.index = pd.to_datetime(df.index, format='%Y%m')
        df = df.astype(float)
        return df

    def get_trade_balance_df(self, start_date, end_date):
        """
        무역 (무역수지 / 수출 총지수 / 수출 총액 / 수입 총지수 / 수입 총액)
        """
        trade_balance_df = self.ecos_data_reader.trade_data_reader.get_trade_balance_df(start_date, end_date)
        export_country_df = self.ecos_data_reader.trade_data_reader.get_trade_export_country_df(start_date, end_date)
        export_product_df = self.ecos_data_reader.trade_data_reader.get_trade_export_product_df(start_date, end_date)
        import_country_df = self.ecos_data_reader.trade_data_reader.get_trade_import_country_df(start_date, end_date)
        import_product_df = self.ecos_data_reader.trade_data_reader.get_trade_import_product_df(start_date, end_date)
        df = pd.concat(
            [
                trade_balance_df.loc[:, ['경상수지']].rename(columns={'경상수지': '무역수지'}),
                export_product_df.loc[:, ['총지수']].rename(columns={'총지수': '수출_총지수'}),
                export_country_df.loc[:, ['국별수출(관세청)']].rename(columns={'국별수출(관세청)': '수출_총액'}),
                import_product_df.loc[:, ['총지수']].rename(columns={'총지수': '수입_총지수'}),
                import_country_df.loc[:, ['국별수입(관세청)']].rename(columns={'국별수입(관세청)': '수입_총액'}),
            ],
            axis=1,
        )
        df.index.name = 'date'
        df.index = pd.to_datetime(df.index, format='%Y%m')
        df = df.astype(float)
        return df
