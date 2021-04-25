from sys import argv
from util import convertDictToList,stringify,convertListOfListToCsv,sortBySecond

players = open(argv[1]).read().split('\n')
global_stats_data = open(argv[2]).read().split('\n')
attempted_variants_data = open(argv[3]).read().split('\n')

# build global_stats map
global_stats = {}
for row in global_stats_data:
    if row == '':
        continue
    variant,num_players,total,won = row.split(',')
    global_stats[(variant+str(num_players))] = (float(won)/float(total))

# build attempted variants map
attempted_variants = {}
for row in attempted_variants_data:
    if row == '':
        continue
    player,attempted = row.split(',')
    attempted_variants[player] = int(attempted)

def calcScore(row):
    if(row == ''):
        return 0
    variant,num_players,attempts,ignore=row.split(',')
    return ((100.0/float(attempts))/global_stats[(variant+str(num_players))])

score_stats = []

for player in players:
    input=open('output/variant_wise_first_win/variant_wise_first_win_%s.csv'%(player)).read().split('\n')
    score = sum([calcScore(row) for row in input])/attempted_variants[player]
    score_stats.append([player,score])

score_stats = sortBySecond(score_stats)

output = open('output/player_score_summary6.csv', 'w')
output.write(convertListOfListToCsv(score_stats))
output.close()