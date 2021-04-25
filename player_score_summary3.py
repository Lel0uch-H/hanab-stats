from sys import argv
from util import convertDictToList,stringify,convertListOfListToCsv,sortBySecond

players = open(argv[1]).read().split('\n')

def calcScore(row):
    if(row == ''):
        return 0
    variant,num_players,attempts,ignore=row.split(',')
    return (1.0/float(attempts))

score_stats = []

for player in players:
    input=open('output/variant_wise_first_win/variant_wise_first_win_%s.csv'%(player)).read().split('\n')
    score = sum([calcScore(row) for row in input])
    score_stats.append([player,score])

score_stats = sortBySecond(score_stats)

output = open('output/player_score_summary3.csv', 'w')
output.write(convertListOfListToCsv(score_stats))
output.close()