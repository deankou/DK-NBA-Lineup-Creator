import json
from os import getcwd

def storeModels(modelList, libDir):
        with open(libDir + '\\' + 'models.json', 'w') as outfile:
            json.dump(modelList, outfile)
            return

def readModels():
        with open(getcwd() + '\\lib\\' + 'models.json') as infile:
            modelList = json.load(infile)
            return modelList

def storeInactives(inactivePlayersList, ymd, todayDir):
        with open(todayDir + '\\' + ymd + 'inactive.json', 'w') as outfile:
            json.dump(inactivePlayersList, outfile)
            return

def readInactives(ymd, todayDir):
        with open(todayDir + '\\' + ymd + 'inactive.json') as infile:
            inactivePlayersList = json.load(infile)
            return inactivePlayersList

def storeRemoved(removedPlayersList, ymd, todayDir):
        with open(todayDir + '\\' + ymd + 'removed.json', 'w') as outfile:
            json.dump(removedPlayersList, outfile)
            return

def readRemoved(ymd, todayDir):
        with open(todayDir + '\\' + ymd + 'removed.json') as infile:
            removedPlayersList = json.load(infile)
            return removedPlayersList

def allRemoved(inactives, userRemoved):
    allRemoved = []
    for plyrs in inactives:
        allRemoved.append(plyrs)
    for plyrs in userRemoved:
        allRemoved.append(plyrs)
    return allRemoved

def storeRequired(requiredPlayersList, ymd, todayDir):
        with open(todayDir + '\\' + ymd + 'required.json', 'w') as outfile:
            json.dump(requiredPlayersList, outfile)
            return

def readRequired(ymd, todayDir):
        with open(todayDir + '\\' + ymd + 'required.json') as infile:
            requiredPlayersList = json.load(infile)
            return requiredPlayersList

def storeLineups(lineups, ymd, todayDir):
        with open(todayDir + '\\' + ymd + 'lineups.json', 'w') as outfile:
            json.dump(lineups, outfile)
            return

def readLineups(ymd, todayDir):
        with open(todayDir + '\\' + ymd + 'lineups.json') as infile:
            lineups = json.load(infile)
            return lineups
        
def storeNBAStats(source, ymd, todayDir):
        with open(todayDir + '\\' + ymd + 'NBAboxscoreSource.json', 'w') as outfile:
            json.dump(source, outfile)
            return

def readNBAStats(ymd, todayDir):
        with open(todayDir + '\\' + ymd  +'NBAboxscoreSource.json') as infile:
            source = json.load(infile)
            return source

