import deantools, os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import dataStorage
from bs4 import BeautifulSoup
import itertools
import pandas as pd
import numpy as np


## This function is used to scrape rotogrinders for projections
## They do a pretty good job of making their site hard to scrape....
def scrape() :
    url = "https://rotogrinders.com/projected-stats/nba-player?site=draftkings"
##    proj2 = "https://www.sportsline.com/nba/player-projections/player-stats/all-players/"

# Selenium method for scraping Javascript
    driver = webdriver.Firefox()
    driver.get(url)
    source = driver.execute_script("return document.documentElement.outerHTML")
# JSON here to stop scraping

    soup = BeautifulSoup(source1,'html.parser')
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
