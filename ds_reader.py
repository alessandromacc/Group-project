import pandas as pd
from dataset import Dataset
from abc import ABC, abstractclassmethod
import typing

class DatasetReader(ABC):
    '''General abstract interface for file readers, only takes path as optional argument since might come in handy
    with subclasses only bound to read text files; in other cases specific arguments will be required by the read method.'''
    def __init__(self, path: str = None):
        pass
    
    @abstractclassmethod
    def read(self):
        pass

class Gff3Reader(DatasetReader):
    '''Non abstract subclass of the abstract class DatasetReader, specifically designed for gff3 files.'''
    def __init__(self, path: str = None):
        super().__init__(path)
    
    @staticmethod
    def read(path: str, delimiter: str = '\t', comment: str = '#', names: str|list = ['Chromosome or scaffold name', 'Source', 'Type', 'Feature Start', 'Feature End', 'Score', 'Strand', 'Phase', 'Attributes']) -> Dataset:
        '''
        Only accepts a gff3 file as input.
        Static method relying on a Pandas reader to read a tabulated file and store data in a Dataset object;
        Parse as first parameter the location of the file, compliantly with those accepted by Pandas read_csv;
        Parse a delimiter character, by default tab, standard in gff3 files, but can be changed by the user;
        Parse the character meant to be found first in a commment line that should not be read by the reader, by default hash;
        Parse the list of names of the columns of the dataset you want to get, CHECK BLANKS MANAGEMENT.
        Returns a Dataset object.
        '''
        try:
            if path.split('.')[-1] == 'gff3':
                return Dataset(pd.read_csv(path, delimiter, comment=comment, names=names))
            else:
                raise TypeError('FileTypeError: a gff3 file was required')
        except TypeError:
            pass