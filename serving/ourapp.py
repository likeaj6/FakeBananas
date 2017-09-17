from flask import Flask
# from flask import request
app = Flask(__name__)

# init all stuff here

@app.route("/")
def hello():
    return "hello world"

@app.route("/claims", methods=['POST'])
def foo():
    # put all code here
    return

if __name__ == '__main__':
    app.run()


