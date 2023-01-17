from ds_reader import *
from operations import *
from dataset import *

reg = OperationRegistry(BasicInfo(name = 'BI'))
x = Gff3Reader.read('Homo_sapiens.GRCh38.85.gff3')
y = x.execute(reg, 'BI')
print(y)
print(x.dataframe.head(40))
print(reg.registry['BI'])

