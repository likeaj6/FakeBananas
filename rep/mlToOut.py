import csv
import time
import pandas as pd

DEFAULTSFILEPATH = '/Users/Joshua_Freier/hackMIT/FakeBananas/rep/reputationDict.csv'
NORMALFILEPATH = '/Users/Joshua_Freier/hackMIT/FakeBananas/rep/reputations.csv'

class globals:
    sources = {}

class opinion:
    def __init__(self, sourceName, articleId, stance):
        self.sourceName = sourceName
        self.articleId = articleId
        self.stance = stance

class source:
    """articles #list of strings
    size #int
    reputation #number between -1 and 1 inclusive"""
    def __init__(self, sourceName, reputation, articles, size):
        self.sourceName = sourceName
        self.reputation = reputation
        self.articles = articles
        self.size = size
    def addArticle(self, articleId, articleValidity):
        if not articleId in self.articles:
            self.reputation = (self.reputation*self.size+articleValidity)/(self.size+1)
            self.articles.append(articleId)
            self.size += 1

def returnOutput(mlOut):
    """takes the output of our ml and turns it into a final stances
    :param mlOut: a panda dataframe
    """
    loadReputations(NORMALFILEPATH)
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
    writeToDisk(NORMALFILEPATH)
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
            globals.sources.update({op.sourceName : source(op.sourceName, 0, [], 1)})
        globals.sources.get(op.sourceName).addArticle(op.articleId, compareStance(op, opinions))

def loadReputations(filepath):
    with open(filepath) as csvfile:
        fieldnames = ['source', 'reputation', 'articles', 'size']
        reader = csv.DictReader(csvfile, fieldnames = fieldnames)
        for row in reader:
            print(row['source'])
            globals.sources[row['source']] = source(row['source'], row['reputation'], row['articles'], row['size'])
            globals.sources[row['source']].size = 100 #Only for defaults

def loadDefaultRepsFromDisk(filepath):
    with open(filepath) as csvfile:
        fieldnames = ['source', 'reputation']
        reader = csv.DictReader(csvfile, fieldnames = fieldnames)
        for row in reader:
#            print(row['source'])
            globals.sources[row['source']] = source(row['source'], row['reputation'], [], 100)

def writeToDisk(filepath):
    with open(filepath, 'w') as csvfile:
        fieldnames = ['source', 'reputation', 'articles', 'size']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for k, v in globals.sources.items():
            if(type(v) == source):
                writer.writerow({'source': k, 'reputation': v.reputation, 'articles' : v.articles, 'size' : v.size})
            else:
                print(source)



loadDefaultRepsFromDisk(DEFAULTSFILEPATH)
writeToDisk(NORMALFILEPATH)
