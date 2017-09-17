import csv
def transfer():
    ##a one time helper function to transfer our big csv of fake news sources
    ## to be part of our reputation dict
    badSources = []
    with open('opensources/sources/sources.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for i in reader:
            badSources.append(i[0])
    with open('reputationDict.csv', 'w') as csvfile:
        fieldnames = ['source', 'reputation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for source in badSources:
            writer.writerow({'source': source, 'reputation': -1})


transfer()
