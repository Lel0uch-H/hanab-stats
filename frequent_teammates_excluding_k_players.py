from sys import argv
from util import convertDictToList, flatten, sortBySecond, stringify

player = argv[1]
k = argv[2]
variant_stats = {}

player_data = open('output/individual_stats/%s.csv'%player, encoding='utf-8').readlines()
player_data = player_data[-1:0:-1]

freq = {}

for row in player_data:
    if row != '':
        game_id,num_players,score,variant,*current_players=row.strip().split(',')
        if num_players != k:
            for teammate in current_players:
                if teammate == player:
                    continue
                if teammate not in freq:
                    freq[teammate] = 0
                freq[teammate] += 1

freq = convertDictToList(freq)
freq = sortBySecond(freq)

output = open('output/frequent_teammates/frequent_teammates_excluding_%s_players_%s.csv'%(k,player), 'w')
output.write('\n'.join([','.join(stringify(flatten(i))) for i in freq]))
output.close()