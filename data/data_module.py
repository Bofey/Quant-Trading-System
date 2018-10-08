from util.database import DB_CONN
from datetime import datetime
from pymongo import  ASCENDING
from pandas import DataFrame

class DataModule:
    def __init__(self):
        pass
    def get_k_data(self,code=None,aufactor=None,index=False,begin_date=None,end_date=None):
        """
        Get stock or index daily data.
        :param aufactor:
        :param index:
        :param begin_date:
        :param end_date:
        :return: DataFrame,index=data,column
        """
        if code is None:
            return None
        if begin_date is None:
            begin_date = datetime.now().strftime('%Y-%m-%d')
        if end_date is None:
            end_date = begin_date
        if index:
            daily_cursor = DB_CONN['daily'].find(
                {'code':code,
                 'date':{'$gte':begin_date,'$lte':end_date}},
                sort=[('date',ASCENDING)]
            )
        else:
            collection = 'daily' if aufactor is None or aufactor == '' else 'daily_' + aufactor
            daily_cursor = DB_CONN[collection].find(
                {'code':code,'index':False,'date':{'$gte':begin_date,'$lte':end_date}},
                sort=[('date',ASCENDING)],
                projection={'_id':False}
            )
        df_daily = DataFrame()
        return df_daily

if __name__=='__main__':
    df_daily = DataModule().get_k_data(code='000001',index=True)
    print(df_daily,flush=True)
    df_daily = DataModule().get_k_data(code='000001', index=False,begin_date='2015-01-01',end_date='2015-01-10')

    print(df_daily,flush=True)