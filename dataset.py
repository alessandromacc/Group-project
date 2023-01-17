import pandas as pd
from operations import *
import typing

class Dataset:
    def __init__(self, df: pd.DataFrame):
        self.__dataframe: pd.DataFrame = df
        self.__queried: bool = False
    
    @property
    def dataframe(self) -> pd.DataFrame:
        return self.__dataframe
    
    @property
    def queried(self) -> bool:
        return self.__queried
    
    def __query(self, r: OperationRegistry, op: str) -> bool:
        self.__queried = True
        return r.status_registry[op]
    
    def execute(self, r: OperationRegistry, op: str):
        try:
            if self.__query(r, op) == True:
                result = r.registry[op].operation(self)
                self.__queried = False
                return result
            else:
                self.__queried = False
                return 'Operation not active'
        except KeyError:
            return 'Not existing operation'

class BasicInfo(Operation):
    def __init__(self, status: bool = True, name: str = 'BasicInfo'):
        super().__init__(status, name)
    
    @staticmethod
    def operation(d: pandas.DataFrame) -> list:
        cn = [i for i in d.columns]
        return cn

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
