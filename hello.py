from flask import Flask
from flask import request
from flask import json
from flask_cors import CORS
import webscraper

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

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
    return response
if __name__ == '__main__':
    app.run()
