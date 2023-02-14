from BSTNode import *
from CSVReader import *

from flask import Flask, session
from flask import url_for
from flask import render_template, jsonify
app = Flask(__name__)

@app.route('/')
def get():
    return render_template('index.html',data=vert)

@app.route('/table')
def table():
    if 'table_data' not in session:  
        ls = readColumn('data.csv','Elo')

        root = BSTNode(ls[0])

        insertMany(root, ls)

        resPre, resIn, resPs = [], [], []
        preOr, preIn, prePs = orderAll(root, resPre, 'PRE'), orderAll(root, resIn, 'IN'), orderAll(root, resPs, 'POST')

        vert = {}
        map(resPre)
        indexMap(resIn, resPre,vert)
        
        session['table_data'] = cook
  
    return render_template('table.html',data=vert, cook=session['table_data'])

if __name__ == '__main__':
    app.run(port=8080, debug=True, threaded=True)

