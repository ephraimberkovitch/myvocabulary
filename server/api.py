from flask import Flask, jsonify
import json
import pymongo
from bson.objectid import ObjectId

def newEncoder(o):
    if type(o) == ObjectId:
        return str(o)
    return o.__str__


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
    words = list(db.words.find({}))
    return json.dumps(words,default=newEncoder)

app.run()