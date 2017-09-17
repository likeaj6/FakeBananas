# This is the main python file that aggregates all our seperate soruces.

# import numpy as np
import pandas as pd
# import local packages
# import ml
# import rep
import webscraper
print("Pipeline running...")

##################
## WEB SCRAPING ##
##################

# the following line take a url in a string as input
# example:
url = 'http://abcnews.go.com/US/wireStory/hurricanes-teach-us-ap-finds-fast-coastal-growth-49893843'
# webscraper.web_scrape(url)
webscraper.web_scrape(url)
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

print(ml_output.loc[0,'Stances'])
print(ml_output.loc[1,'Stances'])



########################
## REPUTATION SYSTEMS ##
########################
rep.loadDefaultReputations()
rep.mlToOut(ml_output)


print("Pipeline complete")
