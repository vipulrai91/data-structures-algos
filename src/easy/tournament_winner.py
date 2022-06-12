from cgitb import reset
from collections import defaultdict

competitons = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]


def tournamentWinner(competitions, results):
    team_dict = defaultdict(int)

    for index, value_pair in enumerate(competitions):
        val = value_pair[::-1]
        team_dict[val[results[index]]] += 1
    return max(team_dict, key=team_dict.get)


print(tournamentWinner(competitions=competitons, results=results))
