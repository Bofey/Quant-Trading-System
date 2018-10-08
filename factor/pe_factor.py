from base_factor import BaseFactor
from data.data_module import DataModule

class PEFactor(BaseFactor):
    def __init__(self):
        BaseFactor.__init__(self,'pe')

    def compute(self,begin_date,end_date):
        print(self.name,flush=True)

        dm =DataModule()
        df_daily = dm.get_k_data()
        print(df_daily)

if __name__ == '__main__':
   pe = PEFactor()
   pe.compute(None,None)