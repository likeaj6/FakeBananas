from flask import Flask
from flask import request
from flask import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/claims", methods=['POST'])
def foo():
    data = [{'name': "CLAIM!!!", 'agree': "99%", 'disagree': "1%" }, { 'name': "Response #2", 'agree': "55%", 'disagree': "45%"}]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    # response.status_code = 201
    # response.headers['Access-Control-Allow-Origin'] = 'http://localhost'
    # response.headers['Access-Control-Allow-Methods'] = '*'
    # response.headers['Access-Control-Allow-Domain'] = '*'
    # response.headers['Access-Control-Allow-Credentials'] = True
    return response
if __name__ == '__main__':
    app.run()
