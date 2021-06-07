from os import remove
from sys import argv
from util import calcNumSuits

variants_filename = argv[1]
player = argv[2]
k=argv[3]

variants = open(variants_filename).read().split('\n')
variants = [i[:(i.find('#')-2)] for i in variants]

variants = set(variants)

games=open('output/individual_stats/%s.csv'%player).read().split('\n')

for game in games:
    game_id,num_players,score,variant,*current_players = game.split(',')
    if k != num_players:
        continue
    if variant not in variants:
        continue
    if int(score) == calcNumSuits(variant)*5:
        variants.remove(variant)

variants = sorted(list(variants))
output = open('output/missing_variants_%s_%s_players.csv'%(player,k), 'w')
output.write('\n'.join(variants))
output.close()

# cat ./output/missing_variants_Lel0uch_5_players.csv | grep -v 'Alternating' | grep -v '\-Ones' | grep -v '\-Fives' | grep -v 'Dark' | grep -v 'Black' | grep -v 'Starved' | grep -v 'Null' | grep -v 'Cocoa' | grep -v 'Gray' | grep -v 'Throw' | wc -l