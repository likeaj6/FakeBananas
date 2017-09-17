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
        self.size = 0 #number of articles from source
        self.sourceName = sourceName
        self.reputation = reputation
    def addArticle(articleId, articleValidity):
        if not articles.contains(opinion.articleId):
            reputation = (reputation*size+articleValidity)/(size+1)
            articles.append(articleId)
            size += 1

class globals:
    defaultReputations = {
        'Trump' : -1,
        'Buzzfeed' : -.96,
        'Breitbart' : -.92,
        'Infowars' : -.7,
        'Yahoo' : -.6,
        'Occupy Democrats' : -6,
        'The Onion' : -.6,
        'Huffington Post' : -.55,
        'Blaze' : -.55,
        'Fox' : -.5,
        'The Sean Hannity Show' : -.5,
        'The Blaze' : -.45,
        'People Magazine' : -.4,
        'The Rush Limbaugh Show' : -.3,
        'ABC' : -.25,
        'MSNBC' : -.2,
        'Drudge Report' : -.1,
        'NBC' : -.1,
        'CBS' : 0,
        'The Daily Show' : 0,
        'Google News' : .05,
        'The Atlantic' : .23,
        'USA Today' : .27,
        'The Colbert Report' : .3,
        'Slate' : .4,
        'ThinkProgress' : .45,
        'Kansas City Star' : .5,
        'CNN' : .5,
        'The Ed Shultz Show' : .5,
        'Time' : .6,
        'Washington Post' : .64,
        'Mother Jones' : .65,
        'Denver Post' : .66,
        'Bloomberg' : .7,
        'Politico' : .75,
        'Seattle Times' : .75,
        'Local' : .75,
        'Dallas Morning News' : .75,
        'LaTimes' : .76,
        'Wall Street Journal' : .76,
        'Guardian' : .77,
        'PBS' : .8,
        'BBC' : .8,
        'Al Jazeera' : .85,
        'NPR' : .9,
        'Associated Press' : .9,
        'Reuters' : .9,
        'Economist' : 1,
    }
    sources = {'New York Times' : source('New York Times', 1)}

def mlToOut(mlOut):
    """takes the output of our ml and turns it into a final stances
    :param mlOut: a panda dataframe
    """
    """opinions #list of type opinion"""
    for row in mlOut.rows:
        stance = row['Stances']
        articleId = row['BodyID']
        sourceName = row['SourceName']
        op = opinion(sourceName, articleId, stance)
        opinions.append(op)
    stance = avgStance(opinions)
    reputations.updateRep(opinions)
    return stance

def avgStance(opinions):
    """takes a list of opinions and calculates the final stance
    :param opinions: a list<opinion> of all opinions to average
    """
    """finalStance #to hold our final stance"""
    for op in opinions:
        print(type(op))
        #disagree
        if op.stance == 0:
            if reputations.contains(op.sourceName):
                finalOpinion -= globals.sources.get(op.sourceName).reputation
        #agree
        if op.stance == 1:
            if reputations.contains(op.sourceName):
                finalOpinion += globals.sources.get(op.sourceName).reputation
        #unrelated
        #if op.stance == 2 do nothing
        #discuss
        if op.stance == 3:
            if reputations.contains(op.sourceName):
                finalOpinion += globals.sources.get(op.sourceName).reputation/4
    return finalStance/opinions.size

def compareStance(opinion, opinions):
    """compares an article with other articles to determine its reputability
    :param opinion: the article who's validity is to be determined
    :param opinions: the articles to check the article in question against
    """
    """finalStance"""
    for op in opinions:
        #disagree
        if op.stance == 0:
            if opinion.stance == 0:
                finalOpinion += globals.sources.get(op.sourceName).reputation
            elif opinion.stance == 1:
                finalOpinion -= globals.sources.get(op.sourceName).reputation
        #agree
        if op.stance == 1:
            if opinion.stance == 1:
                finalOpinion += globals.sources.get(op.sourceName).reputation
            elif opinion.stance == 0:
                finalOpinion -= globals.sources.get(op.sourceName).reputation
    return finalStance/opinions.size

def updateRep(opinions):
    for op in opinions:
        if not globals.sources.contains(op.sourceName):
            globals.sources.update({op.sourceName: source(op.sourceName, 0)})
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
