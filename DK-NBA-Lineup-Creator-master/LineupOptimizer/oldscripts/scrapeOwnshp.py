from pydfs_lineup_optimizer import get_optimizer, Site, Sport
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select

## This function is used to scrape websites for their projections for a given
## day.

def scrape() :
    proj1 = "https://fantasy5x5.com/nba/projections/"
##    proj2 = "https://www.sportsline.com/nba/player-projections/player-stats/all-players/"
    


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
    soup1 = BeautifulSoup(source1,'html.parser')

# Get table of players
    tables = (soup1.find_all('table'))
    print(tables[0])

# TODO setup as pandas df
    
##    niceForm1 = soup1.prettify()
##    print(niceForm1)
    
##    file = open("testfile.txt","w")
##    file.write(niceForm1)
##    file.close()
    
##    for players in soup1.find_all('div',class_="ag-body-container"):
##        print(players.div)
##        print(1)



##    source2 = requests.get(proj2).text
##    soup2 = BeautifulSoup(source2,'lxml')
##    niceForm2 = soup2.prettify()
##
##    table = soup2.find('table')
##    tablerows = table.findall('span', class_="value")

##    for tr in tablerows:
##        td = tr.findall('td')
##        row = [i.text for i in td]
##        print(row)

    
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
    driver.quit()
scrape()
