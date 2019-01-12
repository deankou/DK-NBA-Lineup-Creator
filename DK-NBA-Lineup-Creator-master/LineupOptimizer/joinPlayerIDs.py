import os
import json
import msgpack
import pandas as pd
from fuzzywuzzy import fuzz, process

# Get necessary directories
cwd = os.getcwd()
salaryPath = cwd + "\DKSalaries.csv"

# Read json file
with open('lineups.json') as infile:
    lineups = json.load(infile)

# set up pandas programOutputdf
programOutputdf = pd.DataFrame(lineups)
programOutputdf.columns = ['my_lineups' if x==0 else x for x in programOutputdf.columns]

start = '('
end = ')'
programTeams = programOutputdf['my_lineups'].tolist()

find = '/'
lineupsList = programOutputdf['my_lineups'].str[:-5].tolist()


#head, sep, tail = text.partition('...')

progTeam = []
for entry in programTeams:
    progTeam.append(entry[entry.find(start)+len(start):entry.rfind(end)])

my_lineups = []
for entry in lineupsList:
    head = (entry[:entry.rfind(" ")])
    head = (entry[:entry.rfind(" ")])
    head, sep, tail = head.partition(find)

    head, sep, tail = head.partition(" PG")
    head, sep, tail = head.partition(" SG")
    head, sep, tail = head.partition(" SF")
    head, sep, tail = head.partition(" PF")
    head, sep, tail = head.partition(" C")
    my_lineups.append(head)

programOutputdf['progTeam'] = progTeam
programOutputdf['my_lineups'] = my_lineups
programOutputdf['concatNameandTeam'] = programOutputdf['my_lineups'] + programOutputdf['progTeam']

##print(programOutputdf)
##print(programOutputdf.tail())
##print(programOutputdf.shape)




### *********************************************************************



### *********************************************************************

statsdf = pd.read_json('NBAboxscore.json', convert_dates=False)
statsdf.sort_values(by=['ActFP'],ascending=False,inplace=True)
statsdf.index.rename('NBA_Stats_ID',inplace=True)
##print(statsdf.shape)

fulldf = pd.merge(statsdf, programOutputdf, how='inner', on='concatNameandTeam',
                  left_on=None, right_on=None,left_index=False,
                  right_index=False, sort=False,suffixes=('_x', '_y'),
                  copy=True, indicator=True, validate='one_to_many')

print(fulldf.head())

##programOutputList = programOutputdf['ProgConcatNameandTeam'].tolist()
##choices = ['fuzzy fuzzy was a bear', 'is this a test', 'THIS IS A TEST!!']
##print(process.extract("this is a test", choices, scorer=fuzz.ratio))

    
