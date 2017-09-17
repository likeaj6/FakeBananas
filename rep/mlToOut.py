import csv

class opinion:
    def __init__(self, sourceName, articleId, stance):
        self.sourceName = sourceName
        self.articleId = articleId
        self.stance = stance

class source:
    """articles #list of strings
    size #int
    reputation #number between -1 and 1 inclusive"""
    def __init__(self, sourceName, reputation):
        self.sourceName = sourceName
        self.reputation = reputation
        self.size = 0
        self.articles = []
    def addArticle(self, articleId, articleValidity):
        if not articleId in self.articles:
            self.reputation = (self.reputation*self.size+articleValidity)/(self.size+1)
            self.articles.append(articleId)
            self.size += 1

class globals:
    defaultReputations = {
        'trump' : -1,
        'buzzfeed' : -.96,
        'breitbart' : -.92,
        'infowars' : -.7,
        'yahoo' : -.6,
        'occupy democrats' : -6,
        'the onion' : -.6,
        'huffington post' : -.55,
        'blaze' : -.55,
        'fox' : -.5,
        'the sean hannity show' : -.5,
        'the blaze' : -.45,
        'people magazine' : -.4,
        'the rush limbaugh show' : -.3,
        'abc' : -.25,
        'msnbc' : -.2,
        'drudge report' : -.1,
        'nbc' : -.1,
        'cbs' : 0,
        'the daily show' : 0,
        'google news' : .05,
        'the atlantic' : .23,
        'usa today' : .27,
        'the colbert report' : .3,
        'slate' : .4,
        'thinkprogress' : .45,
        'kansas city star' : .5,
        'cnn' : .5,
        'the ed shultz show' : .5,
        'time' : .6,
        'washington post' : .64,
        'mother jones' : .65,
        'denver post' : .66,
        'bloomberg' : .7,
        'politico' : .75,
        'seattle times' : .75,
        'local' : .75,
        'dallas morning news' : .75,
        'latimes' : .76,
        'wall street journal' : .76,
        'guardian' : .77,
        'pbs' : .8,
        'bbc' : .8,
        'al jazeera' : .85,
        'npr' : .9,
        'associated press' : .9,
        'reuters' : .9,
        'economist' : 1,
    }
    sources = {'New York Times' : source('New York Times', 1)}

def mlToOut(mlOut):
    """takes the output of our ml and turns it into a final stances
    :param mlOut: a panda dataframe
    """
    for index, row in mlOut.iterrows():
        stance = row['Stances']
        articleId = row['BodyID']
        sourceName = row['SourceName']
        op = opinion(sourceName, articleId, stance)
        if index == 0:
            opinions = [op]
        else:
            opinions.append(op)
    stance = avgStance(opinions)
    updateRep(opinions)
    return stance

def avgStance(opinions):
    """takes a list of opinions and calculates the final stance
    :param opinions: a list<opinion> of all opinions to average
    """
    """finalStance #to hold our final stance"""
    finalStance = 0
    for op in opinions:
        print(type(op))
        #disagree
        if op.stance == 0:
            if op.sourceName in globals.sources:
                finalStance -= globals.sources.get(op.sourceName).reputation
        #agree
        if op.stance == 1:
            if op.sourceName in globals.sources:
                finalStance += globals.sources.get(op.sourceName).reputation
        #unrelated
        #if op.stance == 2 do nothing
        #discuss
        if op.stance == 3:
            if op.sourceName in globals.sources:
                finalStance += globals.sources.get(op.sourceName).reputation/4
    finalStance = finalStance/len(opinions)
    return finalStance

def compareStance(opinion, opinions):
    """compares an article with other articles to determine its reputability
    :param opinion: the article who's validity is to be determined
    :param opinions: the articles to check the article in question against
    """
    finalStance = 0
    for op in opinions:
        if op.sourceName in globals.sources:
            #disagree
            if op.stance == 0:
                if opinion.stance == 0:
                    finalStance += globals.sources.get(op.sourceName).reputation
                elif opinion.stance == 1:
                    finalStance -= globals.sources.get(op.sourceName).reputation
            #agree
            if op.stance == 1:
                if opinion.stance == 1:
                    finalStance += globals.sources.get(op.sourceName).reputation
                elif opinion.stance == 0:
                    finalStance -= globals.sources.get(op.sourceName).reputation
    finalStance = finalStance/len(opinions)
    return finalStance

def updateRep(opinions):
    for op in opinions:
        if not op.sourceName in globals.sources:
            globals.sources.update({op.sourceName : source(op.sourceName, 0)})
        globals.sources.get(op.sourceName).addArticle(op.articleId, compareStance(op, opinions))

def loadReputations(reputations):
    for k,v in reputations.items():
        globals.sources.update({k : source(k, v)})

def loadDefaultReputations():
    loadReputations(globals.defaultReputations)

def readFromDisk():
    with open('reputationDict.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            reputations.update(row['source'], row['reputation'])

def writeToDisk():
    with open('reputationDict.csv', 'w') as csvfile:
        fieldnames = ['source', 'reputation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for k,v in reputations.items():
            writer.writerow({'source': k, 'reputation': v})
