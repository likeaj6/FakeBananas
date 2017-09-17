from flask import Flask
from flask import request
from flask import json
from flask_cors import CORS
import pandas as pd
# our own packages
from ml import ourModel
from ml import execnet
<<<<<<< HEAD
from rep import mlToOut
=======
from subprocess import call
>>>>>>> 0c159c7466da483265eeb84f30818c8fe6f77be2


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
<<<<<<< HEAD
        result = execnet.call_python_version("2.7", "webscraper", "web_scrape", [userInput])
        print(result)

        ############# ALL ML #############
=======
        arg1 = userInput
        exit_code = call("python2 watson_scraper.py url " + userInput, shell=True)
        print("Finished")
        # result = execnet.call_python_version("2.7", "webscraper", "web_scrape", [userInput])
        # print(result)

        # stances = ourModel.runModel(sess, keep_prob_pl, predict, features_pl, bow_vectorizer, tfreq_vectorizer, tfidf_vectorizer)

    # print(stances)

>>>>>>> 0c159c7466da483265eeb84f30818c8fe6f77be2
        newsData = pd.read_csv('url.csv')
        URLs = newsData['url'].tolist()
        SourceName = newsData['source'].tolist()
        BodyID = newsData['id'].tolist()

        # stances is a <List> of 0-3 classifications
        Stances = ourModel.runModel(sess, keep_prob_pl, predict, features_pl, bow_vectorizer, tfreq_vectorizer, tfidf_vectorizer)
        BodyID = range(len(Stances))
        ml_output = pd.DataFrame(
            {'BodyID': BodyID,
            'Stances': Stances,
            'SourceName': SourceName,
            'URL': URLs
            })
<<<<<<< HEAD
        print(Stances)

=======


    print(Stances)
>>>>>>> 0c159c7466da483265eeb84f30818c8fe6f77be2
    # data = [{'name': "CLAIM!!!", 'agree': "99%", 'disagree': "1%" }, { 'name': "Response #2", 'agree': "55%", 'disagree': "45%"}]
    response = app.response_class(
        response=json.dumps(sources),
        status=200,
        mimetype='application/json'
    )

    ########### Josh's Algs ############
    # returns a final confidence between -1 and 1
    final_score = mlToOut.mlToOut(ml_output)
    print("final score: %d", final_score)

    return response
if __name__ == '__main__':
    app.run()
