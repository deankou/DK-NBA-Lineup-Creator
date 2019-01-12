from pydfs_lineup_optimizer import get_optimizer, Site, Sport
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv
import pickle
import sys

## This function is used to scrape websites for their projections for a given
## day.

def scrape() :
    proj1 = "https://fantasy5x5.com/nba/projections/"
##    proj2 = "https://www.sportsline.com/nba/player-projections/player-stats/all-players/"


    
# Comment and uncomment the areas between the stars accordingly to use pickle
# for debugging.
##******************************************************************

# Selenium method for scraping Javascript
    driver = webdriver.Firefox()
    driver.get(proj1)
    source1 = driver.execute_script("return document.documentElement.outerHTML")
    soup1 = BeautifulSoup(source1,'html.parser')

# Expands the table to show all players
    select = Select(driver.find_element_by_name('player_table_length'))
    select.select_by_value('-1')

# Rescrape the updated source code that now shows all players
    source1 = driver.execute_script("return document.documentElement.outerHTML")
    
# Pickle useful for debugging and avoiding repeated scrapes
    pickleOut = open("fantasy5x5.pickle", 'wb')
    pickle.dump(source1, pickleOut)
    pickleOut.close()
    soup1 = BeautifulSoup(source1,'html.parser')
    driver.quit()
    
##******************************************************************
    
### If pickle is being used, uncomment this section
##    pickleIn = open("fantasy5x5.pickle",'rb')
##    source1 = pickle.load(pickleIn)
##    soup1 = BeautifulSoup(source1,'html.parser')
    
##******************************************************************


# Get table of players
    tables = (soup1.find_all('table'))
    table = tables[0]
    table_body = table.find('tbody')
    rows = table_body.find_all('tr', style='background-color:')

##    for row in rows:
##        data = row.find_all('td')
##        for col in data:
##            print(col.text)

    plyr = []
    projFP = []

# TODO scrape all relevant data
    for row in rows:
        data = row.find_all('td')
        plyr.append(data[1].text)
        projFP.append(data[19].text)


    with open('5x5proj.csv', 'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(zip(plyr, projFP))

# TODO setup as pandas df

scrape()
