from BSTNode import *
from CSVReader import *

from flask import Flask, session
from flask import url_for
from flask import render_template, jsonify
app = Flask(__name__)

@app.route('/')
def get():
    return render_template('index.html',data=vert)

@app.route('/table/<int:ad>')
def table(ad): 
    ls = readColumn('data.csv','Elo')

    root = BSTNode(ls[0])
    ls.append(ad)
    insertMany(root, ls)

    resPre, resIn, resPs = [], [], []
    preOr, preIn, prePs = orderAll(root, resPre, 'PRE'), orderAll(root, resIn, 'IN'), orderAll(root, resPs, 'POST')

    vert = {}
    map(resPre)
    indexMap(resIn, resPre,vert)
    
    return render_template('table.html',data=vert)

@app.route("/test")
def test():
    return render_template('ajax.html')

@app.route("/get_data")
def get_data():
    text = request.args.get('text')
    return text

if __name__ == '__main__':
    app.run(port=8080, debug=True)

