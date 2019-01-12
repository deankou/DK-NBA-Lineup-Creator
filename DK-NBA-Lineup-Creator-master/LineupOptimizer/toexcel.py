import dataStorage
import xlsxwriter
import pandas as pd

##def preprocess():
##    #should open json containing list of models
##    #grab them all and place in spreadsheet format

    
def lineups2excel(modelName,lineupNum,ymd,players,todayDir):
    # Instead of passing it these things, get from JSON
#    readLineups('A_1.00_Exposure,')

    workbook = xlsxwriter.Workbook(todayDir + "\\" + ymd + 'Lineups.xlsx')
    lineupSht = workbook.add_worksheet('Lineups')
    fieldNames = ["modelName","lineup_#", "position", "name","team","NBA_ID", "projFP", "actFP"]

    row = 0
    col = 0
    for field in fieldNames:
        lineupSht.write(row, col, field)
        col += 1

    row = 1
    for i,plyr in enumerate(players): #Clean up players
        lineupSht.write(row, 0, str(modelName))
        lineupSht.write(row, 1, lineupNum[i])
#        lineupSht.write(row, 2, position)
        lineupSht.write(row, 3, str(plyr))
        if row%9 == 0:
            lineupSht.write(row, 5, 'total')
        row += 1


    workbook.close()

