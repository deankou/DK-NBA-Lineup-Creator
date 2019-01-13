

# Cleans up the data coming out of the lineup optimizer

def cleanNamesAndTeams(player_pos_team):

    player_name = []
    team = []
    for entry in player_pos_team:
        head = (entry[:entry.rfind(" ")])
        head = (entry[:entry.rfind(" ")])
        head, sep, tail = head.partition('/')
        if head[-3:] == " PG":
            head = head[:-3]
        if head[-3:] == " SG":
            head = head[:-3]
        if head[-3:] == " SF":
            head = head[:-3]
        if head[-3:] == " PF":
            head = head[:-3]
        if head[-2:] == " C":
            head = head[:-2]
        player_name.append(head)

    bad_team = [i.replace('(GS)', '(GSW)') for i in player_pos_team]
    bad_team = [i.replace('(NY)', '(NYK)') for i in bad_team]
    bad_team = [i.replace('(SA)', '(SAS)') for i in bad_team]
    bad_team = [i.replace('(NO)', '(NOP)') for i in bad_team]


    for entry in bad_team:
        head, sep, tail = entry.partition("(")
        head, sep, tail = tail.partition(")")
        team.append(head)
    


    return player_name, team
