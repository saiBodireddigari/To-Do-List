def add_viewer(name, team=None):
    if team is None:
        team = []
    team.append(name)
    return team
