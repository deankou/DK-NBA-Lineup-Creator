from pydfs_lineup_optimizer import get_optimizer, Site, Sport, CSVLineupExporter
import json
import dataStorage

# add exposure option
def runOptimizer(ymd,todayDir,modelName,salaryPath,allRemoved,userRequired,amount):

# Set up the optimizer
    optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASKETBALL)
    optimizer.load_players_from_csv(salaryPath)

# Locate the players name object
    takeOut = []
    for plyr in allRemoved:
        takeOut.append(optimizer.get_player_by_name(plyr))
    keepIn = []
    for plyr in userRequired:
        keepIn.append(optimizer.get_player_by_name(plyr))

# Actually add and remove from optimizer
    for plyr in keepIn:
        optimizer.add_player_to_lineup(plyr)

    for plyr in takeOut:
        optimizer.remove_player(plyr)

    count = 1
    lineupNum = []
    players = []
# TODO add exposure option
    for lineup in optimizer.optimize(n=amount): #Exposures gets added here max_exposure=0.3
        for plyrs in lineup.players:
            lineupNum.append(count)
            players.append(str(plyrs))
        count += 1
        players.append("")
        lineupNum.append("")

# List for storage
    lineups = []
    lineups.append(lineupNum)
    lineups.append(players)
    dataStorage.storeLineups(lineups, modelName, ymd, todayDir)
    

    return [lineupNum, players]

    
