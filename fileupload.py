from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template('Acknowledgement.html', name = f.filename)