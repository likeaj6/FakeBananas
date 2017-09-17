from flask import Flask
from flask import request
from flask import json
from flask_cors import CORS
import pandas as pd
# import webscraper
# our own packages
from ml import ourModel
from ml import execnet
from subprocess import call


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# INIT ALL ML
# print("loading tensorflow  model")
# sess, keep_prob_pl, predict, features_pl, bow_vectorizer, tfreq_vectorizer, tfidf_vectorizer = ourModel.loadML()

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
        print("Calling webscraper!")
        # sources = webscraper.web_scrape(userInput)
        arg1 = userInput
        exit_code = call("python2 watson_scraper.py url " + userInput, shell=True)
        print("Finished")
        # result = execnet.call_python_version("2.7", "webscraper", "web_scrape", [userInput])
        # print(result)

        # stances = ourModel.runModel(sess, keep_prob_pl, predict, features_pl, bow_vectorizer, tfreq_vectorizer, tfidf_vectorizer)

    # print(stances)

        newsData = pd.read_csv('url.csv')
        URLs = newsData['url'].tolist()
        SourceName = newsData['source'].tolist()
        BodyID = newsData['id'].tolist()

        Stances = ourModel.runModel(sess, keep_prob_pl, predict, features_pl, bow_vectorizer, tfreq_vectorizer, tfidf_vectorizer)
        BodyID = range(len(Stances))
        ml_output = pd.DataFrame(
            {'BodyID': BodyID,
            'Stances': Stances,
            'SourceName': SourceName,
            'URL': URLs
            })


    print(Stances)
    # data = [{'name': "CLAIM!!!", 'agree': "99%", 'disagree': "1%" }, { 'name': "Response #2", 'agree': "55%", 'disagree': "45%"}]
    response = app.response_class(
        response=json.dumps(sources),
        status=200,
        mimetype='application/json'
    )

    # run ML!
    # stances is a <List> of 0-3 classifications


    return response
if __name__ == '__main__':
    app.run()
