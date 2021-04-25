from sys import argv
from util import calcNumSuits, convertDictToList, flatten, stringify

players = open(argv[1]).read().split('\n')

accounted_games = set()
variant_stats = {}

for player in players:
    if(player == ''):
        continue
    player_data = open('output/failed_variants/failed_variants_%s.csv'%player, encoding='utf-8').readlines()
    for row in player_data:
        if(row == ''):
            continue
        variant,num_players,attempts,ignore = row.split(',')
        if (variant,num_players) not in variant_stats:
            variant_stats[(variant,num_players)] = 0
        variant_stats[(variant,num_players)] += int(attempts)

variant_stats = convertDictToList(variant_stats)
variant_stats = sorted(variant_stats)

output = open('output/global_failed_variant_stats.csv', 'w')
output.write('\n'.join([','.join(stringify(flatten(i))) for i in variant_stats]))
output.close()