from pydfs_lineup_optimizer import get_optimizer, Site, Sport
import pandas as pd

salaryPath = r"C:\Users\Dean Koumoutsos\Documents\Python\LineupOptimizer\DKSalaries.csv"
injurySite = "https://www.cbssports.com/nba/injuries/daily/"
# Set up the optimizer
optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASKETBALL)
optimizer.load_players_from_csv(salaryPath)


tables = pd.read_html(injurySite)
df = tables[0]
outsListDirty = df["Player"].values
outs = []
for player in outsListDirty:
    outs.append(player.rsplit('  ', 1)[1])




injuries = []
for player in outs:
    injuries.append(optimizer.get_player_by_name(player))

for player in injuries:
    optimizer.remove_player(player)
for lineup in optimizer.optimize(n=4, max_exposure=0.6):
    print(lineup)
    
