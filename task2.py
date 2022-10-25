def matches(team):
    
    count_matches = 0 
    match = None
    while match != 1:
        ex_team = 0
        if team % 2 != 0:
            ex_team = 1
        match = team // 2
        team = (team // 2) + ex_team
        count_matches += match
    return count_matches

x  = int(input(" n = "))
print(matches(x))