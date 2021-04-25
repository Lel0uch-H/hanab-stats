from sys import argv
from util import convertDictToList,sortBySecond,convertListOfListToCsv

players = open(argv[1]).read().split('\n')
score_stats ={}

def incrementPlayerScore(player):
    if player not in score_stats:
        score_stats[player] = 0
    score_stats[player] += 1

for player1 in players:
    for player2 in players:
        if player1 < player2:
            rows = open('output/first_win_faceoff/first_win_faceoff_%s_%s.csv'%(player1,player2)).read().split('\n')
            score_diff = 0
            for row in rows:
                if row == '':
                    continue
                variant,num_players,attempts1,ignore1,attempts2,ignore2 = row.split(',')
                score_diff += (1.0/int(attempts1) - 1.0/int(attempts2))
            if score_diff > 0:
                incrementPlayerScore(player1)
            else:
                incrementPlayerScore(player2)

score_stats = convertDictToList(score_stats)
score_stats = sortBySecond(score_stats)

output = open('output/player_score_summary1.csv', 'w')
output.write(convertListOfListToCsv(score_stats))
output.close()