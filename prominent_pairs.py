from sys import argv
from util import convertDictToList, stringify

players = open(argv[1]).read().split('\n')

output = []

overall_freq = []

for player in players:
    player_data = open('output/individual_stats/%s.csv'%player, encoding='utf-8').readlines()
    player_freq = {}
    for row in player_data:
        if row != '':
            game_id,num_players,score,variant,*current_players=row.strip().split(',')
            for player2 in current_players:
                if not (player2 > player) or player == player2: # don't count dupe pairs 
                    continue
                if player2 not in player_freq:
                    player_freq[player2] = 0
                player_freq[player2] += 1
    player_freq = convertDictToList(player_freq)
    print(player, player_freq)
    player_freq = [[player] + i for i in player_freq if i[1] >= 500]
    overall_freq.extend(player_freq)

output = open('output/prominent_pairs.csv', 'w')
output.write('\n'.join([','.join(stringify(i)) for i in overall_freq]))
output.close()