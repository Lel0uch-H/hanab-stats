from sys import argv
from util import calcNumSuits, convertDictToList, flatten, stringify

player = argv[1]
variant_stats = {}

player_data = open('output/individual_stats/%s.csv'%player, encoding='utf-8').readlines()
player_data = player_data[-1:0:-1]

for row in player_data:
    if row != '':
        game_id,num_players,score,variant,*current_players=row.split(',')
        if (variant,num_players) not in variant_stats:
            variant_stats[(variant,num_players)] = [0,0] # [played,hasWon]
        if(variant_stats[(variant,num_players)][1]):
            continue
        variant_stats[(variant,num_players)][0] += 1
        if(int(score) == calcNumSuits(variant)*5):
            variant_stats[(variant,num_players)][1] = 1

variant_stats = convertDictToList(variant_stats)
variant_stats = [i for i in variant_stats if i[1][1]==1 ]
variant_stats = sorted(variant_stats)

output = open('output/variant_wise_first_win/variant_wise_first_win_%s.csv'%player, 'w')
output.write('\n'.join([','.join(stringify(flatten(i))) for i in variant_stats]))
output.close()