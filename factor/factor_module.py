from util.database import DB_CONN
from pandas import DataFrame

class FactorModule:
    def __init__(self):
        pass
    def get_stock_factor(self,code=None,factor=None,begin_date=None,end_date=None):
        """
        Get factor values of one stock between begin_date and end_date
        :param code:
        :param factor:
        :param begin_date:
        :param end_date:
        :return: DataFram
        """
        factor_cursor = DB_CONN[factor].find(
            {'name':factor,'date':{'$gte':begin_date,'$lte':end_date}})

        df_factor = DataFrame()

        return df_factor