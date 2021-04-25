from sys import argv
from util import calcNumSuits, convertDictToList, flatten, stringify

players = open(argv[1]).read().split('\n')

accounted_games = set()
variant_stats = {}

for player in players:
    if(player == ''):
        continue
    player_data = open('output/individual_stats/%s.csv'%player, encoding='utf-8').readlines()
    for row in player_data:
        if row != '':
            game_id,num_players,score,variant,*current_players=row.split(',')
            if(game_id in accounted_games):
                continue
            accounted_games.add(game_id)
            if (variant,num_players) not in variant_stats:
                variant_stats[(variant,num_players)] = [0,0] # [played,won]
            variant_stats[(variant,num_players)][0] += 1
            # print(int(score), calcNumSuits(variant)*5)
            if(int(score) == calcNumSuits(variant)*5):
                # print("Max score!")
                variant_stats[(variant,num_players)][1] += 1

variant_stats = convertDictToList(variant_stats)
variant_stats = sorted(variant_stats)

output = open(argv[2], 'w')
output.write('\n'.join([','.join(stringify(flatten(i))) for i in variant_stats]))
output.close()