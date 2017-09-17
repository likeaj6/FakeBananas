from eventregistry import *
from threading import Thread, Lock
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as Features
import pandas as pd
import json

# Print a list of recently added articles mentioning entered words
api_key = 'eda39267-9017-481a-860d-0b565c6d8bf3'
er = EventRegistry(apiKey = api_key)

global_df = pd.DataFrame()
mutex = Lock()

def get_articles(keywords):
    global global_df
    q = QueryArticlesIter(keywords=QueryItems.AND(keywords))
    q.setRequestedResult(RequestArticlesInfo(count= 199, sortBy="sourceImportance"))
    print keywords

    x = 0

    local_df = pd.DataFrame()

    res = er.execQuery(q)
    for article in res['articles']['results']:
        data = {
            'source': article['source']['title'].encode('utf-8'),
#             'title' : article['title'].encode('utf-8'),
            'url' : article['url'].encode('utf-8'),
            'text' : article['body'].encode('utf-8')
        }
        local_df = pd.concat([local_df, pd.DataFrame(data,index=[x])])
        x += 1

    mutex.acquire()
    try:
        global_df = pd.concat([global_df,local_df])
    finally:
        mutex.release()

def watson(user_url):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
      username="09b56387-57ee-4390-9365-a07a37706fb4",
      password="ISoTe5EueZJp",
      version="2017-02-27")

    response = natural_language_understanding.analyze(
      url=user_url,
      features=[
        Features.Keywords(
          emotion=False,
          sentiment=False,
            limit=15
        )
      ]
    )
    keywords = []
    for keyword in response['keywords']:
        if keyword['relevance'] > 0.80 and len(keywords) < 8:
            keywords.append(keyword['text'].encode('utf-8'))
    return keywords

class myThread(threading.Thread):
    def __init__(self, query):
        threading.Thread.__init__(self)
        self.query = query

    def run(self):
        get_articles(self.query)

def watson_scrape(url):
    global global_df
    keywords = watson(url)

    index = 0
    threads = []

    for query in keywords:
        threads.append(myThread(query))
        threads[index].start()
        index += 1
    for thread in threads:
        thread.join()
    global_df = global_df.reset_index(drop=True)
    # global_df.to_csv('watson_articles.csv')
    global_df['uid'] = range(len(global_df.index))
    return global_df.to_dict(orient='records')
