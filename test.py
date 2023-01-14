from ds_reader import dataset_reader, Dataset
from operations import *

reg = OperationRegistry(BasicInfo(name = 'BI'))
x = dataset_reader('Homo_sapiens.GRCh38.85.gff3')
y = x.execute(reg, 'BI')
print(y)
print(x.dataframe.head(40))
print(reg.registry['BI'])

