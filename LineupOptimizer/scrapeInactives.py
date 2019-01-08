from pydfs_lineup_optimizer import get_optimizer, Site, Sport
import pandas as pd
from bs4 import BeautifulSoup
import requests

## This function is used to scrape websites for inactive players
##It includes all players for the current day. It does not consider
##a single slate

def scrape() :
    salaryPath = r"C:\Users\Dean Koumoutsos\Documents\Python\First-Lineup-Creator-master\LineupOptimizer\DKSalaries.csv"
    injurySite = "https://www.cbssports.com/nba/injuries/daily/"
    
    injurySite1 = "https://www.rotowire.com/basketball/nba-lineups.php"
    injurySite2 = "https://www.cbssports.com/nba/injuries/daily/"
    
    source = requests.get(injurySite1).text
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

            
# From CBS.....TODO convert to beautiful soup method
    tables = pd.read_html(injurySite2)
    df = tables[0]
    outsListDirty = df["Player"].values
    for players in outsListDirty:
        inactives.append(players.rsplit('  ', 1)[1])
    return inactives

