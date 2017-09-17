from eventregistry import *
from threading import Thread, Lock
from py_ms_cognitive import PyMsCognitiveWebSearch
import nltk
import numpy as np
import pandas as pd
import io, json

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

def main(args):
    web_scrape(args[1])

if __name__ == '__main__':
    web_scrape(sys.argv)
