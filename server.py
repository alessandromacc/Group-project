from flask import Flask, render_template
from dataset import Dataset
from operations import *
from ds_reader import dataset_reader

myapp = Flask('webapp')
reg = OperationRegistry(BasicInfo())
df = dataset_reader()
@myapp.route('/')
def index():
    global reg, df
    return render_template('index.html', reg = reg)

@myapp.route('/basicInfo')
def basic_info():
    global reg, df
    bi = df.execute(reg, 'BasicInfo')
    return render_template('BasicInfo.html', bi=bi)


myapp.run()