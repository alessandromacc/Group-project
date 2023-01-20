from flask import Flask, render_template
from dataset import *
from operations import *
from ds_reader import Gff3Reader

'''Server page with the Flask code'''

myapp = Flask('webapp')

'''Define the operation registry with all the operations instances needed in the webpage.'''
reg = OperationRegistry(BasicInfo(), FeaturesCount(), ListID())

'''Use the Gff3Reader class to read a gff3 file and store it into a Dataset object,
pass as argument the path to the gff3 file.'''
df = Gff3Reader.read('/Users/Alessandro/Desktop/Uni/2° year/Advanced Programming/group pj-local/Homo_sapiens.GRCh38.85.gff3')

@myapp.route('/')
def index():
    '''Homepage, parse for jinja rendering the registry'''
    global reg, df
    return render_template('index.html', reg = reg)

@myapp.route('/basicInfo')
def basic_info():
    '''Operation page, parse for jinja rendering just the value of the executed method'''
    global reg, df
    bi = df.execute(reg, 'BasicInfo')
    return render_template('BasicInfo.html', bi=bi)

@myapp.route('/FeaturesCount')
def features_count():
    '''Operation page, parse for jinja rendering the value of the executed method'''
    global reg, df
    tdf = df.execute(reg, 'FeaturesCount')
    height = len(tdf.dataframe[0])
    return render_template('FeaturesCount.html', tdf = tdf, h = height)

@myapp.route('/ListID')
def list_IDs():
    '''Operation page, displays the list of unique IDs found in the genome annotation'''
    global reg, df
    types = df.execute(reg, 'ListID')
    return render_template('ListID.html', types = types)

myapp.run()