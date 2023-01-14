
from abc import ABC, abstractclassmethod
import pandas
import typing

class Operation(ABC):
    def __init__(self, status: bool = True, name: str = None):
        self.__status: bool = status
        self.__name: str = name
    
    @property
    def status(self) -> bool:
        return self.__status
    
    @property
    def name(self) -> str:
        return self.__name
    
    @status.setter
    def status(self, s: bool) -> None:
        self.__status: bool = s
    
    @abstractclassmethod
    def operation(self, d: pandas.DataFrame):
        pass

class BasicInfo(Operation):
    def __init__(self, status: bool = True, name: str = 'BasicInfo'):
        super().__init__(status, name)
    
    @staticmethod
    def operation(d: pandas.DataFrame) -> list:
        cn = [i for i in d.columns]
        return cn

class OperationRegistry:
    def __init__(self, *ops: Operation):
        self.__registry: dict = {i.name:i for i in ops}
        self.__status_registry: dict = {i.name:i.status for i in ops}
    
    @property
    def registry(self) -> dict:
        return self.__registry
    
    @property
    def status_registry(self) -> dict:
        return self.__status_registry



