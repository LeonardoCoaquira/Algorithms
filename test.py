from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('ajax.html')

@app.route('/submit', methods=['POST'])
def submit():
    text_input = request.form['text-input']
    return text_input

if __name__ == '__main__':
    app.run(port=8080, debug=True)