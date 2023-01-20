import pandas as pd
from operations import *
import typing

class Dataset:
    '''Dataset class, wraps around a pandas DataFrame, each attribute is converted to a property,
    but no chance for modifying them is offered to the user.'''
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
        '''Verifies wether the requested operation is marked as active in the reference registry,
        returning a boolean value: True for active and vice versa. The queried property is set True
        as part of the mechanism that forces the user to execute any operation by means of the Dataset method
        execute.'''
        self.__queried = True
        return r.status_registry[op]
    
    def execute(self, r: OperationRegistry, op: str):
        '''Takes as arguments the registry where an operation is supposed to be found and the name of such operation,
        also retrievable as the name property of any operation. Looks into the registry for the operation and calls it,
        returning whatever the operation returns it. Only successfully executed if the operation is active and the
        operation name parsed is found in the registry.'''
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
    def __init__(self, status: bool = False, name: str = 'BasicInfo'):
        super().__init__(status, name)
    
    @staticmethod
    def operation(d: Dataset) -> list:
        if d.queried == True:
            cn = [i for i in d.dataframe.columns]
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

class ListID(Operation):
    def __init__(self, status: bool = False, name: str = 'ListID'):
        super().__init__(status, name)
    
    def operation(self, d: Dataset):
        if d.queried==True:
            types = pd.Series(d.dataframe['Type'].unique())
            return types