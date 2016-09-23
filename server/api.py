from flask import Flask
import json
import pymongo

app = Flask(__name__)

@app.route('/')
@app.route('/test')
def test():
    return "Hello, World!"

@app.route('/add_word/<word>/<translation>/<comment>',methods=['POST'])
def add_word(word,translation,comment):
    client = pymongo.MongoClient()
    db = client.myvocabulary
    db.words.insert({'word':word,'translation':translation,'comment':comment})
    return "{'result':'OK'}"

@app.route('/get_words',methods=['GET'])
def get_words():
    client = pymongo.MongoClient()
    db = client.myvocabulary
    words = db.words
    result = words.find()
    return json.dumps(result)

app.run()