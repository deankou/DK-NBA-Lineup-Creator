from pydfs_lineup_optimizer import get_optimizer, Site, Sport
import pandas as pd
from bs4 import BeautifulSoup
import requests
import scrapeInactives
import os

# Get current working directory
cwd = os.getcwd()
salaryPath = cwd + "\DKSalaries.csv"

# TODO Add Pickle for this so I don't always scrape if file is <5 min old
# Removed to allow for speed in testing
inactives = scrapeInactives.scrape()

# Set up the optimizer
optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASKETBALL)
optimizer.load_players_from_csv(salaryPath)

# Manual remove players
alsoRemove = []
for players in alsoRemove:
    inactives.append(players)

# Manual add players
require = []
alsoAdd = []
for players in alsoAdd:
    require.append(players)

injuries = []
for player in inactives:
    injuries.append(optimizer.get_player_by_name(player))

required = []
for player in require:
    required.append(optimizer.get_player_by_name(player))

for player in required:
    optimizer.add_player_to_lineup(player)

for player in injuries:
    optimizer.remove_player(player)
    
for lineup in optimizer.optimize(n=3, max_exposure=0.3):
    print(lineup)
    
