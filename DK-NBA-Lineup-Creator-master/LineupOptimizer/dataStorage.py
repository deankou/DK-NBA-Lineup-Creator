from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pickle
import json
import itertools
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook

import pandas as pd
import numpy as np
import os


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

def storeLineups(lineups, modelName, ymd, todayDir):
        with open(todayDir + '\\' + ymd + modelName + 'lineups.json', 'w') as outfile:
            json.dump(lineups, outfile)
            return

def readLineups(modelName, ymd, todayDir):
        with open(todayDir + '\\' + ymd + modelName +'lineups.json') as infile:
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




## This function is used to scrape NBA nightly statlines for validation purposes
#def scrape() :
#    url = "https://stats.nba.com/players/traditional/?DateFrom=01%2F10%2F2019&DateTo=01%2F10%2F2019&PerMode=Totals&sort=PTS&dir=-1"

    
# Comment and uncomment the areas between the stars accordingly to use pickle
# for debugging.
##******************************************************************

### Selenium method for scraping Javascript
##    driver = webdriver.Firefox()
##    driver.get(url)
##    source = driver.execute_script("return document.documentElement.outerHTML")
##
### Expands the table to show all players
##    select = Select(driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/select"))
##    select.select_by_visible_text("All")
##    source = driver.execute_script("return document.documentElement.outerHTML")
##    
### Pickle useful for debugging and avoiding repeated scrapes
##    pickleOut = open("NBAboxscore.pickle", 'wb')
##    pickle.dump(source, pickleOut)
##    pickleOut.close()
##    
##    driver.quit()
    
##******************************************************************
    
### If pickle is being used, uncomment this section
##    pickleIn = open("NBAboxscore.pickle",'rb')
##    source = pickle.load(pickleIn)
##
##    # CHANGE TO READ JSON WHEN DONE
##    with open('NBAboxscoreSource.json', 'w') as outfile:
##        json.dump(source, outfile)
##    # Read json file
##    with open('NBAboxscoreSource.json') as infile:
##        source = json.load(infile)
####******************************************************************
##    
##    soup = BeautifulSoup(source,'html.parser')    
##
### Get table of players
##    tables = (soup.find_all('table'))
##    table = tables[0]
##    table_head = table.find('thead')
##    headers = table_head.find_all('th')
##    fieldnames = []
##    stats = []
##    for field in itertools.islice(headers,30):
##        fieldnames.append((field.text))
##    fieldnames[0] = "NBA_Stats_ID"
##    stats.append(fieldnames)
##
##  
##    table_body = table.find('tbody')
##    rows = table_body.find_all('tr')
##
##    initList = []
##    for row in rows:
##        data = row.find_all('td')
##        NBA_Stats_IDs = data[1].a.get('href')
##        NBA_Stats_IDs = NBA_Stats_IDs[8:-1]
##
##        for col in data:            
##            initList.append(col.text)
##            initList[0] = NBA_Stats_IDs
##        stats.append(initList)
##        initList = []
##
##
##    for i in stats:
##        for index, j in enumerate(i):
##            if (j.isnumeric()):
##                i[index] = (float(j))
##                
##
##    pd.set_option('display.max_columns', 35)
##    pd.set_option('display.width', 1000)
##    df = pd.DataFrame(stats[1:],columns=stats[0])
##    
##    df['NBA_Stats_ID'] = df['NBA_Stats_ID'].astype(int)
##    df.set_index(['NBA_Stats_ID'],inplace=True)    
##
##    df['DDpts'] = np.where(df['PTS'] >9, 1, 0)
##    df['DDreb'] = np.where(df['REB'] >9, 1, 0)
##    df['DDast'] = np.where(df['AST'] >9, 1, 0)
##    df['DDblk'] = np.where(df['BLK'] >9, 1, 0)
##    df['DDstl'] = np.where(df['STL'] >9, 1, 0)
##    df['#ofDDig'] = (df['DDpts'] + df['DDreb'] +
##                       df['DDast'] + df['DDblk'] +df['DDstl'])
##    df['DoubDoub'] = np.where(df['#ofDDig'] > 2,1,0)
##    df['TripDoub'] = np.where(df['#ofDDig'] == 3,1,0)
##    df['ActFP'] = (df['PTS'] + (0.5 * df['3PM']) + (1.25 * df['REB']) +
##                   (1.5 * df['AST']) + (2 * df['STL']) + (2*df['BLK']) -
##                   (0.5 * df['TOV']) ++ (1.5 * df['DoubDoub']) +
##                   (3*df['TripDoub']))
##    df['concatNameandTeam'] = df['PLAYER'] + df['TEAM']
##
###DATA TYPES ARE NOT CONSISTENT
####    df = df.astype(float)
##
##    
##    df = df.sort_values(by=['ActFP'],ascending=False)
##
##
##
### Write json file
##    df.to_json('NBAboxscore.json')
##
### All three lines should be used
##    dfnew = pd.read_json('NBAboxscore.json', convert_dates=False)
##    dfnew.sort_values(by=['ActFP'],ascending=False,inplace=True)
##    dfnew.index.rename('NBA_Stats_ID',inplace=True)
##
##    print(dfnew.head())
##
##    print(df.equals(dfnew))
###DATA TYPES ARE NOT CONSISTENT
##
##    df.to_csv('temp.csv')
##
