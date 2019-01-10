from pydfs_lineup_optimizer import get_optimizer, Site, Sport
import pandas as pd
from bs4 import BeautifulSoup
import requests

## This function is used to scrape websites for their projections for a given
## day.

def scrape() :
    proj1 = "https://rotogrinders.com/projected-stats/nba-player?site=draftkings"
    proj2 = "https://www.sportsline.com/nba/player-projections/player-stats/all-players/"
    
##    source1 = requests.get(proj1).text
##    soup1 = BeautifulSoup(source1,'lxml')
##    niceForm1 = soup1.prettify()
##
##    file = open("testfile.txt","w")
##    file.write(niceForm1)
##    file.close()
##    
##    for players in soup.find_all('div',class_="rgt-col"):
##        print(players.div)
##        print(1)



    source2 = requests.get(proj2).text
    soup2 = BeautifulSoup(source2,'lxml')
    niceForm2 = soup2.prettify()

    table = soup2.find('table')
    tablerows = table.findall('span', class_="value")

    for tr in tablerows:
        td = tr.findall('td')
        row = [i.text for i in td]
        print(row)

    
### From Rotowire
##    for out in soup.find_all('li',class_ = "lineup__player"):
##        if (("INACT") in out.text) or (("OUT") in out.text):
##            playerURL = ("https://www.rotowire.com" + out.a.get('href'))
##            plyrSource = requests.get(playerURL).text
##            soup2 = BeautifulSoup(plyrSource,'lxml')
##            name = soup2.find('div',class_ = "p-card__player-name")
##            inactives.append(name.text)
##
##            
### From CBS.....TODO convert to beautiful soup method
##    tables = pd.read_html(injurySite2)
##    df = tables[0]
##    outsListDirty = df["Player"].values
##    for players in outsListDirty:
##        inactives.append(players.rsplit('  ', 1)[1])
##    return inactives

scrape()
