from eventregistry import *
import numpy as np
import pandas as pd
import random
import os
import sys

# Print a list of recently added articles mentioning entered words
api_key = 'eda39267-9017-481a-860d-0b565c6d8bf3'
oldStdOut = sys.stdout
f = open(os.devnull, 'w')
sys.stdout = f
er = EventRegistry(apiKey = api_key)
sys.stdout = oldStdOut

def get_articles(keywords):
    q = QueryArticlesIter(keywords=QueryItems.AND(keywords))

    x = 0
    df = pd.DataFrame({'source':'test','url':'testing','text':'placeholers'}, index=[0])
    df.columns = ['source','url','text']

    for article in q.execQuery(er, sortBy = 'date'):
        data = {
            'source': article['source']['title'].encode('utf-8'),
#             'title' : article['title'].encode('utf-8'),
            'url' : article['url'].encode('utf-8'),
            'text' : article['body'].encode('utf-8')
        }
        df_temp = pd.DataFrame(data,index=[x])
        df = pd.concat([df,df_temp])
        x += 1
    return df

def get_keywords(user_url):
    url = user_url.decode('utf-8')
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    keywords_unicode = article.keywords
    keywords = []
    for word in keywords_unicode:
        keywords.append(word.encode('utf-8'))
    return keywords

def get_search_params(keywords):
    search_params = []
    while len(keywords) != 0:
        # Randomly select 3 words
        rm = random.sample(keywords,3)
        # add the list of 3 words to the searchable list
        search_params.append(rm)
        # remove words from the list
        for word in rm:
            keywords.remove(word)

        # put 1 or 2 random words back
        # if 3 words left just append to search_params
        if len(keywords) is 3:
            search_params.append(keywords)
            keywords = []
        # if no words left just exit
        elif len(keywords) is 0:
            keywords = []
        # if 1 word left, append 2 and search_params
        elif len(keywords) is 1:
            keywords.append(random.sample(rm,2)[0:2])
        else:
            keywords.append(random.sample(rm,1)[0])
    return search_params


df = pd.DataFrame({'source':'test','url':'testing','text':'placeholers'}, index=[0])
df.columns = ['source','url','text']
params = [['embassy', 'zone', 'decade'],['digging', 'expands', 'decade']]

for query in params:
    df = pd.concat([df,get_articles(query)])

df = df.drop(df.index[[0,1]])
df = df.reset_index(drop=True)

print(df.to_json(orient='index'))
