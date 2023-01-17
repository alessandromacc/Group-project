from flask import Flask, render_template
from dataset import *
from operations import *
from ds_reader import Gff3Reader

myapp = Flask('webapp')
reg = OperationRegistry(BasicInfo())
df = Gff3Reader.read('Homo_sapiens.GRCh38.85.gff3')
@myapp.route('/')
def index():
    global reg, df
    return render_template('index.html', reg = reg)

@myapp.route('/basicInfo')
def basic_info():
    global reg, df
    bi = df.execute(reg, 'BasicInfo')
    return render_template('BasicInfo.html', bi=bi)

@myapp.route('/FeaturesCount')
def features_count():
    global reg, df
    tdf = df.execute(reg, 'FeaturesCount')
    height = len(tdf.dataframe[0])
    return render_template('FeaturesCount.html', tdf = tdf, h = height)

myapp.run()