from functools import reduce
from sys import argv
from util import calcNumSuits,isSingleDark,isDoubleDark,isNonDark,convertDictToList, sortByKth,stringify,flatten,sortByKth

argc = len(argv) 
assert(argc >= 3)

player1 = argv[1]
player2 = argv[2]

filters = []
if argc > 3:
    filters = argv[3:]

games = open('output/individual_stats/%s.csv'%player1).read().split('\n')
games = games[-1:0:-1]

variant_stats = {}

def applyFilter(f, game):
    game_id,num_players,score,variant,*players = game.split(',')
    if len(f)==2 and f[1] == 'p': # 2p,3p,etc.
        if num_players != f[0]:
            return False
    if f=='nondark' and not isNonDark(variant):
        return False
    if f=='singledark' and not isSingleDark(variant):
        return False
    if f=='doubledark' and not isDoubleDark(variant):
        return False
    if 'suits' in f: # 5suits,6suits,etc.
        if calcNumSuits(variant) != ord(f[0])-ord('0'):
            return False
    return True

for game in games:
    # print(game)
    if game == '':
        continue
    valid = True
    if player2 not in game:
        continue
    for f in filters:
        if not applyFilter(f, game):
            valid = False
            break
    if not valid:
        continue
    # print(game)
    game_id,num_players,score,variant,*players = game.split(',')
    if variant not in variant_stats:
        variant_stats[variant] = [0,0] # [played,hasWon]
    if(variant_stats[variant][1]):
        continue
    variant_stats[variant][0]+=1
    if(int(score) == calcNumSuits(variant)*5):
            variant_stats[variant][1] = 1

variant_stats = convertDictToList(variant_stats)
variant_stats = [flatten(i) for i in variant_stats]
variant_stats = sortByKth(variant_stats,1)
variant_stats = sortByKth(variant_stats,2)

output = open('output/pairwise_statistics/pairwise_statistics_%s_%s_%s.csv'%(player1,player2,'_'.join(filters)), 'w')
output.write('\n'.join([','.join(stringify(i)) for i in variant_stats]))
output.close()

attempts = sum(i[1] for i in variant_stats)
won = sum(i[2] for i in variant_stats)

output = open('output/pairwise_statistics/overall_%s.csv'%'_'.join(filters), 'a')
output.write("%s,%s,%d,%d,%s\n"%(player1,player2,attempts,won, ("%.2f"%(attempts*1.0/won) if won !=0 else 'NA')))
output.close()
