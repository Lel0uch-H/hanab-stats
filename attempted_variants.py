from sys import argv

players = open(argv[1]).read().split('\n')

output = open('output/attempted_variants.csv','w')

for player in players:
    attempted = set()
    rows=open('output/individual_stats/%s.csv'%player, encoding='utf-8').read().split('\n')
    for row in rows:
        game_id,num_players,score,variant,*players = row.split(',')
        attempted.add(variant+str(num_players))
    output.write('%s,%i\n'%(player,len(attempted)))

output.close()