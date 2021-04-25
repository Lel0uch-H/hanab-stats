from sys import argv

players = open(argv[1]).read().split('\n')

output = open('output/won_variants.csv','w')

for player in players:
    won_count=open('output/variant_wise_first_win/variant_wise_first_win_%s.csv'%player, encoding='utf-8').read().count('\n')+1
    output.write('%s,%i\n'%(player,won_count))

output.close()