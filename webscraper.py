from eventregistry import *
import numpy as np
import pandas as pd

# Print a list of recently added articles mentioning entered words
api_key = 'eda39267-9017-481a-860d-0b565c6d8bf3'
er = EventRegistry(apiKey = api_key)

list_of_articles = []
def get_articles(claim):
    
    #parse claim into a list of keywords
    keywords = claim
    print claim
    
    q = QueryArticlesIter(keywords=QueryItems.AND(keywords))
    
    for article in q.execQuery(er, sortBy = 'date'):
        data = {
            'source': article['source']['title'].encode('utf-8'),
            'title' : article['title'].encode('utf-8'),
            'url' : article['url'].encode('utf-8'),
            # 'text' : article['body'].encode('utf-8')
        }
        list_of_articles.append(data)
    
    df = pd.DataFrame()
    for article in list_of_articles:
        df = df.append(article,ignore_index=True)
    df.to_csv('articles.csv')
    
# parameter is a list of strings to query
get_articles(['mike','hostile','pompeo'])

df1 = pd.read_csv('articles.csv')
df1.columns = ['id','source','text',"""'title""" 'url']