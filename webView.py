from BSTNode import *
from CSVReader import *

ls = readColumn('data.csv','Elo')

root = BSTNode(ls[0])

insertMany(root, ls)

resPre, resIn, resPs = [], [], []
preOr, preIn, prePs = orderAll(root, resPre, 'PRE'), orderAll(root, resIn, 'IN'), orderAll(root, resPs, 'POST')

vert = {}
map(resPre)
indexMap(resIn, resPre,vert)
view = printMapTwo(vert)

from flask import Flask
from flask import url_for
from flask import render_template, jsonify
app = Flask(__name__)

@app.route('/')
def get():
    return render_template('index.html',data=vert)

@app.route('/table')
def table():
    return render_template('table.html', size=len(vert), data=vert)

if __name__ == '__main__':
    app.run(port=8080, debug=True, threaded=True)

