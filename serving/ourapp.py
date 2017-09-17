from flask import Flask
# from flask import request
# import numpy as np
import pandas as pd
# import local packages
# import ml
import rep

app = Flask(__name__)

# init all stuff here

@app.route("/")
def hello():
    return "hello world"

@app.route("/claims", methods=['POST'])
def foo():
    # PUT ALL 'EVERY RUN' CODE HERE
    print("Pipeline running...")

    ##################
    ## WEB SCRAPING ##
    ##################

    # example call to python2 file:
    # result = call_python_version("2.7", "module(folder_name)", "filename.py", "function_name", ["param1", "param2"])

    ######################
    ## MACHINE LEARNING ##
    ######################

    # runs predictions and outputs a .csv file
    # predictions is a list of 0-4 for agree/dis..etc.

    # stances = ml.mlPred()
    stances = [1,2,3,2,3,3,2,2,3,1,0,0,2,3]
    bodyID = range(len(stances))
    sourceNames = range(len(stances))
    urls = range(len(stances))

    ml_output = pd.DataFrame(
            {'BodyID': bodyID,
                'Stances': stances,
                'SourceName': sourceNames,
                'URL': urls
                })

    print(ml_output)


    ########################
    ## REPUTATION SYSTEMS ##
    ########################
    rep.loadDefaultReputations()

    print("Pipeline complete")
    return



if __name__ == '__main__':
    app.run()


