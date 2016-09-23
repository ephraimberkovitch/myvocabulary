from flask import Flask
import pymongo

app = Flask(__name__)

@app.route('/')
@app.route('/test')
def test():
    return "Hello, World!"

@app.route('/add_word/<word>/<translation>/<comment>',methods=['POST'])
def add_word(word,translation,comment):
    return "Hello, World!"

@app.route('/get_words',methods=['GET'])
def test():
    return "Hello, World!"

app.run()