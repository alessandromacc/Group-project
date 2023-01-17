import pandas as pd
from operations import *
import typing

class Dataset:
    def __init__(self, df: pd.DataFrame):
        self.__dataframe: pd.DataFrame = df
        self.__col_names: list = [i for i in self.__dataframe.columns]
    
    @property
    def dataframe(self) -> pd.DataFrame:
        return self.__dataframe
    
    @property
    def col_names(self) -> list:
        return self.__col_names
    
    def __query(self, r: OperationRegistry, op: str) -> bool:
        return r.status_registry[op]
    
    def execute(self, r: OperationRegistry, op: str):
        try:
            if self.__query(r, op) == True:
                return r.registry[op].operation(self.dataframe)
            else:
                return 'Operation not active'
        except KeyError:
            return 'Not existing operation'

class FeaturesCount(Operation):
    def __init__(self, status: bool = False, name: str = 'FeaturesCount'):
        super().__init__(status, name)
    
    def operation(self, d: Dataset):
        if d.queried == True:
            col = d.dataframe['Source']
            counter = {}
            for i in col:
                if i not in ['.', 'GRCh38']:
                    counter[i] = counter.get(i, 0) + 1
            result = Dataset(pandas.DataFrame([j,k] for j,k in counter.items()))
            return result
