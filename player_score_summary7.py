from sys import argv
from util import convertDictToList,stringify,convertListOfListToCsv,sortBySecond

players = open(argv[1]).read().split('\n')
global_stats_data = open(argv[2]).read().split('\n')
attempted_variants_data = open(argv[3]).read().split('\n')
failed_attempts_data = open(argv[4]).read().split('\n')

# build global_stats map
global_stats = {}
failed_attempts = {}
for row in global_stats_data:
    if row == '':
        continue
    variant,num_players,total,won = row.split(',')
    global_stats[(variant+str(num_players))] = (int(won),int(total))
    failed_attempts[(variant+str(num_players))] = 0 # adding this here since some variants have never been failed

# build attempted variants map
attempted_variants = {}
for row in attempted_variants_data:
    if row == '':
        continue
    player,attempted = row.split(',')
    attempted_variants[player] = int(attempted)

# build failed attempts map
for row in failed_attempts_data:
    if row == '':
        continue
    variant,num_players,total = row.split(',')
    failed_attempts[(variant+str(num_players))] = (int(total))

def calcScore(row):
    if(row == ''):
        return 0
    variant,num_players,attempts,ignore=row.split(',')
    return (100.0/float(attempts))/  \
        ((1.0*global_stats[(variant+str(num_players))][0])
            /(failed_attempts[variant+str(num_players)]+global_stats[(variant+str(num_players))][0]))

score_stats = []

for player in players:
    input=open('output/variant_wise_first_win/variant_wise_first_win_%s.csv'%(player)).read().split('\n')
    score = sum([calcScore(row) for row in input])/attempted_variants[player]
    score_stats.append([player,score])

score_stats = sortBySecond(score_stats)

output = open('output/player_score_summary7.csv', 'w')
output.write(convertListOfListToCsv(score_stats))
output.close()