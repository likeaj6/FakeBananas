from flask import Flask
from flask import request
from flask import json
from flask_cors import CORS
import webscraper
import tensorflow as tf
# our own packages
from ml import ourModel
from ml import util

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# INIT ALL ML
sess, test_set, keep_prob_pl, predict, features_pl = ml.loadML()

sess = loadML()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/claims", methods=['POST'])
def foo():
    inputType = json.loads(request.data)
    isURL = inputType['type'] == 'url'
    userInput = inputType['claim']
    sources = []
    if isURL:
        sources = webscraper.web_scrape(userInput)
    # data = [{'name': "CLAIM!!!", 'agree': "99%", 'disagree': "1%" }, { 'name': "Response #2", 'agree': "55%", 'disagree': "45%"}]
    response = app.response_class(
        response=json.dumps(sources),
        status=200,
        mimetype='application/json'
    )

    # run ML!
    # stances is a <List> of 0-3 classifications
    stances = ml.runModel(sess, test_set, keep_prob_pl, predict, features_pl)

    return response
if __name__ == '__main__':
    app.run()
