# https://www.algoexpert.io/questions/tournament-winner

# O(n) time | O(k)
# k == number of teams, n == number of competitions
def tournamentWinner(competitions, results):
    best_team = ''
    scores = {best_team: 0}
    for couple, win in zip(competitions, results):
        home, away = couple
        winner = home if win == 1 else away
        scores[winner] = 3 + scores.get(winner, 0)
        if scores[winner] > scores[best_team]:
            best_team = winner
    return best_team


if __name__ == '__main__':
    assert tournamentWinner(
        competitions=[
            ["HTML", "C#"],
            ["C#", "Python"],
            ["Python", "HTML"]
        ],
        results=[0, 0, 1]
    ) == 'Python'
