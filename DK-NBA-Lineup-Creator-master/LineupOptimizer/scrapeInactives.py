import pandas as pd
from bs4 import BeautifulSoup
import requests

## This function is used to scrape websites for inactive players
##It includes all players for the current day. It does not consider
##a single slate

def scrapeRotowire():

    url = "https://www.rotowire.com/basketball/nba-lineups.php"
    
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    
    inactives = []
    
# From Rotowire
    for out in soup.find_all('li',class_ = "lineup__player"):
        if (("INACT") in out.text) or (("OUT") in out.text):
            playerURL = ("https://www.rotowire.com" + out.a.get('href'))
            plyrSource = requests.get(playerURL).text
            soup2 = BeautifulSoup(plyrSource,'lxml')
            name = soup2.find('div',class_ = "p-card__player-name")
            inactives.append(name.text)
    return inactives


def scrapeCBS():

    url = "https://www.cbssports.com/nba/injuries/daily/"
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')

    inactives = []
    
# Notice, does not use bs4 method, uses pandas
    tables = pd.read_html(url)
    df = tables[0]
    outsListDirty = df["Player"].values
    for players in outsListDirty:
        inactives.append(players.rsplit('  ', 1)[1])
    return inactives


def scrapeAll() :
    
    inactives = []

#*********Comment out to remove**********************************
    rotoList = scrapeRotowire()
    for plyrs in rotoList:
        inactives.append(plyrs)
#****************************************************************

#*********Comment out to remove**********************************    
    cbsList = scrapeCBS()
    for plyrs in cbsList:
        inactives.append(plyrs)
#****************************************************************

    return inactives


