from sys import argv
from util import calcNumSuits

player1 = argv[1]
player2 = argv[2]
player3 = argv[3]
max_game_id = int(argv[4]) if len(argv) >=5 else 10**9

games = open("output/individual_stats/%s.csv"%player1).read().split('\n')

perfect = [0,0]
nonzeros = [0,0]
zeros = [0,0]

for game in games:
    if game == '':
        continue
    if player2 not in game:
        continue
    game_id,num_players,score,variant,*players = game.split(',')
    if int(num_players) < 3:
        continue
    if int(game_id) > max_game_id:
        continue
    idx = 0 if player3 in game else 1
    maxScore = calcNumSuits(variant)*5
    # print(game, idx, maxScore)
    if int(score) == 0:
        zeros[idx] += 1
    elif maxScore == int(score):
        perfect[idx] += 1
    else:
        nonzeros[idx] += 1

output = open('output/third_wheel_%s_%s_%s.csv'%(player1,player2,player3), 'w')
output.write(',with,without\n')
output.write('perfect,%d,%d\n'%(perfect[0],perfect[1]))
output.write('nonzero,%d,%d\n'%(nonzeros[0],nonzeros[1]))
output.write('zero,%d,%d\n'%(zeros[0],zeros[1]))
output.close()