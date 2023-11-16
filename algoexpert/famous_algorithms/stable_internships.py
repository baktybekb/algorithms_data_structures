# https://www.algoexpert.io/questions/stable-internships

# O(n^2) time | O(n^2) space, n --> number of interns/teams
def stableInternships(interns, teams):
    free_interns = list(range(len(interns)))
    rank_choices = [0] * len(interns)  # tracker of intern's choices
    team_maps = []
    for intern_preferences in teams:
        team = [0] * len(interns)
        for rank, intern in enumerate(intern_preferences):
            team[intern] = rank
        team_maps.append(team)
    matched_pairs = [-1] * len(teams)

    while free_interns:
        intern = free_interns.pop()
        team_preferences = interns[intern]
        desired_team = team_preferences[rank_choices[intern]]
        rank_choices[intern] += 1
        if matched_pairs[desired_team] == -1:
            matched_pairs[desired_team] = intern
            continue
        previous_intern = matched_pairs[desired_team]
        intern_preferences = team_maps[desired_team]
        if intern_preferences[previous_intern] < intern_preferences[intern]:
            free_interns.append(intern)
        else:
            matched_pairs[desired_team] = intern
            free_interns.append(previous_intern)
    return [[intern, team] for team, intern in enumerate(matched_pairs)]
