from eventregistry import *
import numpy as np
import pandas as pd
import random

# Print a list of recently added articles mentioning entered words



def get_articles(claim):
    
    #parse claim into a list of keywords
    keywords = claim
    list_of_articles = []
    
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
        if len(keywords) is 3:
            search_params.append(keywords)
            keywords = []
            print "this should be the last thing"
        elif len(keywords) is 1:
            keywords.append(random.sample(rm,2)[0:2])
        else:
            keywords.append(random.sample(rm,1)[0])
    return search_params


# parameter is a list of strings to query
get_articles(['mike','hostile','pompeo'])

df1 = pd.read_csv('articles.csv')
df1.columns = ['id','source','text',"""'title""" 'url']