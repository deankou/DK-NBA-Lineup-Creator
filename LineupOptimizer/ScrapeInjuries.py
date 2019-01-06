### import libraries
##import urllib.request
##from bs4 import BeautifulSoup
##
### specify the url
##quote_page = 'http://www.donbest.com/nba/injuries/'
##
### query the website and return the html to the variable ‘page’
##page = urllib.request.urlopen(quote_page)
##
### parse the html using beautiful soup and store in variable `soup`
##soup = BeautifulSoup(page, 'html.parser')
##
##print(soup)


import pandas as pd
tables = pd.read_html('https://www.cbssports.com/nba/injuries/daily/')
df = tables[0]
outsListDirty = df["Player"].values
outs = []
for player in outsListDirty:
    outs.append(player.rsplit('  ', 1)[1])

