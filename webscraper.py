from eventregistry import *
from newspaper import Article
from threading import Thread, Lock
import numpy as np
import pandas as pd
import io, json
import random

# Print a list of recently added articles mentioning entered words
api_key = 'eda39267-9017-481a-860d-0b565c6d8bf3'
er = EventRegistry(apiKey = api_key)

global_df = pd.DataFrame()
mutex = Lock()

def get_articles(keywords):
    global global_df
    q = QueryArticlesIter(keywords=QueryItems.AND(keywords))
    q.setRequestedResult(RequestArticlesInfo(count= 10, sortBy="sourceImportance"))
    # print keywords

    x = 0

    local_df = pd.DataFrame()

    res = er.execQuery(q)
    for article in res['articles']['results']:
        data = {
            'source': article['source']['title'].encode('utf-8'),
#             'title' : article['title'].encode('utf-8'),
            'url' : article['url'].encode('utf-8'),
            # 'text' : article['body'].encode('utf-8')
        }
        local_df = pd.concat([local_df, pd.DataFrame(data,index=[x])])
        x += 1

    mutex.acquire()
    try:
        global_df = pd.concat([global_df,local_df])
    finally:
        mutex.release()

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

def get_keywords(user_url):
    url = user_url.decode('utf-8')
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    keywords = article.keywords
    kl = []
    for word in keywords:
        kl.append(word.encode('utf-8'))
    return kl

class myThread(threading.Thread):
    def __init__(self, query):
        threading.Thread.__init__(self)
        self.query = query

    def run(self):
        get_articles(self.query)

def web_scrape(url):
    global global_df
    kl = get_keywords(url)
    params = get_search_params(kl)

    index = 0
    threads = []

    for query in params:
        threads.append(myThread(query))
        threads[index].start()
        index += 1
    for thread in threads:
        thread.join()



    # global_df = global_df.reset_index(drop=True)
    # with io.open('data.json', 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(global_df, ensure_ascii=False))
    global_df['id'] = range(len(global_df.index))
    bodies = global_df.loc[:,['id','text']]
    bodies.to_csv('ml/bodies.csv')
    claim = [claim] * len(global_df.index)
    claims = pd.DataFrame(claim)
    claims.to_csv('ml/claims.csv')
    urls = global_df.loc[:,['id','source','url']]
    urls.to_csv('url.csv')
    return global_df.to_dict(orient='records')

    # return global_df.to_json(orient='records')
