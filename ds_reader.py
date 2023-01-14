import pandas as pd
from dataset import Dataset
import typing

def dataset_reader(path: str = 'Homo_sapiens.GRCh38.85.gff3', delimiter: str = '\t', comment: str = '#', names: str|list = ['Chromosome or scaffold name', 'Source', 'Type', 'Feature Start', 'Feature End', 'Score', 'Strand', 'Phase', 'Attributes']) -> pd.DataFrame:
    '''
    Global function relying on a Pandas reader to read a tabulated file and store data in a Dataset object (see Dataset documentation);
    Parse as first parameter the location of the file, compliantly with those accepted by Pandas read_csv;
    Parse a delimiter character, by default tab, standard in gff3 files, but can be changed by the user;
    Parse the character meant to be found first in a commment line that should not be read by the reader, by default hash;
    Parse the list of names of the columns of the dataset you want to get, CHECK BLANKS MANAGEMENT.

    Returns a Dataset object.
    '''
    return Dataset(pd.read_csv(path, delimiter=delimiter, comment=comment, names=names))


