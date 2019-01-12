from deantools import ymd
import dirBuild, scrapeInactives, dataStorage, toexcel
from runOptimizer import runOptimizer
import os


# Are the lineups being created for today?
forToday = True
# TODO should be GUI

# Creates a folder for todays date in the current directory
if forToday:
    # Should probably be its own class
    ymd = ymd()
    dirBuild.createTodayDir(ymd)
    todayDir = os.getcwd() +"\\" + ymd
    salaryPath = todayDir + "\\" + ymd +"DKSalaries.csv"
# TODO Auto salary download and location


# *********************************************************************
# Comment out between stars an uncoment stars after to use JSON
# To adjust the websites being scraped, check scrapeInactives
inactives = scrapeInactives.scrapeAll()

# JSON to save inactives
dataStorage.storeInactives(inactives, ymd, todayDir)

# Manual remove players
userRemoved = [] #Edit here
 



# JSON to save Removed
dataStorage.storeRemoved(userRemoved, ymd, todayDir)

# Returns single list of inactives and user removals
allRemoved = dataStorage.allRemoved(inactives, userRemoved)

###***********************************************************************
### Only uncomment if using previously stored data
##allRemoved= dataStorage.allRemoved(dataStorage.readInactives(ymd, todayDir),
##                                   dataStorage.readRemoved(ymd, todayDir))
##

# ********************************************************************

# Manual add players
userRequired = [] # Edit here
dataStorage.storeRequired(userRequired, ymd, todayDir)

### Only uncommented if using previously stored data. Not sure if i'll have to add variables
##useRequire = readRequired(ymd, todayDir)

modelName = 'A_1.00_Exposure'
amount = 150

[lineupNum, players] = runOptimizer(ymd, todayDir,
                                    modelName, salaryPath,
                                    allRemoved, userRequired,
                                    amount)

toexcel.lineups2excel(modelName,lineupNum,ymd,players,todayDir)
    
