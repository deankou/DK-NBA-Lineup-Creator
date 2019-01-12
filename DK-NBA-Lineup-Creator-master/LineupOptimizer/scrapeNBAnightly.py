import deantools, os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import dataStorage
from bs4 import BeautifulSoup
import itertools
import pandas as pd
import numpy as np

## This function is used to scrape NBA nightly statlines for validation purposes
def scrapeNBAStats() :
    month, day, year = deantools.dateNBAStats()
    ymd = deantools.ymd()
    todayDir = os.getcwd() +"\\" + ymd
    url = 'https://stats.nba.com/players/traditional/?DateFrom='+month+'%2F'+day+'%2F'+year+'&DateTo='+month+'%2F'+day+'%2F'+year+'&PerMode=Totals&sort=PTS&dir=-1'

    
# If avoiding repeated scrapes, comment out this section and uncomment the
# section below.
##******************************************************************

# Selenium method for scraping Javascript
    driver = webdriver.Firefox()
    driver.get(url)
    source = driver.execute_script("return document.documentElement.outerHTML")

# Expands the table to show all players
    select = Select(driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/select"))
    select.select_by_visible_text("All")
    source = driver.execute_script("return document.documentElement.outerHTML")
    
# JSON useful for debugging and avoiding repeated scrapes
    dataStorage.storeNBAStats(source, ymd, todayDir)
    driver.quit()
    
##******************************************************************
##    
### If JSON is being used, uncomment this section to avoid extra scrapes.
##    source = dataStorage.readNBAStats(ymd,todayDir)
##    
##******************************************************************
    
    soup = BeautifulSoup(source,'html.parser')    

# Get table of players
    tables = (soup.find_all('table'))
    table = tables[0]
    table_head = table.find('thead')
    headers = table_head.find_all('th')
    fieldnames = []
    stats = []
    for field in itertools.islice(headers,30):
        fieldnames.append((field.text))
    fieldnames[0] = "NBA_Stats_ID"
    stats.append(fieldnames)
    
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    initList = []
    for row in rows:
        data = row.find_all('td')
        NBA_Stats_IDs = data[1].a.get('href')
        NBA_Stats_IDs = NBA_Stats_IDs[8:-1]

        for col in data:            
            initList.append(col.text)
            initList[0] = NBA_Stats_IDs
        stats.append(initList)
        initList = []


    for i in stats:
        for index, j in enumerate(i):
            if (j.isnumeric()):
                i[index] = (float(j))
                

    pd.set_option('display.max_columns', 35)
    pd.set_option('display.width', 1000)
    df = pd.DataFrame(stats[1:],columns=stats[0])
    
    df['NBA_Stats_ID'] = df['NBA_Stats_ID'].astype(int)
    df.set_index(['NBA_Stats_ID'],inplace=True)    

    df['DDpts'] = np.where(df['PTS'] >9, 1, 0)
    df['DDreb'] = np.where(df['REB'] >9, 1, 0)
    df['DDast'] = np.where(df['AST'] >9, 1, 0)
    df['DDblk'] = np.where(df['BLK'] >9, 1, 0)
    df['DDstl'] = np.where(df['STL'] >9, 1, 0)
    df['#ofDDig'] = (df['DDpts'] + df['DDreb'] +
                       df['DDast'] + df['DDblk'] +df['DDstl'])
    df['DoubDoub'] = np.where(df['#ofDDig'] > 2,1,0)
    df['TripDoub'] = np.where(df['#ofDDig'] == 3,1,0)
    df['ActFP'] = (df['PTS'] + (0.5 * df['3PM']) + (1.25 * df['REB']) +
                   (1.5 * df['AST']) + (2 * df['STL']) + (2*df['BLK']) -
                   (0.5 * df['TOV']) ++ (1.5 * df['DoubDoub']) +
                   (3*df['TripDoub']))
    df['concatNameandTeam'] = df['PLAYER'] + df['TEAM']

#DATA TYPES ARE NOT CONSISTENT
##    df = df.astype(float)

    
    df = df.sort_values(by=['ActFP'],ascending=False)



# Write json file
    df.to_json(todayDir+'\\'+ymd+'NBAboxscoredf.json')

# All three lines should be used
    dfnew = pd.read_json('NBAboxscore.json', convert_dates=False)
    dfnew.sort_values(by=['ActFP'],ascending=False,inplace=True)
    dfnew.index.rename('NBA_Stats_ID',inplace=True)

    print(dfnew.head())

    print(df.equals(dfnew))
#DATA TYPES ARE NOT CONSISTENT

    df.to_csv(todayDir+'\\'+ymd+'NBAboxscoredf.csv')

scrapeNBAStats()
