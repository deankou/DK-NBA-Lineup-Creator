from pydfs_lineup_optimizer import get_optimizer, Site, Sport
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
#from selenium.webdriver.support.ui import Select

## This function is used to scrape websites for their projections for a given
## day.

def scrape() :
    proj1 = "https://rotogrinders.com/projected-stats/nba-player?site=draftkings"
##    proj2 = "https://www.sportsline.com/nba/player-projections/player-stats/all-players/"

# Selenium method for scraping Javascript
    driver = webdriver.Firefox()
    driver.get(proj1)
    source1 = driver.execute_script("return document.documentElement.outerHTML")
    soup1 = BeautifulSoup(source1,'html.parser')
    print(soup1.prettify)




















    
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



##    source2 = requests.get(proj2).text
##    soup2 = BeautifulSoup(source2,'lxml')
##    niceForm2 = soup2.prettify()
##
##    table = soup2.find('table')
##    tablerows = table.findall('span', class_="value")
##
##    for tr in tablerows:
##        td = tr.findall('td')
##        row = [i.text for i in td]
##        print(row)

    

##    return inactives
    driver.quit()
scrape()
